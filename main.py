import requests
import folium
from pyfiglet import Figlet


def get_info_by_ip(ip='127.0.0.1', map=False):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

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
    ip = input('Please enter a target IP: ')
    map = input('Do you want to save as map? (yes/no): ')
    map = map == 'yes'
    get_info_by_ip(ip, map)


if __name__ == '__main__':
    main()
