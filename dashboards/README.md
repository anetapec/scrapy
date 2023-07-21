# Create  Backups Collections Mongo

```bash
cd aneta/software/repos/scrapy

mongodump --out=db=tricity

```
# For restoring the complete folder exported by mongodump:

```bash
mongorestore -d db=tricity /path/

#  for me : path = /home/aneta/software/repos/scrapy/dashboards/venv/lib/python3.8/site-packages/pymongo
```
