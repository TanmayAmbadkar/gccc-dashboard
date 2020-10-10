# Ranklist for 30 days of Cloud by google 

This project was designed to maintain a ranklist of students participating in the 30 days of cloud by Google. I am scraping the profiles collected for my institute and displaying the ranklist. I would like to add one more college just to test if the service breaks or still works. If anyone is interested, just drop an issue here saying you would like to add your college to the list. Make a csv file with the following columns: 

|Timestamp|Name|URL|
|---|---|---|
|xxxx|Name 1|public profile URL|
|xxxx|Name 2|public profile URL|


You can check out the deployed website [Here!](http://gccc-ranklist.tk)


# New Features!

  - Multiple college support
  - Removed the use of csv for scraping
  - Added animations and confetti to the ranklist [Go check it out!](http://gccc-ranklist.tk/iiitv/)

### Tech

gccc-dashboard uses the following:

* Django - as the backend for the services
* BeautifulSoup - For scraping the profile
* pandas - for working with the csv
* APScheduler - for scheduling tasks


### Installation

gccc-dashboard requires django 3.1.1 to run.

For linux users
```sh
$ git clone https://github.com/TanmayAmbadkar/gccc-dashboard.git
$ cd gccc-dashboard
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows users with conda
```sh
$ git clone https://github.com/TanmayAmbadkar/gccc-dashboard.git
$ cd gccc-dashboard
$ conda create -n myenv python=3.8
$ conda activate myenv
$ pip install -r requirements.txt
```

To test the app

First edit the apps.py file in the ranklist directory. Comment out the entire function *def ready()* and then run the following command

```sh
$ python manage.py makemigrations ranklist && python manage.py migrate
$ python manage.py createsuperuser
```
Now uncomment the previously commented function and run the following command
```sh
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.

If you want to deploy the app, you can use the following tutorial to deploy it on an AWS EC2 machine using apache - [tutorial](https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab) 


If you'd like to contribute, just make an issue and start working on it!
