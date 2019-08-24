# Surf Forecast Bot

A Facebook Messenger Bot that informs the user of requested forecasts and notifies about perfect surfing conditions.

All the sea data is queried using the [Stormglass API](https://stormglass.io) which is open-source.

The bot currently supports forecast for the following beaches:
- Carcavelos 
- Costa da Caparica
- Guincho

This API integrates with [Google Dialogflow](https://dialogflow.com), which resourtes to Machine Learning algorithms to train the bot in order to understand
and learn what is spoken to him.

Queries can be done asking questions like:

`How is Costa da Caparica in 2 days?`

`Tell me how's wave height at Carcavelos tomorrow in the morning`

`Forecast for the next week on Guincho`

`How will the wind be at Carcavelos by the end of the day?`

## Setup

This project uses Python3.7 and the Flask Framework.

External services include **Google Dialogflow** and the **Stormglass API**.

Instaling all the dependencies and running the server:

```bash
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements
$ python3 manage.py runserver
```

Required environmental variables in `.env` file:
```
SECRET_KEY=" " - random
APP_ENV=" " - development|testing|production

# Facebook
VERIFY_TOKEN=" " - token used to verify app with Facebook (random)
ACCESS_TOKEN="" - rovided by Facebook

# Stormglass
STORMGLASS_URL="https://api.stormglass.io/v1/weather/point"
STORMGLASS_API_KEY=""

# Dialogflow
DIALOGFLOW_URL="https://api.dialogflow.com/v2/"
DIALOGFLOW_PROJECT_ID=""
DIALOGFLOW_CLIENT_ACCESS_TOKEN=""
GOOGLE_SERVICE_ACCOUNT_KEYS="" - path to JSON with GCP credentials
```

Finally you have to follow the steps in the [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/introduction) guide in order to create the Facebook Application and setup the webhook.

The server running the API has to have a valid SSL Certificate in order to be accepted by the Facebook Messenger API.
