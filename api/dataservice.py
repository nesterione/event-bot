from bson import ObjectId
import pymongo
import datetime


class DataService:
    def __init__(self, db):
        self.db = db

    def get_actual_events(self):
        result = self.db.events.find({'active': True}).sort("created", pymongo.DESCENDING)
        return result

    def get_event(self, event_id):
        return self.db.events.find_one({'_id': ObjectId(event_id)})

    def upsert_event(self, json):


        if '_id' in json:
            event = self.db.events.find_one({'_id': ObjectId(json['_id'])})
        else:
            event = {
                'title': '',
                'description': '',
                'date': '',
                'location': '',
                'attendees': [],
                'price': '',
                'created': datetime.datetime.now(),
                'tags': [],
                'active': True
            }

        if 'title' in json:
            event['title'] = json['title']
        if 'description' in json:
            event['description'] = json['description']
        if 'date' in json:
            event['date'] = json['date']

        if 'attendees' in json:
            unique = {}

            for attendee in event['attendees']:
                unique[attendee['id']] = attendee
            for attendee in json['attendees']:
                unique[attendee['id']] = attendee

            merged = []
            for k in unique.keys():
                merged.append(unique[k])

            event['attendees'] = merged

        if 'location' in json:
            event['location'] = json['location']
        if 'price' in json:
            event['price'] = json['price']

        if 'tags' in json:
            unique = set(event['tags'])
            unique.add(*json['tags'])
            event['tags'] = list(unique)

        if '_id' not in event:
            result = self.db.events.insert_one(event).inserted_id
        else:
            result = self.db.events.replace_one({'_id': event['_id']}, event, upsert=True).upserted_id

        return result

    def disable_event(self, event_id):
        self.db.events.update_one({'_id': ObjectId(event_id)}, {'$set': {'active': False}})


    def upsert_attendee(self):
        pass

    def remove_attendee(self):
        pass
