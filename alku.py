import urllib.request
import json

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/'

usertags = raw_input("Kirjoita mielenkiinnonkohteesi: ").strip().upper() #tähän voisi listata pari esimerkki tägiä jsonista jotta käyttäjä pystyisi kirjoittamaan niitä.


def get_activities():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())

def main():
    activities = get_activities()
    a_tags = activities['tags']

    if usertags in a_tags:
        print(activities[usertags].title())
    else:
        print('Tapahtumia ei löytynyt')

if __name__=='__main__':
    main()
