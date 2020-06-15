from socket import socket, AF_INET, SOCK_DGRAM
from requests import get
__name__ = 'pythonscriptgetip'
__author__ = 'Pranav Balaji Pooruli'
__email__ = 'pranav.pooruli@gmail.com'
__version__ = '0.0.1'


def private():
    _ = socket(AF_INET, SOCK_DGRAM)
    _.connect(('8.8.8.8', 8080))
    ip = _.getsockname()[0]
    return ip


def public():
    link = 'https://ipinfo.io/json'
    response = get(link, verify=True)
    if not response.status_code == 200:
        return 'UNAVAILABLE'
    data = response.json()
    return data['ip']
