## Events API

> Strongly recomended to use ```virtualenv```

## Instalation env (Linux)

1. Make sure you in /api directory 
2. ```virtualenv -p /usr/bin/python3.5 flenv``` (only if you didn't create yet)
3. Active virtualenv ```source ./flenv/bin/activate```
4. Install requrements ```pip3 install -r ./req.txt```
5. To run app make it executable ```chmod a+x app.py``` and run ```./add.py``` 

## DB

set environment variables: ```DB_URI``` and ```DB_NAME```

For Linux

```
export DB_URI=mongodb://username:password@mongohost:port/databasename

export DB_NAME=databasename

```

## API Description 

> current version ```v0.1```


```[GET] ${host}/api/${version}/events``` - show actual events

```[GET] ${host}/api/${version}/events/${id}``` - get event with id [NOT IMPLEMENTED]

```[PUT] ${host}/api/${version}/events``` - create or update event [NOT IMPLEMENTED]

```[DELETE] ${host}/api/${version}/events/${id}``` - delete event (actually only mark as not actual) [NOT IMPLEMENTED]

```[PUT] ${host}/api/${version}/events/${id}/attendees``` - add or update attendee for event with id [NOT IMPLEMENTED]

```[DELETE] ${host}/api/${version}/events/${id}/attendees/${attendeeId}``` - delete attendy with attendeeId for event with id [NOT IMPLEMENTED]

## Data format 

saved entities 

```
{
  '_id': 1,
  'title': 'New active Test Quiz',
  'description': 'Обычный квиз',
  'date': '06.03.2017 19:00',
  'location': 'Red pub',
  'attendees': [
    {
    'id': 1,
    'name': 'Igor Nesterenya',
    'notes': 'За понедельник.'
    },
    {
    'id': 2,
    'name': 'One More',
    'notes': '-'
    }
  ],
  'price':'5 BYN',
  'created': datetime.datetime.now(),
  'tags': ['bg'],
  'active': True
}
```

## Request examples

> app run on localhost:6910, version api **v0.1**

#### show actual events
```
curl -i http://localhost:6910/api/v0.1/events
```

```
HTTP/1.0 200 OK
Content-Type: application/json
Connection: close
Server: Werkzeug/0.12 Python/3.5.2
Date: Sat, 11 Mar 2017 20:35:30 GMT

...
```

#### insert/update

```
curl -i -H "Content-Type: application/json" -X PUT -d '{"price": "5 BYN", "tags": ["bg"], "description": "short info", "title": "Quiz", "date": "06.03",  "location": "pub"}' http://localhost:6910/api/v0.1/events

```

```
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.12 Python/3.5.2
Date: Sat, 11 Mar 2017 22:15:32 GMT

"58c47702fd8c2c7dcba0a272"
```