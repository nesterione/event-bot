from pymongo import MongoClient
import pymongo
import datetime

class DataService:

    def __init__(self, db):
        self.db = db

    def get_actual_events(self):
        result = self.db.events.find({'active':True}).sort("created", pymongo.DESCENDING)
        return result

    def upsert_event(self):
        pass

    def disable_event(self):
        pass

    def upsert_attendee(self):
        pass

    def remove_attendee(self):
        pass
