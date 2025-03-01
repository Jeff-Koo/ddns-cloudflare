import os
import requests
from cloudflare import Cloudflare
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Configuration
ZONE_ID = os.getenv('ZONE_ID')
CLOUDFLARE_EMAIL = os.getenv('CLOUDFLARE_EMAIL')
CLOUDFLARE_API_KEY = os.getenv('CLOUDFLARE_API_KEY')

print(CLOUDFLARE_EMAIL)

client = Cloudflare(
    api_email=CLOUDFLARE_EMAIL,
    api_key=CLOUDFLARE_API_KEY, 
)


def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


def get_dns_records():
    pages = client.dns.records.list(zone_id=ZONE_ID)
    page = pages.result[0]
    print(page)
    return 


def update_dns_record(record_id, ip):
    record_response = client.dns.records.update(
        zone_id=ZONE_ID,
        dns_record_id=record_id,
        content=ip
    )
    print(record_response)


def main():
    current_ip = get_public_ip()
    print(f'Current public IP: {current_ip}')

    dns_records = get_dns_records()
    print(dns_records)
    record_id = None

    for record in dns_records:
        record_id = record['id']
        if record['content'] != current_ip:
            print(f'IP has changed from {record["content"]} to {current_ip}. Updating DNS record...')
            # update_dns_record(record_id, current_ip)
        else:
            print('IP has not changed. No update needed.')

    if record_id is None:
        print('DNS record not found.')


if __name__ == '__main__':
    main()
