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

# Ví dụ [02.NavigateURLToApps]
==============================================================

**Ta sẽ tạo 1 App Django mẫu như sau:**<br/>
- Hiển thị trang HelloWorld khi truy cập vào 
```shell
http://localhost:8000
http://localhost:8000/polls
```
	- In ra lời chào thế giới
	- Chúc ngày mới vui vẻ :)

- Hiển thị trang mang sắc thái mùa xuân với urls:
```shell
http://localhost:8000/spring
http://localhost:8000/spring/list
```

- Hiển thị trang mang sắc thái mùa hè với urls:
```shell
http://localhost:8000/summer
http://localhost:8000/summer/list
```

- Hiển thị trang mang sắc thái mùa thu với urls:
```shell
http://localhost:8000/autumn
http://localhost:8000/autumn/list
```

- Hiển thị trang mang sắc thái mùa đông với urls:
```shell
http://localhost:8000/winter
http://localhost:8000/winter/list
```


**Tham khảo**
- https://viblo.asia/p/tim-hieu-ve-django-framework-ho-tro-python-trong-lap-trinh-web-QpmlexbkZrd
- https://medium.com/@doanhtu/l%C3%A0m-sao-%C4%91%E1%BB%83-t%E1%BA%A1o-1-trang-web-v%E1%BB%9Bi-django-i-fddff91786f7

**Tạo 4 apps mang các sắc thái khác nhau (Python packages)**
```shell
tdc@tdc:~/django/navigate_urls$
-------------------------------------------------
python3 manage.py startapp spring
python3 manage.py startapp summer
python3 manage.py startapp autumn
python3 manage.py startapp winter
```

**Định vị URLs đến các components UI cần thiết được mô tả như sau**
```shell
main_site/settings.py
	ROOT_URLCONF = 'main_site.urls'

main_site/urls.py
# Urls trỏ đến 4 seasons khác nhau ...
    path('spring/', include('spring.urls')),
    path('summer/', include('summer.urls')),
    path('autumn/', include('autumn.urls')),
    path('winter/', include('winter.urls')),
	
spring/urls.py
	urlpatterns = [
		path('', views.index, name='index'),
		path('list', views.listInSpring, name='listInSpring'),
	]

summer/urls.py
	urlpatterns = [
		path('', views.index, name='index'),
		path('list', views.listInSummer, name='listInSummer'),
	]

autumn/urls.py
	urlpatterns = [
    	path('', views.index, name='index'),
    	path('list', views.listInAutumn, name='listInAutumn'),
	]

winter/urls.py
	urlpatterns = [
		path('', views.index, name='index'),
		path('list', views.listInWinter, name='listInWinter'),
	]
```

**Kết quả thực thi**<br/>
```shell
tdc@tdc:~/django/navigate_urls$ python3 manage.py runserver
```

**Truy cập trang chủ**
```shell
http://localhost:8000/
```