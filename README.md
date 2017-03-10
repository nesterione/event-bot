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



This should run in docker container 
