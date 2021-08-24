from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


ACCEPTED_SOURCES = ["sg", "icon", "meteo"]


class ParameterValue(BaseModel):
    name: str
    values: Optional[List[float]] = []


class WeatherDataValue(BaseModel):
    hours: List[int]
    parameters: List[ParameterValue]

    @classmethod
    def from_stormglass_response(cls, data: dict) -> "WeatherDataValue":
        hours = []
        parameters = {}

        for hour_data in data.get("hours"):
            for key, value in hour_data.items():
                if key == "time":
                    hour = WeatherDataValue._get_hour_from_time(value)
                    hours.append(hour)

                else:
                    source_value = None
                    for source in value:
                        data_value = source.get("value")
                        source_value = data_value
                        if source.get("source") in ACCEPTED_SOURCES:
                            source_value = data_value
                            break

                    parameter = parameters.get(key)
                    if not parameter:
                        parameter = ParameterValue(name=key)
                        parameters[key] = parameter

                    parameter.values.append(source_value)

        final_parameters_list = []
        for key, value in parameters.items():
            final_parameters_list.append(value)

        return cls(
            hours=hours,
            parameters=final_parameters_list,
        )

    @staticmethod
    def _get_hour_from_time(time: str) -> int:
        time_obj = datetime.fromisoformat(time)
        return int(time_obj.hour)
