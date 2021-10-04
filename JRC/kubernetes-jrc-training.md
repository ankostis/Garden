# Kubernetes JRC Training

- doc: https://kubernetes.io/docs/reference/kubernetes-api/

echo -e '\nsource <(kubectl completion bash)\n' >> ~/.bashrc

## master node
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

## for each node:
sudo kubeadm join 172.31.4.94:6443 --token s99adr.q3wjstujf1rjceun \
--discovery-token-ca-cert-hash sha256:8bb4eb3c372738e3fbcf498f9edbbd772571b87f7e829a97455e813106cb1b45

## Admin commands

kubectl get all -A

kubectl get node
kubectl get namespace  # or `kubectl get ns`
kubectl get pod -n kube-system

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl get pod -n kube-system
kubectl get node

kubectl describe nodes ip-master
kubectl describe nodes ip-node1
kubectl describe nodes ip-node2

kubectl get pod -n kube-system -o wide
kubectl logs -n kube-system <pod>

### Role-Based AC
kubectl get roles.rbac.authorization.k8s.io -A

kubectl get clusterrole -A
kubectl describe clusterrole admin

kubectl get serviceaccount
kubectl describe serviceaccounts default
    kubectl create serviceaccount -o yaml --dry-run

### Deploy a pod

Produce an yaml:

    kubectl run myfirstpod --image=nginx:1.19 --dry-run -o yaml > myfirst.yaml

Trim yaml:

~/myfirstpod
```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: myfirstpod
  name: myfirstpod
spec:
  containers:
  - image: nginx:1.19
    name: myfirstpod
```

kubectl apply -f myfirstpod.yaml

kubectl run myfirstpod --image=nginx:1.19

kubectl describe pod myfirstpod
kubectl describe pod  # all pods in `default` ns

kubectl get pod myfirstpod -o yaml

kubectl delete pod myfirstpod

kubectl exec -it myfirstpod -- bash

### Hide a cluster IP behind a Service

sample: lab/01b-two-container.yaml
...

kubectl create service clusterip <name> <port>:<targetPort> --dry-runner
then edit & apply

kubectl get endpoints

```yaml
apiVersion: v1
kind: Service
metadata:  name: svc-frontend
spec:  ports:  - name: 80-80
    port: 80
    protocol: TCP
    targetPort: 80
selector:
    app: svc-frontend
type: ClusterIP
```
### Deployements
file: 11a-ngnix-...

    kubectl rollout status deployment nginx
    kubectl rollout history deployment nginx
    kubectl rollout history deployment --revision=3
    kubectl rollout undo deployment nginx --to-revision 1

### Services

file: 11b-ngnix-...

    kubectl apply -f 11b-nginx-deploy-service.yaml
    kubectl get pod --show-labels
    kubectl get service
    kubectl describe service servicenginx

### Docker Registry

- harbor.io FOSS installable registry

### Quotas per ns

file: 10-quota.yaml
prometheus.io

### Git org

helm.sh

### DBs & Stateful apps

- k8s `statefulset` (not `deployment`)

## Questions

- Q: confusing to deal with names (internal/external IPs, DNS) - how to assign own names?
  - Q: how not to hard-code IPs?  SERVICES?  LABELs
- Q: how to organize applicable files in Git?  HELM
- Q: is there a modus operandi for starting small and augmenting files while migrating pods-->deployments & hooking services?
- Q: gateways/ingress
- Q: clean up/gc leave behind resources?  YES, linstall distribution
- Q: Change certificate to include another IP?

Martino Fornasa
- Q: Network config? https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml