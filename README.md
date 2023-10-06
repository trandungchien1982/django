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

# Ví dụ [01.HelloWorld]
==============================================================

**Ta sẽ tạo 1 App Django mẫu như sau:**<br/>
- Hiển thị trang HelloWorld khi truy cập vào 
```shell
http://127.0.0.1:8000
http://127.0.0.1:8000/polls
```
	- In ra lời chào thế giới
	- Chúc ngày mới vui vẻ :)

- Hiển thị trang Login Admin khi truy cập vào
```shell
http://127.0.0.1:8000/admin
```

**Tham khảo**
- https://viblo.asia/p/tim-hieu-ve-django-framework-ho-tro-python-trong-lap-trinh-web-QpmlexbkZrd
- https://medium.com/@doanhtu/l%C3%A0m-sao-%C4%91%E1%BB%83-t%E1%BA%A1o-1-trang-web-v%E1%BB%9Bi-django-i-fddff91786f7

**Tạo 1 Poll app (Python package)**
```shell
python3 manage.py startapp polls
```

**Kết quả thực thi**<br/>
```shell
tdc@tdc:~/django/hello_world$ python3 manage.py runserver
```

**Truy cập trang chủ**
```shell
http://127.0.0.1:8000/
```