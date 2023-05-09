# scrappy
## Make sure you've the latest version of our packages installed.
```bash
sudo apt-get update
sudo apt install tree
```

## install python3-venv
```bash
sudo apt install -y python3-venv
```

## Create a new virtual environment:

```bash
cd flats
python3 -m venv venv
source venv/bin/activate
```
## Install Scrapy in our virtual environment.
```bash
pip install scrapy 
```
# Building our  Scrapy spider.
## Creating  Scrapy Project
```bash
scrapy startproject flatsscraper
```
## Creating Spider
```bash
scrapy genspider flatsspiders dom.trojmiasto.pl
```
## Open shell
```bash
scrapy shell
```
## Install ipython
```bash
pip3 install ipython

# in scrapy.cfg
[settings]
default = chocolatescraper.settings
shell = ipython
```
## Create CSS selector in scrapy shell
```bash
fetch('https://dom.trojmiasto.pl/nieruchomosci-rynek-wtorny/e1i,27_60_17_14_13_18_16_24_19_25_6_15_61_20_21,ii,1,qi,45_,wi,100.html')

```


