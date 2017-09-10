'''Forwarding Rules for My Mac Skill'''

import requests


def forward_request(access_token, intent):
    base_url = 'http://mymac.alexa.yadgaran.net'
    intent_route = intent_router(intent)

    return requests.get(base_url + intent_route,
                        params={'access_token': access_token}).json()


def intent_router(intent):
    intent_map = {
        'launch': '/',
        'Play': '/play',
        'Pause': '/pause',
        'Mute': '/mute',
        'Unmute': '/unmute',
        'VolumeDown': '/volumedown',
        'VolumeUp': '/volumeup',
        'Snooze': '/snooze'
    }

    return intent_map[intent]
