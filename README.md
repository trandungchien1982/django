# Django: The Web App framework for Python
-------------------------------------------------------------------------
Các ví dụ liên quan đến Django từ cơ bản đến nâng cao<br/>
Mỗi nhánh trong Repo sẽ là 1 ví dụ/ giải pháp/ project mẫu trong Django

# Môi trường phát triển
- Python 3.8.10
- Django 4.2.6 LTS
- SQLite3

# Cài đặt Django 4.2.6 LTS theo hướng dẫn
```shell
pip3 install Django==4.2.6
---------------------------------

```

# Start server
```shell
python3 manage.py runserver
```

# Access into HomePage
```shell
http://127.0.0.1:8000/
```

# Folder liên quan trên Windows
```
D:\Projects\django
```

==============================================================

# Ví dụ [03.RESTfulAPI]
==============================================================

**Ta sẽ tạo 1 App Django mẫu như sau:**<br/>
- Sử dụng Django REST framework
```shell
pip3 install djangorestframework
pip3 install markdown
pip3 install django-filter
```

- Tạo 1 app restful api bên trong project Django
```shell
python3 manage.py startapp restful01
python3 manage.py migrate
```

- Tiến hành migration data sau khi đã có models
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

- Các API hỗ trợ RESTful bao gồm GET, POST, PUT, DELETE


**Tham khảo**
- https://viblo.asia/p/gioi-thieu-django-rest-framework-Eb85oJb2l2G
- https://blog.logrocket.com/django-rest-framework-create-api/
- https://www.django-rest-framework.org/tutorial/quickstart/#quickstart


**Start Apps Django như bình thường & xem kết quả**<br/>
```shell
tdc@tdc:~/django/restful-api$ python3 manage.py runserver
```
- Ví dụ mẫu có sẵn trên trang chủ của Django REST framework, liên quan đến tương tác với table users ...
- Danh sách users

```shell
GET http://localhost:8000/users/
```
- Thêm user mới với username+email, password tự nhập vào trên CLI
```shell
python3 manage.py createsuperuser --email admin@example.com --username admin
```
- Update các user items bằng cách login vào user/pass: admin/admin và sau đó tương tác vào UI


