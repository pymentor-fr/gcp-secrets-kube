from setuptools import setup, find_packages

setup(
    name='gcp-secrets-kube',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=[
        'google-cloud-secret-manager==2.0.0',
        'click==7.1.2',
    ],
    entry_points='''
        [console_scripts]
        gcp-secrets-kube=gcp_secrets_kube.main:launch
    ''',
)
