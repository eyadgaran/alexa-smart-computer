'''Functions to Interface with Authentication'''

import requests
from secrets import personal_alexa_profile
from app import app


def validate_access_token(token):
    base_url = 'https://api.amazon.com/user/profile?access_token='
    profile = requests.get(base_url + token)
    app.logger.debug('hello')

    profile_id = profile.json()['user_id']

    if profile_id != personal_alexa_profile:
        app.logger.debug(profile.json())
        raise ValueError("Invalid Token")

    app.logger.info("User: {} ({}), Authenticated".format(
        profile.json()['name'], profile_id))
