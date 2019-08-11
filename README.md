# Surf Forecast Bot

A Facebook Messenger Bot that informs the user of requested forecasts and notifies about perfect surfing conditions.

All the sea data is queried using the [MagicSeaWeed API](https://pt.magicseaweed.com/developer/api) which is open-source.


## Setup

This project uses Python3.7

Instaling all the dependencies and running the server:

```bash
$ pipenv install
$ pipenv shell
$ python manage.py runserver
```

Required environmental variables:
````
SECRET_KEY=" " - random

APP_ENV=" " - development|testing|production

VERIFY_TOKEN=" " - random
ACCESS_TOKEN=" " - provided by Facebook
```

I recommend using a cloud service like Heroku to deploy the application.

After setting the link between the Heroku application, you have to follow the steps in the [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/introduction) guide in order to create the Facebook Application
