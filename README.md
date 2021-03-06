# Welcome to NeonCart Medical Store which is build by the GooseCity team

Here is a video that our team has recorded for you, in which we carefully introduce the features of our website, the story behind it and, most importantly, the demonstration of its functionality.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CMCEIkYGrOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<h1>User Guide</h1>
<section>
<h2> User Interface</h2>
<p> Welcome to NeonCart Medical Store, an online medical shopping center dedicated to the convenience of people</p>
 <p>Please vist our shop by click <a href="http://47.251.43.118:8000.com">NeonCart Medical Store</a>
 <p> When users visit our domain, they will be asked to log in, and the login operation is shown below</p>
  
  <img width="1870" alt="Login" src="https://user-images.githubusercontent.com/57980036/164515933-ac78e55b-f5ef-480e-8842-a96dadd744ce.png">
  
  <img width="1872" alt="Register" src="https://user-images.githubusercontent.com/57980036/164521096-da350653-1fe0-405a-9849-5cb1dbfb94a3.png">
  
  <p>Once you have successfully logged in, you will be greeted with a very simple and straightforward interface, to make a purchase, please complete your personal information and payment address first (as shown below) so that we can complete your payment process more efficiently </p>
  
 <img width="878" alt="personalInfo" src="https://user-images.githubusercontent.com/57980036/164547341-4d565133-9714-48f6-8432-67b56888435e.png">
 <img width="921" alt="personal info" src="https://user-images.githubusercontent.com/57980036/164547367-7ab1c299-9e58-4799-af71-513c433ee049.png">
 <p>After completing your information, you can use our website to shop as much as you like!</p>
<br>
<br>
<section>

<h2> Administrator Interface</h2>
<h2><p>Welcome to be the administrator of this website</p></h2>
<p>As the administrator of this website, please always keep the following principles in mind</p>
 1.<b>Please do not disclose your login information to others</b><br>
 2.<b>Please note that you should not disclose any user information to any individual, group, or organization</b><br>
 3.<b>Administrator accounts can only be used to log into the administrator interface, please do not try to use the same username and password to log into the user interface</b>
 <br>

 <p>In our admin system, you can add or delete products, general user information, and add new admins, as you can see, you have a lot of power, so by all means, <b>Be Sure To Keep Your Account Safe!</b></p>
<p>When you have successfully logged in and entered the administrator screen, your site should look like the following.</p>
 <img width="1870" alt="admin" src="https://user-images.githubusercontent.com/57980036/164567539-3ba0aa35-446d-4e43-8275-63d200ca179e.png"><br>
 <p>In the center of the screen are the bar chart and pie chart of our data visualization</p>
 <p>Some administrators have reported problems with misaligned numbers when opening web pages, if you encounter this problem please close all small windows and refresh the web page</p>
</section>
 <br>
 
- ### Environmental Requirements

The database???mysql

Python Environment Requirements???

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

- ### Project Operation

Start the database first.

Then enter the terminal in turn

~~~shell
cd Project_name
python manage.py runserver
~~~

- #### The Alipay has been deployed and fully functional, but Please <u>**Don't Scan The QR Code**</u> to prevent the Economic Disputes.

- #### The credit card System is working, but don't stroe any real information in this site.

- ### Test account 
-      47.251.43.118:8000/
       website Login account :1
               Password: 1
       
       http://47.251.43.118:8000/backstage/
        Administrator Backstage:
               Account:n@163.com
               Password:1
       
      Also, when you going to test you also can create and add your own account both of  website and Administrator.
- ## Test Operation
- #### The Test file is located at GooseCity/test.py
- ####  Requirements

~~~shell
requests
json
time
lxml
~~~



#### Implementation principle

Use Python's crawler technology to simulate user registration, login and other operations on the website to judge whether the returned data is abnormal.

#### Operation mode

~~~python
python test.py
~~~

#### Website return value description

- Examples

~~~text
200-the server successfully returned to the web page
404-the requested page does not exist
503-server timeout
~~~
 <br>

<summary><h2> About </h2>
-Chenhao Cui <a href="https://www.linkedin.com/in/chenhao-cui-6a43981a2">LinkedIn</a><br>
-Hayden Bunce <a href="https://www.linkedin.com/in/hayden-bunce-1b94b4238/">LinkedIn</a><br>
-Logan Etheredge <a href="https://www.linkedin.com/in/logan-etheredge-001576238">LinkedIn</a><br>
-Weihang He <a href="https://www.linkedin.com/in/weihang-he-86b570238/">LinkedIn</a>
