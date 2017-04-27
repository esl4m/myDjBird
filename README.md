# DjBird -- Django Bird
Hello ..
<br/>
 DjBird is a simple Python-Django project. works on Python 2.7.6 and Django 1.8
<br/>
 You can create new account and start following other people. You have a simple timeline showing your username and your profile picture.<br/>
Also you can see numbers of tweets, followers and following.<br/>
You can show your tweet and you can delete it, Also you can like, dislike and reply on your tweet and other tweets.
If this tweet has replies, it will be shown under it.<br/>
You can see list of users profiles and you can follow / unfollow them. Also if you clicked on any profile, you can see their info and updates.
<br/><br/>
This is still a beta version , so don't be sad if you see some bugs :D
<br/><br/>
And it will be great if you want to send me your comments on my email : me@esl4m.com
<br/><br/>
Thank you for your time and enjoy using DjBird :) 
<br/><br/>
* On your workspace create new folder djbird and in this folder create a new env<br/>
```
$ virtualenv env
```
* Then activate it :
```
$ source env/bin/activate
```
* Install requirements .. just run
```
$ pip install -r requirements.txt    # (to install all requirements)
```

* Clone latest version
```
$ git clone https://github.com/esl4m/myDjBird.git
```

* Create mysql Database :
<br/>
from terminal login to mysql 
```
$ mysql --user=root --password=root
```
then create your database 
```
$ create database dj_bird ;
```
* Then :
```
$ python manage.py syncdb
```
(add the django admin user if you want)
<br/>
or add it from here :
```
python manage.py createsuperuser
```
* Run server :
```
$ python manage.py runserver 
```
<br/>
To access the application .. type on your browser 
```
$ 127.0.0.1:8000/myDjBird_app/
```
<br/><br/>
Thank you for your time and enjoy using DjBird :)
<br/><br/>

* Future work :
.. In web version :<br/>
Add the timeline tweets.<br/>
.. In Mobile version :<br/>
..

