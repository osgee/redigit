# Introduction

This project aims at solving the problem of handwriting digits recognition.
Actaully, this is teamwork project, including several students as following:

        Fengtao, Wangwenbing, Yanghuan, Marui. 
    
And, this is for the Analysis and Programming Course, which is directed by Professor Jiang and Professor Yang.
We dicide to use python to handle the hard work!

# Environment

        The operating system is Ubuntu
        Python version is 2.7
        Django version is 1.7

# Dependencies

        django  numpy  scipy  nolearn  pandas  PIL

# Commands to configure dependency

        $ sudo apt-get update
        $ sudo apt-get install python-pip
        $ sudo pip install numpy scipy nolearn pandas
        $ sudo apt-get install libpng-dev libjpeg8-dev libfreetype6-dev 
        $ sudo pip install matplotli
        $ sudo pip install PIL
    
# Usages

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

        $ python manage.py syncdb

2) Run Django

        $ python manage.py runserver $IP:$PORT
    
# Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide

PS: Thanks for Cloud9's kind support!