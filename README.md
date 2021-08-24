# SurfAi Chatbot
<p align="center">
  <img src="wave.png">
</p>

A chatbot system that provides helpful data related to surfing conditions. The bot artificial inteligence knowledge base is built on top of [Google Dialogflow](https://dialogflow.com) and all the weather data is fetched from the [Stormglass API](https://stormglass.io).
[Google Dialogflow](https://dialogflow.com) can be used to train machine learning classifiers to be able to detect the intent of a given question and extract important 
entities from it (eg: location, weather parameter).


## Example interactions
`How is the weather in Costa da Caparica?`

`Tell me how's the wave height at Carcavelos.`

`Forecast for Guincho.`

`Air temperature at Carcavelos?`

## REST API
### Example request
```
curl --location --request POST 'http://127.0.0.1:8080/surf_bot/beach' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "Swell height at Guincho",
    "sender_id": "jose"
}'
```

### Example response
```
{
    "intent": "Specific Weather Parameters Intent",
    "text": "Swell height at Guincho",
    "response": "The swellHeight in Guincho will be:",
    "data": {
        "hours": [7, 8],
        "parameters": {
            "swellHeight": [1.05, [1.06](1.06)],
        }
    }
    "data": {
        "hours": [
            {
                "swellHeight": [
                    {
                        "source": "sg",
                        "value": 0.7
                    },
                    {
                        "source": "icon",
                        "value": 1.14
                    },
                    {
                        "source": "meteo",
                        "value": 0.7
                    }
                ],
                "time": "2021-08-22T07:00:00+00:00"
            },
        ....
        ],
    }
}
```

## Supported locations
### Portugal:
- Carcavelos 
- Costa da Caparica
- Guincho


## Setup
This project uses Python3.7 and the Flask Framework.

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
ACCESS_TOKEN="" - provided by Facebook

# Stormglass
STORMGLASS_URL="https://api.stormglass.io/v1/weather/point"
STORMGLASS_API_KEY=""

# Dialogflow
DIALOGFLOW_URL="https://api.dialogflow.com/v2/"
DIALOGFLOW_PROJECT_ID=""
DIALOGFLOW_CLIENT_ACCESS_TOKEN=""
GOOGLE_SERVICE_ACCOUNT_KEYS="" - path to JSON with GCP credentials
```

## Integration with Facebook Messenger

The API supports Facebook Messenger events so that the bot can be deployed in that platform.

For this, we have to follow the steps in the [Messenger Platform](https://developers.facebook.com/docs/messenger-platform/introduction) guide in order to create the Facebook Application and setup the webhook, pointing to `/messenger_webhook`.

The machine running the server has to have a valid SSL Certificate in order to be accepted by the Facebook Messenger API.
