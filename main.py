import requests
import folium
import argparse
from pyfiglet import Figlet


def get_info_by_ip(ip='127.0.0.1', map=False):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Provider]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Postal]': response.get('zip'),
            '[Timezone]': response.get('timezone'),
            '[On map]': f'https://www.openstreetmap.org/#map=18/{response.get("lat")}/{response.get("lon")}',
        }

        for key, value in data.items():
            print(f'{key} : {value}')

        if map:
            area = folium.Map(
                location=[response.get("lat"), response.get("lon")])
            area.save(f'./maps/{response.get("query")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))

    parser = argparse.ArgumentParser(
        description='Get IP information and optionally save as map.')
    parser.add_argument('--ip', help='Target IP address')
    parser.add_argument('--map', action='store_true',
                        help='Save as map (no value needed)')
    args = parser.parse_args()

    ip = args.ip or help()
    map = args.map

    get_info_by_ip(ip, map)


def help():
    print('[!] No IP provided!')
    print('[?] Example: python3 main.py --ip 8.8.8.8')
    print('[?] Example with map: python3 main.py --ip 8.8.8.8 --map')
    exit()


if __name__ == '__main__':
    main()
