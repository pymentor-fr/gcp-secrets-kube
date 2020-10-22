import base64
import logging
import sys
import yaml

import click
from google.cloud import secretmanager


LABEL_NS_STARTSWITH = 'k8s-ns'
OUTPUT_FILE = 'secrets.yaml'


def get_namespaces(client, project_id, secret_name):
    logger.info(f'Get namespaces from labels starting with {LABEL_NS_STARTSWITH}')
    name = client.secret_path(project_id, secret_name)
    response = client.get_secret(request={"name": name})
    namespaces = [response.labels[l] for l in response.labels if l.startswith(LABEL_NS_STARTSWITH)]
    return namespaces


def get_secret_value(client, project_id, secret_name, version):
    name = f"projects/{project_id}/secrets/{secret_name}/versions/{version}"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data
    return payload


def build_secret_manifest(name, namespace, key, value):
    logger.info('Build secret manifest')
    secret = {
        'apiVersion': 'v1',
        'kind': 'Secret',
        'metadata': {'name': name, 'namespace': namespace},
        'type': 'Opaque',
        'data': {
            key: value,
        }
    }
    return secret
    return yaml.dump(secret)


handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger('gcp_secrets_kube')
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@click.command()
@click.argument('project_id')
@click.argument('secret_name')
@click.option('--version', default='latest')
def launch(project_id, secret_name, version):
    client = secretmanager.SecretManagerServiceClient()
    secret_value = get_secret_value(client, project_id, secret_name, version)
    b64_value = base64.b64encode(secret_value).decode("utf-8")
    namespaces = get_namespaces(client, project_id, secret_name)
    res = [build_secret_manifest(secret_name, ns, secret_name, b64_value) for ns in namespaces]
    logger.info(f'Writing file {OUTPUT_FILE}')
    with open(OUTPUT_FILE, 'w') as file:
        yaml.dump_all(res, file)


if __name__ == '__main__':
    launch()
