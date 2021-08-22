from flask import current_app as app


class BaseException(Exception):
    error_message = ""
    details = {}

    def to_dict(self) -> dict:
        return {
            "error_message": self.error_message,
            "details": self.details,
        }


class WeatherAPIError(BaseException):
    error_message = "Failed to request weather data to the StormGlass API"
    details = {}


class LocationNotFoundError(BaseException):
    error_message = "Location requested is not supported"
    details = {
        "supported_locations": app.config.get("SUPPORTED_LOCATIONS"),
    }
