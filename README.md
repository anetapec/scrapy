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
sudo -E minikube start --driver=none --driver=none

```


