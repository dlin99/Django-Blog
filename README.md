
# Django Blog With APT Endpoints Built With Django Rest Framework 
- Blog built with Django
- Blog API built with Django-Rest-Framework 
- Live Deployment: http://dyclin99.pythonanywhere.com/

## Tech & Tools:
- Python
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


## API Structure
In this application, we provide endpoints for users to access the blog posts and blog comments from using the HTTP methods - GET, POST, PUT, DELETE.

For blog post:
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`posts/` | GET | READ | Get all posts
`posts/:slug/` | GET | READ | Get a single post
`posts/create/`| POST | CREATE | Create a new post
`movies/:slug/update/` | PUT | UPDATE | Update a post
`movies/:slug/delete/` | DELETE | DELETE | Delete a post

For blog comment:
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`comments/` | GET | READ | Get all comments
`comments/:id/` | GET | READ | Get a single comment
`comments/create/`| POST | CREATE | Create a new comment
`comments/:id/` | PUT | UPDATE | Update a comment
`comments/:id/` | DELETE | DELETE | Delete a comment

## Use
We use [httpie](https://github.com/jakubroztocil/httpie#installation) to test the API (You can also use curl). 


First, we have to start up Django's development server.
```
  python manage.py runserver
```
Only authenticated users can use some of the API services (POST, PUT, DELETE), for that reason if we try this:
```
  http POST http://127.0.0.1:8000/api/comments/create/
```
we get:
```
  {
    "detail": "Authentication credentials were not provided."
  }
```
However, we can GET posts and comments without authentication:
```
  http http://127.0.0.1:8000/api/comments/63/
```
we get the comment with id = 63
```
{
    "author": {
        "email": "admin@example.com",
        "first_name": "",
        "last_name": "",
        "username": "admin"
    },
    "content": "children comment 2 - update",
    "content_object_url": "/api/posts/you-wont-believe-these-clickbait-titles/",
    "id": 63,
    "replies": null,
    "reply_count": 0,
    "timestamp": "2020-12-25T09:59:05.143859Z"
}
```

## Registration and Obtain Tokens

We first have to register a new account
```
  http POST http://127.0.0.1:8000/api/users/register/ username=user123 password=password123 email=user@example.com email2=user@example.com
```
To get a token by
```
  http POST http://127.0.0.1:8000/api/auth/token/ username=user123 password=password123
```
after that, we get the token
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywidXNlcm5hbWUiOiJ1c2VyMTIzIiwiZXhwIjoxNjA5MDM0NTkxLCJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20ifQ.CmQZHPkj6sbf3WwoRijehzhs0PQONZMY0nL85QU8Tzw"
}
```

The API has some restrictions:
-   The posts/comments are always associated with the user who created it.
-   Only authenticated users may create posts/comments.
-   Only the creator of a post/comment may update or delete it.
-   Unauthenticated user can only read the posts and comments.

### Commands

For post:
```
http POST http://127.0.0.1:8000/api/posts/create/ "Authorization: JWT <YOUR_TOKEN>" title="Your Title" content="Your content"
http http://127.0.0.1:8000/api/posts/:slug/
http PUT http://127.0.0.1:8000/api/posts/:slug/update/ "Authorization: JWT <YOUR_TOKEN>" title="Your Title - Updated" content="Your content - Updated"
http DELETE http://127.0.0.1:8000/api/posts/:slug/delete/ "Authorization: JWT <YOUR_TOKEN>"
```

For comments:
```
http POST http://127.0.0.1:8000/api/posts/create/ "Authorization: JWT <YOUR_TOKEN>" title="Your Title" content="Your content"
http http://127.0.0.1:8000/api/posts/:slug/
http PUT http://127.0.0.1:8000/api/posts/:slug/update/ "Authorization: JWT <YOUR_TOKEN>" title="Your Title - Updated" content="Your content - Updated"
http DELETE http://127.0.0.1:8000/api/posts/:slug/delete/ "Authorization: JWT <YOUR_TOKEN>"
```


### Functions:
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