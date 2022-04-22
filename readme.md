# GooseCity
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

- #### The Alipay has been deployed and fully functional, but Please <u>**Don't Scan The QR Code**</u> to prevent the Economic Disputes.

- #### The credit card System is working, but don't stroe any real information in this site.

- #### Test account 
       website Login account :1
               Password: 1
       
       http://47.251.43.118:8000/backstage/
        Administrator Backstage:
               Account:n@163.com
               Password:1
       
      Also, when you going to test you also can create and add your own account both of  website and Administrator.

- #### If your data visualization on the admin web page has adaptation problems，Please close the small window adjacent to him, such as the product list, and refresh. he will be back to normal.

