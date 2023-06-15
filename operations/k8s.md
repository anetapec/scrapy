### Helm deployment

```bash
cd ~/software/repos/scrapy/k8s/charts

# helm upgrade [RELEASE] [CHART] [flags]

helm upgrade release1 mongodb --install --create-namespace --namespace mongodb --values mongodb/values.yaml --values mongodb/values/common-values.yaml --wait

```


### K8s namespaces
```bash
kubectl get ns
kubectl create ns test1
```


### K8s context / config
```bash

kubectl config set-context --current --namespace mongodb # setting global namesapces in config
kubectl get po -n kube-system # getting pods from specific namespace -n kube-system
```


### K8s pods 

```bash
kubectl get events # check namespace event for last 1h
kubectl get po

## Check status of the POD should be RUNNING here is a problem with pulling image due to poor network -> ImagePullBackOff
##aneta@aneta-VirtualBox:~/software/repos/scrapy/k8s/charts$ kubectl get po 
NAME                             READY   STATUS             RESTARTS   AGE
release1-mongodb-8969958-8sffv   0/1     ImagePullBackOff   0          4m13s 


### HERE IS OK
NAME                             READY   STATUS    RESTARTS   AGE
release1-mongodb-8969958-8sffv   1/1     Running   0          9m47s
```

### K8s services connect via service with port-forward
```bash
kubectl get svc 

kubectl port-forward svc/mongodb 27018:27017 # local-port:k8s-pod-port

```



