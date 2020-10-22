# Why gcp-secrets-kube?

Store your secrets in [GCP secret manager](https://cloud.google.com/secret-manager) and build your
manifests for your favourite gitops tool.

# Features
- Transform secrets from GCP secret manager to k8s secrets manifests
- Assign k8s namespaces according to dedicated secrets labels
- One to many relationship between GCP secrets and k8s secrets (with namespaces). *Don't repeat yourself!*

# Install

`pip install gcp-secrets-kube`

# Run
Get a secrets.yaml file by running:   
`gcp-secrets-kube PROJECT_ID SECRET_ID  # latest secret version`  
or  
`gcp-secrets-kube PROJECT_ID SECRET_ID --version 123`

# Miscellaneous
Build secrets in GCP and add labels like `k8s-ns-xxx` with the namespace as the value. xxx could be 1, 2 or 3... according to how many namespaces you want the secret to be configured in.

# Example of gitops approach with sealed-secrets
Gitops offers observability and control on your Kubernetes cluster, but secrets cannot be saved in
the git repository. With *gcp-secrets-kube* extract your secrets from gcp, create your manifests,
seal your secrets with [seal-secrets](https://github.com/bitnami-labs/sealed-secrets) then add your
sealed secrets to your gitops repository.

Seal your secrets in one command line:  
`kubeseal <secrets.yaml -o yaml`
