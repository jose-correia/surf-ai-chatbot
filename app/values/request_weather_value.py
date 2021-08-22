from pydantic import BaseModel


class RequestWeatherValue(BaseModel):
    text: str
    sender_id: str = None

    @classmethod
    def from_messenger_event(cls, data: dict) -> "RequestWeatherValue":
        return cls(
            text=data['messaging'][0]['message']['text'],
            sender_id=data['messaging'][0]['sender']['id'],
        )
