from packaged_scripts.system.keyboard import SPECIAL_KEYMAP, VirtualKeyboard
from flask import request
from flask_ask import statement, question
from threading import Thread
import time

from app import app
from auth import validate_access_token

KEYBOARD = VirtualKeyboard()


# Authentication
@app.before_request
def auth_validation():
    access_token = request.args.get('access_token')
    validate_access_token(access_token)


# @ask.launch
@app.route('/')
def start_skill():
    welcome_message = 'Hello, what would you like to do?'
    return question(welcome_message).render_response()


# @ask.intent("Play")
@app.route('/play/')
def play(response=True):
    key = SPECIAL_KEYMAP['play_pause']
    KEYBOARD.tap_key(key)
    if response:
        return statement('ok').render_response()


# @ask.intent("Pause")
@app.route('/pause/')
def pause(response=True):
    key = SPECIAL_KEYMAP['play_pause']
    KEYBOARD.tap_key(key)
    if response:
        return statement('ok').render_response()


# @ask.intent("Mute")
@app.route('/mute/')
def mute():
    key = SPECIAL_KEYMAP['mute']
    KEYBOARD.tap_key(key)
    return statement('ok').render_response()


# @ask.intent("Unmute")
@app.route('/unmute/')
def unmute():
    key = SPECIAL_KEYMAP['mute']
    KEYBOARD.tap_key(key)
    return statement('ok').render_response()


# @ask.intent("VolumeUp")
@app.route('/volumeup/')
def volumeup():
    key = SPECIAL_KEYMAP['sound_up']
    KEYBOARD.tap_key(key)
    return statement('ok').render_response()


# @ask.intent("VolumeDown")
@app.route('/volumedown/')
def volumedown():
    key = SPECIAL_KEYMAP['sound_down']
    KEYBOARD.tap_key(key)
    return statement('ok').render_response()


# @ask.intent("Snooze")
@app.route('/snooze/')
def snooze():
    def snoozer():
        pause(response=False)
        time.sleep(60 * 10)
        play(response=False)

    threads = [Thread(target=snoozer)]
    [t.start() for t in threads]

    return statement('snoozing').render_response()
