import urllib.request
import json

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/'

# tähän voisi listata pari esimerkki tägiä jsonista jotta käyttäjä pystyisi kirjoittamaan niitä.


def get_activities(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

# Fetch the tags from an activity


""" 
def user_input():
    usertags = input("Valitse yksi tägeistä: ").strip().lower()
    return usertags


def gettags(activities):
    return activities['tags']




# Fetch name of an activity.


def getname(act):
    return act['name']['fi']
 """

# Return activity['tags'] dictionaryn value arvot


def printtags(activities):
    return activities['tags'].values()

# Search activities['data'] with given input to find activities with matching tags


def searchtags(data, chosen):
    # loop every value in data
    for x in data:
        # loop every value in data['tags'] in x position/value
        for y in x['tags']:
            # if chosen(user input) value found inside, then print the activitys finnish name
            if chosen in y['name'].lower():
                print(x['name']['fi'])
                # if chosen found in tags, do not go through all tags (might give duplicates otherwise)
                break

# Get activities, print tags, save user input, print input for clarity, use funktion search


def searchtags_2():

    chosen = input(
        "Kirjoita valitsemasi tägit pilkulla eroteltuna: ").lower().strip()
    # Jos tägejä on useampi...
    # Muokataan annettua stringiä niin että sanojen väliin tulee %2C%20
    if ", " or "," in chosen:
        chosen = chosen.replace(", " or ",", "%2C%20")

    # Pläntätään stringi findtags="http://open-api.myhelsinki.fi/v1/activities/?tags_search=tähän"
    findtags = "http://open-api.myhelsinki.fi/v1/activities/?tags_search="+chosen

    foundactivities = get_activities(findtags)
    # for looppi jolla esitellään jotenkin järkevästi saatu data terminaalissa esimerkiksi foundactivities['data']['name']['fi'] näin alkuun
    # Vastaus tähän löytynee searchtags versio ykkösestä
    for x in foundactivities['data']:
        print(x['name']['fi'])
        # print(foundactivities['data']['name']['fi'])


def main():
    activities = get_activities(JSON_URL)
    print(printtags(activities))
    searchtags_2()
    """ chosen = input("Valitse yksi tägeistä: ").strip().lower()
    print("valitsit tägin: " + chosen)
    searchtags(activities['data'], chosen) """


""" def tools():
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
 """

if __name__ == '__main__':
    main()
