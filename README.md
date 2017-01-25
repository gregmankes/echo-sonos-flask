# echo-sonos-flask
Simple echo sonos controller using flask-ask and SoCo frameworks

Instructions

Clone repo
```
git clone https://github.com/gregmankes/echo-sonos-flask.git
```

Install `soco`
```
pip install soco --user
```

Install `flask-ask`
```
pip install flask-ask --user
```

Install [ngrok](http://ngrok.com)

Follow instructions [here](https://github.com/johnwheeler/flask-ask) and [here](https://youtu.be/cXL8FDUag-s?t=1m26s) to create the skill

Copy the following into intent schema:
```json
{
    "intents": [
        {
            "intent": "AMAZON.PauseIntent"
        },
        {
            "intent": "AMAZON.ResumeIntent"
        },
      	{
          	"intent": "AMAZON.NextIntent"
        },
      	{
          	"intent": "VolumeUpIntent"
        },
      	{
          	"intent": "VolumeDownIntent"
        },
      	{
          	"intent": "PlayIntent"
        },
      	{
          	"intent": "StopIntent"
        }
    ]
}
```

Copy the following into the sample utterances:
```
PlayIntent play
VolumeUpIntent volume up
VolumeDownIntent volume down
VolumeUpIntent turn up the jams
VolumeDownIntent pipe it down
StopIntent stop
```

Run the flask app
```
python controller.py
```

Run ngrok
```
ngrok http 5000
```
Copy the ngrok https url to global endpoint

PROFIT!!!

SIDE NOTES:
To interface with alexa, you would say:
```
Alexa, tell <skill_name> to <command_name>
```

You are only able to do basic control functions (this is really just so I can control pandora on sonos with voice). The available control functions thus far are:
* play
* pause (accessible with "stop" as well)
* next
* volume up (accessible with "pump up the jams" as well)
* volume down (accessible with "pipe it down" as well)

The computer that you are running this from must be on the same network as your sonos speakers. It will work if you are using a bridge or boost setup.

REFERENCE MATERIAL:

[SoCo UPnP Library](https://github.com/SoCo/SoCo)

[flask-ask python framework](https://github.com/johnwheeler/flask-ask)
