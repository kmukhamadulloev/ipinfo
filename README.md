# IP info

IP address parser, using `ip-api.com` resource.

Dont forget to create virtual enviroment:
* Create: `python3 -m venv vevn`
* Use: `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`

How to use:
* Example: `python3 main.pu --ip 8.8.8.8`
* Example with map: `python3 main.pu --ip 8.8.8.8 --map`

Example:
* Input: `python3 main.pu --ip 45.45.45.45 --map`
```
    ________     _____   ____________ 
   /  _/ __ \   /  _/ | / / ____/ __ \
   / // /_/ /   / //  |/ / /_  / / / /
 _/ // ____/  _/ // /|  / __/ / /_/ / 
/___/_/      /___/_/ |_/_/    \____/  
                                      

[IP] : 45.45.45.45
[Provider] : Videotron Ltee
[Org] : Videotron Ltee
[Country] : Canada
[Region] : Quebec
[City] : Clerval
[Postal] : J0Z
[Timezone] : America/Toronto
[On map] : https://www.openstreetmap.org/#map=18/48.754/-79.4312
```
**Also it creates HTML file in maps folder**