
# Django Blog With APT Endpoints Built With Django Rest Framework 
- Blog built with Django
- Blog API built with Django-Rest-Framework 
- Live Deployment: http://dyclin99.pythonanywhere.com/

## Tech & Tools:
- Python 3.6
- Django
- Django REST framework
- Django REST framework JWT

## To Use
1. git clone this repository to your computer
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. run http://localhost:8000/



## Structure
In this application, we provide endpoints for users to access the blog posts and blog comments from using the HTTP methods - GET, POST, PUT, DELETE.

In our case, we have one single resource, `movies`, so we will use the following URLS - `/movies/` and `/movies/<id>` for collections and elements, respectively:

For blog post:
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`posts` | GET | READ | Get all posts
`posts/:slug` | GET | READ | Get a single post
`posts/create/`| POST | CREATE | Create a new post
`movies/:slug/update` | PUT | UPDATE | Update a post
`movies/:slug/delete` | DELETE | DELETE | Delete a post

For blog comment:
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`comments` | GET | READ | Get all comments
`comments/:id` | GET | READ | Get a single comment
`comments/create/`| POST | CREATE | Create a new comment
`comments/:id` | PUT | UPDATE | Update a comment
`comments/:id` | DELETE | DELETE | Delete a comment

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
  python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
  http  http://127.0.0.1:8000/api/v1/movies/3
```
we get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
  http http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
we get the movie with id = 3
```
{  "title":  "Avengers",  "genre":  "Superheroes",  "year":  2012,  "creator":  "admin"  }
```

## Login and Tokens

To get a token first we have to login
```
  http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

The API has some restrictions:
-   The movies are always associated with a creator (user who created it).
-   Only authenticated users may create and see movies.
-   Only the creator of a movie may update or delete it.
-   Unauthenticated requests shouldn't have access.

### Commands
```
http http://127.0.0.1:8000/api/v1/movies/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>"
http POST http://127.0.0.1:8000/api/v1/movies/ "Authorization: Token <YOUR_TOKEN>" title="Ant Man and The Wasp" genre="Action" year=2018
http PUT http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>" title="AntMan and The Wasp" genre="Action" year=2018
http DELETE http://127.0.0.1:8000/api/v1/movies/3 "Authorization: Token <YOUR_TOKEN>"
```

### Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page=size=X
```
http http://127.0.0.1:8000/api/v1/movies/?page=1 "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/api/v1/movies/?page=3 "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/api/v1/movies/?page=3&page_size=15 "Authorization: Token <YOUR_TOKEN>"
```

Finally, I provide a DB to make these tests.




# Functions:
- User:
  - Purchase products as a logged in or a guest user.
- Logged In User:
  - Login and Signup Pages
  ![image](readme_images/login_signup_pages.png)
  - Forget Password, Reset via Email
  ![image](readme_images/reset_password1.png)
  ![image](readme_images/reset_password2.png)
  ![image](readme_images/reset_password3.png)
  - Change Password
  ![image](readme_images/change_password.png)
  - Profile/Change Profile Pages
  ![image](readme_images/profile.png)
  - My Orders Page/Order Details
  ![image](readme_images/my_orders.png)
  ![image](readme_images/order_detail.png) 
- Homepage:
  - Show all the products with pagination (6 items per page)
  ![image](readme_images/homepage.png)
- Product Page:
  - Show the details of individual product
  ![image](readme_images/product.png)
- Cart Page:
  - Show all the items in your shopping cart
  ![image](readme_images/cart.png)



# Reference:
- Python Django Tutorial. (https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- Advancing the Blog. (https://www.youtube.com/playlist?list=PLEsfXFp6DpzQB82YbmKKBy2jKdzpZKczn)
- Blog API with Django Rest Framework. (https://www.youtube.com/playlist?list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)