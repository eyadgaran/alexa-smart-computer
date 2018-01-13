from secrets import PRODUCTION_KEY, PRODUCTION_SECRET
from packaged_scripts.network.godaddy import GodaddyDomain
from packaged_scripts.network.ngrok import get_ngrok_tunnel

DOMAIN_NAME = 'yadgaran.net'
LOCALHOST_URL = 'localhost:2080'

RECORDS_TO_UPDATE = [
    {
        "type": "A",
        "name": "mymac.alexa",
        "ttl": 600
    }
]

if __name__ == '__main__':
    domain = GodaddyDomain(DOMAIN_NAME, PRODUCTION_KEY, PRODUCTION_SECRET)
    ngrok_url = get_ngrok_tunnel(LOCALHOST_URL)
    print ngrok_url
    # TODO: figure out godaddy forwarding api call
    # for record in RECORDS_TO_UPDATE:
    #     domain.update_record_details(
    #         record['type'],
    #         record['name'],
    #         record['ttl'],
    #         ngrok_url
    #     )
