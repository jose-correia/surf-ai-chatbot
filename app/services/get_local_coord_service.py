from flask import current_app as app
from typing import Tuple
import logging
from app.values.errors import LocationNotFoundError


logger = logging.getLogger()


class GetLocalCoordService():
    """
        Returns the coordinates of a specific supported location
    """

    def __init__(self, location: str):
        self.location = location

    def call(self) -> Tuple[str, str]:

        location_data = app.config.get("SUPPORTED_LOCATIONS").get(self.location)

        if not location_data:
            logger.error("Requested location that is not configured! {}".format(self.location))
            raise LocationNotFoundError()

        return (location_data['latitude'], location_data['longitude'])
