- #### Environmental Requirements

The database：mysql

Python Environment Requirements：

~~~shell
django
pymysql
pandas
Pillow
~~~

- #### Project Clone

~~~shell
git clone line
~~~

- #### Project Configuration

Setting.py file in the project

~~~python
DATABASES={
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"sale",
        "USER":"root",
        "PASSWORD":"password",  #Need to change your password information
        "PORT":3306,
        "HOST":"127.0.0.1"
    }
}
~~~

- #### Project Operation

Start the database first.

Then enter the terminal in turn

~~~shell
cd Project_name
python manage.py runserver
~~~

#### 

Administrator side：
http://47.251.43.118:8000/backstage/index/
account：n@163.com
Password：1

Main page:http://47.251.43.118:8000/
Account:xiaoming
Password:12

