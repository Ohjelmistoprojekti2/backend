import urllib.request
import json

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/' # ?limit=20

# tähän voisi listata pari esimerkki tägiä jsonista jotta käyttäjä pystyisi kirjoittamaan niitä.


def get_activities():
    with urllib.request.urlopen(JSON_URL) as response:
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
            if chosen in y['name']:
                print(x['name']['fi'])
                # if chosen found in tags, do not go through all tags (might give duplicates otherwise)
                break

# Get activities, print tags, save user input, print input for clarity, use funktion search


def main():
    activities = get_activities()
    print(printtags(activities))
    chosen = input("Valitse yksi tägeistä: ").strip().lower()
    print("valitsit tägin: " + chosen)
    searchtags(activities['data'], chosen)


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
