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

PROFIT!!!
