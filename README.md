# scrapy

## Building docker container

```bash 
docker build -t tricityserver:0.0.0 .

```


## Running docker container

```bash  
docker run --add-host=mongoservice:172.17.0.1 tricityserver:0.0.0 

```

docker run -ti --add-host=mongoservice:172.17.0.1 tricityserver:0.0.0 sh 


## Upgrade with helm with creating namespace

```bash
cd ./k8s/charts/
helm upgrade mongodb mongodb --namespace mongodb --install --create-namespace
```

### CNI for Minikube prerequisite
```bash
curl -LO cni.tgz https://github.com/containernetworking/plugins/releases/download/v1.3.0/cni-plugins-linux-amd64-v1.3.0.tgz
sudo mkdir -p /opt/cni/bin
sudo mv cni.tgz /opt/cni/bin
sudo tar zxvf cni.tgz
```

### Starting minikube cluster
```bash
export CHANGE_MINIKUBE_NONE_USER=true
sudo sysctl fs.protected_regular=0
sudo -E minikube start --driver=none --extra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf

```

kubectl port-forward svc/mongodb 27018:27017
kubectl port-forward svc/mongodb 27018:27017

# restore mongodb
```bash
kubectl port-forward svc/mongodb 27018:27017  # fir
# change port in setting for scrapy to 27018
sudo cp -r /home/aneta/software/repos/scrapy/db=tricity /tmp/hostpath-provisioner/mongodb/mongodb/data/db/
kubectl exec -it mongodb-85458765c5-wgf8s -- bash
# next command inside continaer after running -- kubectl exec a
mongorestore -d tricity -u scrapy -p scrapy1234 --drop  --authenticationDatabase admin ./db=tricity/tricity
```
mongorestore -u root -p $MONGODB_ROOT_PASSWORD
kubectl exec -it mongodb-85458765c5-wgf8s -- bash
/bitnami/mongodb
zVoN1cyxP0

mongorestore -d tricity --drop  ./db=tricity/tricity

sudo cp -r /home/aneta/software/repos/scrapy/db=tricity /tmp/hostpath-provisioner/mongodb/mongodb/data/db/

Additional node config if coredns is not working
```bash
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -F
```