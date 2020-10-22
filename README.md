# Why gcp-secrets-kube

Store your secrets in GCP secret manager and deploy your secrets on Kubernetes the gitops way.
Gitops offers observability and control on your Kubernetes cluster, but secrets cannot be saved in
the git repository. With gcp-secrets-kube extract your secrets from gcp create your manifests then
seal your secrets with [seal-secrets](https://github.com/bitnami-labs/sealed-secrets) and add your
sealed secrets to your gitops repository.

# Features
Assign namespaces according to dedicated secrets labels

# Installation

`pip install gcp-secrets-kube

# Run
Latest secret version:
` gcp-secrets-kube PROJECT_ID SECRET_ID

Specific version
` gcp-secrets-kube PROJECT_ID SECRET_ID --version 123
