from pydantic import BaseModel


class ResponseValue(BaseModel):
    intent: str
    text: str
    response: str
    data: dict = {}
