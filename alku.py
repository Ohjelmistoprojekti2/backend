import urllib.request
import json

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/'

def get_activities():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())

def main():
    activities = get_activities()
    a_tags = activities['tags']

if __name__=='__main__':
    main()
