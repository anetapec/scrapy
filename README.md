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