# Generic Blog API
A basic version of a blog API using Flask with SqlAlchemy. Meaning of basic is that there's no use of Blueprints, routing classes or Swagger.
Just plain routing functions. a simplified docs page is included on the homepage.

## Tech

![](https://img.shields.io/static/v1?style=for-the-badge&label=Python&message=3.10&color=006600&logo=python)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Flask&message=2.0&color=006600&logo=jetbrains)   
![](https://img.shields.io/static/v1?style=for-the-badge&label=Pycharm&message=2021.3.2&color=006600&logo=pycharm)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Sqlite&message=3.0&color=006600&logo=sqlite)  

## Get all posts

**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/&color=005599)

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/
```

**Response**

```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": Integer,
    "title": String,
    "slug": String,
    "body": String,
    "author": String,
    "created": DateTime,
    "updated": DateTime,
    "status": String,
    "featured": Boolean
}
```

## Create Post
**Request**

![](https://img.shields.io/static/v1?label=POST&message=/api/posts/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/
```
**Response**
```text
HTTP/1.1 201 OK
Content-Type: application/json
```
```json
{
    "title": String,
    "body": String,
    "status": String,
    "featured": Boolean
}
```

## Get single post
**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/posts/<int:pk>/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": Integer,
    "title": String,
    "slug": String,
    "body": String,
    "author": String,
    "created": DateTime,
    "updated": DateTime,
    "status": String,
    "featured": Boolean
}
```

## Update post
**Request**

![](https://img.shields.io/static/v1?label=PUT&message=/api/posts/:pk&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
* Since it's a Patch request each item can be updated individually (except update date)
```json
{
    "title": String,
    "body": String,
    "status": String,
    "featured": Boolean
}
```

## Delete post
**Request**

![](https://img.shields.io/static/v1?label=DELETE&message=/api/posts/<int:pk>/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/posts/:pk
```
```text
HTTP/1.1 204 OK
Content-Type: application/json
```

**Response**
```text
[]
```

## Additional packages used

* [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [Marshmallow-Sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
* [Gunicorn](https://gunicorn.org/)  // Python WSGI HTTP Server for UNIX

### Notes

* Requirements.txt file is included





