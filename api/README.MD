## Events API

> Strongly recomended to use ```virtualenv```

## Instalation env (Linux)

1. Make sure you in /api directory 
2. ```virtualenv -p /usr/bin/python3.5 flenv``` (only if you didn't create yet)
3. Active virtualenv ```source ./flenv/bin/activate```
4. Install requrements ```pip3 install -r ./req.txt```
5. To run app make it executable ```chmod a+x app.py``` and run ```./add.py``` 


## API Description 

> current version ```v0.1```


```[GET] ${host}/api/${version}/events``` - show actual events (nev)

```[GET] ${host}/api/${version}/events/${id}``` - get event with id [NOT IMPLEMENTED]

```[PUT] ${host}/api/${version}/events``` - create or update event [NOT IMPLEMENTED]

```[DELETE] ${host}/api/${version}/events/${id}``` - delete event (actually only mark as not actual) [NOT IMPLEMENTED]

```[GET] ${host}/api/${version}/events/${id}/attendees``` - get attendees for event with id [NOT IMPLEMENTED]

```[PUT] ${host}/api/${version}/events/${id}/attendees``` - add or update attendee for event with id [NOT IMPLEMENTED]

```[DELETE] ${host}/api/${version}/events/${id}/attendees/${attendeeId}``` - delete attendy with attendeeId for event with id [NOT IMPLEMENTED]