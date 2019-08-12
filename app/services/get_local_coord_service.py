from flask import current_app


class GetLocalCoordService():
    """
        Returns the coordinates of a specific supported location
    """

    def __init__(self, location):
        self.location = location

    def call(self) -> bool:
        
        for location in current_app.config.SUPPORTED_BEACHES:
            if location == self.location:
                return (location['latitude'], location['longitude'])

        return (None, None)
    