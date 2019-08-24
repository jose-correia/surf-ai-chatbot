from datetime import datetime, timedelta


class EntityTimestampConverter(object):

    def __init__(self):
    
        self.current_time = datetime.now()

        self.TIME_INTERVALS = {
            'now': {
                'start': self.current_time.hour,
                'end': self.current_time.hour
            },
            'morning': {
                'start': 7,
                'end': 11
            },
            'midday': {
                'start': 11,
                'end': 13
            },
            'afternoon': {
                'start': 15,
                'end': 18
            }
            'all day': {
                'start': 7,
                'end': 18
            }
        }

        self.DATETIMES = {
            'today': {
                'start': self.current_time.today(),
                'end': self.current_time.today()
            },
            'tomorrow': {
                'start': (self.current_time.today() + timedelta(days=1)).replace(hour=7, minute=0),
                'end': (self.current_time.today() + timedelta(days=1)).replace(hour=18, minute=0)
            },
            'in 2 days': {
                'start': (self.current_time.today() + timedelta(days=2)).replace(hour=7, minute=0),
                'end': (self.current_time.today() + timedelta(days=2)).replace(hour=7, minute=0)
            },
            'this week': {
                'start': self.current_time.today(),
                'end': (self.current_time.today() + timedelta(days=6-self.current_time.weekday())).replace(hour=18, minute=0)
            },
            'next week': {
                'start': (self.current_time.today() + timedelta(days=7-self.current_time.weekday())).replace(hour=7, minute=0),
                'end': (self.current_time.today() + timedelta(days=13-self.current_time.weekday())).replace(hour=18, minute=0)
            },
        }

    def get_start_timestamp(self, date_entity, time_entity):
        
        if date_entity in self.DATETIMES:
            start_date = self.DATETIMES[date_entity]['start']

            if time_entity in self.TIME_INTERVALS:
                start_time = self.TIME_INTERVALS[time_entity]['start']

                start_datetime = start_date.replace(hour=start_time)
                return start_datetime
            return start_date
        return None

    def get_end_timestamp(self, date_entity, time_entity):
        
        if date_entity in self.DATETIMES:
            end_date = self.DATETIMES[date_entity]['end']

            if time_entity in self.TIME_INTERVALS:
                end_time = self.TIME_INTERVALS[time_entity]['end']

                end_datetime = end_date.replace(hour=end_time)
                return end_datetime
            return end_date
        return None
