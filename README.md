# CRUD_API_FLASK

## Start the APP

``` bash
# Activate virtual-ENV
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DataBase
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```
## Endpoints

* GET     /product
* GET     /product/:id
* POST    /product
* PUT     /product/:id
* DELETE  /product/:id
