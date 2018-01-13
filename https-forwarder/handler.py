# Skill enters here and gets routed appropriately
import logging
import requests
import secrets
import my_mac

FORMAT = "[%(asctime)s %(name)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    """
    Entry function of API Call
    event and context get passed and parsed appropriately
    :param event:
    :param context:
    :return:
    :rtype:
    """
    logger.debug(event)
    logger.debug(context)

    access_token = event['session']['user']['accessToken']
    logger.info("Token: {}".format(access_token))
    validate_access_token(access_token)

    application = event['session']['application']['applicationId']
    intent = parse_intent(event)

    # My Mac App
    if application == secrets.my_mac_app_id:
        return my_mac.forward_request(access_token, intent)


def validate_access_token(token):
    base_url = 'https://api.amazon.com/user/profile?access_token='
    profile = requests.get(base_url + token)

    profile_id = profile.json()['user_id']

    personal_profile = secrets.personal_alexa_profile

    if profile_id != personal_profile:
        logger.debug(profile.json())
        raise ValueError("Invalid Token")

    logger.info("User: {} ({}), Authenticated".format(
        profile.json()['name'], profile_id))


def parse_intent(event):
    intent_type = event['request']['type']

    # Launch request
    if intent_type == 'LaunchRequest':
        return 'launch'

    # Action Intents
    elif intent_type == 'IntentRequest':
        intent = event['request']['intent']['name']

        return intent

    # Other
    else:
        raise ValueError('Intent Not Supported')
