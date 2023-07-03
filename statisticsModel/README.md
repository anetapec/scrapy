## Create / activate  virtual environment:

```bash

python3 -m venv venv   # create
source venv/bin/activate  #activate
```

# install django 
```bash
pip install Django
```

##  Start a Django project
```bash
# go to folder where project is 

django-admin startproject <project_name>
```
# create an app 
```bash
python3 manage.py startapp myfirstapp
```
###  Start the server using 
```bash
 python3 manage.py runserver
```

## Instal dnspython for using mongodb+srv:// URIs
```bash
pip install dnspython
```

### Create the collections in MongoDB
```bash
python3 manage.py makemigrations <app-name>
```

```bash
python3 manage.py migrate
```