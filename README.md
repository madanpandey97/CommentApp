# CommentApp
A Comment app to create and fetch comment 

Short Description 
Following feature includes in this api
* Create User 
* Login with User credential 
* Create Update delete Retrieve Comment 
* Add a reply on the existing comment 
* delete main thread comment or existing reply 

Note The comment and sub comment is user specific no other user can delete or update comment created by other user 
## please import the following postman collection link to get the details of api 
Please pass the require params in body 
``` 
https://www.getpostman.com/collections/a286fd4566976b0fde04
```

## To run the Product 

Clone this repository on your system 
make sure you have python installed version greater then  3.5
please create virtualenv (suggestion please use pycharm for defalut virtual env ) 
This project use postgresql database so make sure you insall that or replace the database variable in setting.py file to make it work with sqlite database 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
pleaee run the command in order to run this code 
* pip install -r requirements.txt
* python manage.py makemigrations 
* python manage.py migrate 
* python manage.py runserver 
