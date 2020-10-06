# gccc-dashboard

This project is very much in beta right now. It basically scrapes data from qwiklabs every 20 minutes, and updates the ranklist. It should work for multiple colleges.


# New Features!

  - multicollege support

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

```sh
$ python manage.py makemigration && python manage.py migrate
$ python manage.py runserver
```

If you want to deploy the app, you can use the following tutorial to deploy it on an AWS server using apache - [tutorial](https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab)

If you'd like to contribute, just make an issue and start working on it!
