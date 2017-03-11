# event-bot

Telegram bot for Events

## Project structure 

- ```api``` - contains REST API for whole functionality of events-platform 
- ```web-client``` - contains client app whick will open in browser 
- ```telegram-bot``` - client app, telegram bot application

## Project ideas

1. Telegram bot for watching events, vote and so on 
2. Web appliction for convinient configuration of events. (bot will use information from this site) 


It will be like event platfor first of all for us. 

                    DB 
                     |
            Flask app / REST API 
         |                        |
     simple web gui            Telegrab bot
    (maybe angular later)



## Run into Docker 

Each folder contains Dockerfile. Root folder contains docker-compose.yml.

You can run each container separately or all together. 

#### Install docker and docker-container 

* [Docker instalation](https://docs.docker.com/engine/installation) 
* [Docker-compose instalation](https://docs.docker.com/compose/install)

#### Run 

> Make sure you into root folder of project

to build containers locally use:

```
docker-compose build
```

to start apps 

```
docker-compose up
```

or if you want run it as background task 

```
docker-compose up -d
```

to stop and remove containers 

```
docker-compose stop
docker-compose rm
```

if you want to check container use following comands:

```
docker ps 
# to show stopped containers 
docker ps -a

# to show images
docker images
```
## Run withoud docker 

If you want run all withoud docker you need to install all dependencies 

* python3 (and all req.txt dependencies)

then you can run each application. for exampla ```/api/.app.py``` or ```python3 ./api/api.py```

## Contributing notes 

If you want to participate you can do it! 
