import logging
from flask import Flask
from flask_ask import Ask, statement,  session
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
import soco

devices = []
VOLUME_CHANGE = 10

def setup(internal_counter=0):
    kill()
    internal_counter += 1
    for zone in soco.discover():
        devices.append(zone)
    if ((len(devices) < 1) and internal_counter < 5):
        setup(internal_counter)

@ask.intent('AMAZON.ResumeIntent')
def resume():
    for zone in devices:
        if zone.is_coordinator:
            zone.play()
    return statement("Resuming Music")

@ask.intent("PlayIntent")
def play():
    resume()
    return statement("Playing Music")

@ask.intent("AMAZON.PauseIntent")
def pause():
    for zone in devices:
        if zone.is_coordinator:
            zone.pause()
    return statement("Pausing Music")

@ask.intent("StopIntent")
def stop():
    return pause()

@ask.intent("AMAZON.NextIntent")
def next():
    for zone in devices:
        if zone.is_coordinator:
            zone.next()
    return statement("")

@ask.intent("VolumeUpIntent")
def volume_up():
    for zone in devices:
        zone.volume += VOLUME_CHANGE
    return statement("")

@ask.intent("VolumeDownIntent")
def volume_down():
    for zone in devices:
        zone.volume -= VOLUME_CHANGE
    return statement("")

def kill():
    for item in devices:
        del item

if __name__ == '__main__':
    setup()
    app.run(debug=True)
