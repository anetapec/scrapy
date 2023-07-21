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
## Mongo dump
```bash
cd scrapy
mongodump --out=db=tricity
```