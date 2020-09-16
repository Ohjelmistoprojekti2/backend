import urllib.request
import json

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/'

print("tägi1, tägi2, tägi3") #Lisätään oikeat tägit eri aihealueista myöhemmin.
usertags = input("Valitse yksi tägeistä: ").strip().upper() #tähän voisi listata pari esimerkki tägiä jsonista jotta käyttäjä pystyisi kirjoittamaan niitä.



def get_activities():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())

# Fetch the tags from an activity
def gettags(act):
    return act['tags']

# Fetch name of an activity.
def getname(act):
    return act['name']['fi']

def main():
    activities = get_activities()
    a_tags = activities['tags']
    activity_list = activities['data']

    if usertags in a_tags:
        print(activity_list[usertags].title())
    else:
        print('Tapahtumia ei löytynyt')

    for idx, act in enumerate(activity_list):
        for x in gettags(act):
            if usertags == gettags(act):
                print(getname(act))
                break
            print(x['name'])
        print("\n")


if __name__=='__main__':
    main()
