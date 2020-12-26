# E-Commerce-Website 
- Blog built with Django
- Blog API built with Django-Rest-Framework
- Deploy on Pythonanywhere 
- Live Deployment: http://dyclin99.pythonanywhere.com/


# Tech & Tools:
1. Django
2. Django REST framework
3. Django REST framework JWT

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

# To use:
1. git clone this repository to your computer
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. run http://localhost:8000/


# Reference:
- Python Django Tutorial. (https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- Advancing the Blog. (https://www.youtube.com/playlist?list=PLEsfXFp6DpzQB82YbmKKBy2jKdzpZKczn)
- Blog API with Django Rest Framework. (https://www.youtube.com/playlist?list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)