from app import app
from flask import json
import requests

# Testataan että /app/activities on olemassa
def test_get_activities():
    print("------------------------ Next: test_get_activities")
    x = requests.get('http://127.0.0.1:5000/app/activities')

    # Checking that we get a working site.
    print('Id of first activity:', x.json()['activities'][1]['id'])
    assert x.status_code == 200

    # Checking that we have activities by checking activities list length
    print('Number of activities found:', len(x.json()['activities']))
    assert len(x.json()['activities']) != 0

# Testataan että /app/tags on olemassa
def test_get_tags():
    print("------------------------ Next: test_get_tags")
    x = requests.get('http://127.0.0.1:5000/app/tags')

    # Checking that we get a working site.
    assert x.status_code == 200

    # Checking that the list which contains the tags isn't empty.
    print(len(x.json()['tags']), 'tags found')
    assert len(x.json()['tags']) != 0

    # Checking that one of the tags I know exists is in the list.
    print('Tag sauna is at index', x.json()['tags'].index('sauna'))
    assert 'sauna' in x.json()['tags']

# Testataan että /app/activities/search on olemassa käyttäen tagia 'sauna'
def test_get_search():
    print("------------------------ Next: test_get_search")   
    x = requests.get('http://127.0.0.1:5000/app/activities/search?tags=sauna')

    # Checking that we get a working site.
    assert x.status_code == 200
    print('Id of first activity:', x.json()['data'][1]['id'])

    """
    Here we will construct a list containing boolean values, one boolean for each activity.
    
    If the activity contains the tag 'sauna', the boolean is true.
    If the activity does not contain the tag 'sauna', the boolean is false.

    We will assert that every value in the list is true, because every activity
    in this list should have the tag 'Sauna'
    """

    lilbool = False
    biglist = []

    # Loop through every activity in x['data']
    for I1 in x.json()['data']:
        # Loop every value in x['data']['tags'] in I1 position/value
        for I2 in I1['tags']:
            # If tag 'sauna' found inside, then set lilbool to true
            if 'sauna' in I2['name']:
                lilbool = True
                break
        # Append the value of lilbool to biglist and reset lilbool to false
        biglist.append(lilbool)
        lilbool = False
    
    # Checking that every boolean in biglist is now true.
    # Because every activity should have the 'sauna' tag.
    print('Values in biglist:', biglist)
    assert all(biglist) is True

def test_get_search_mumbojumbo():
    print("------------------------ Next: test_get_search_mumbojumbo")
    x = requests.get('http://127.0.0.1:5000/app/activities/search?tags=dakkavore')

    # It still returns a working website for me to look at.
    # It just will not have data.
    assert x.status_code == 200
    try:
        print('ID of first activity:', len(x.json()['data'][1]['id']))
    except IndexError:
        print('Here I would have attempted to print the ID of the first activity, but I found none.')
    except:
        print('There came an error in printing ID of first activity, but not the one I expected.')

    lilbool = False
    biglist = []

    for I1 in x.json()['data']:
        # loop every value in data['tags'] in I1 position/value
        for I2 in I1['tags']:
            # if 'dakkavore' found inside, then set lil bool to true
            if 'dakkavore' in I2['name']:
                lilbool = True
                break
        biglist.append(lilbool)
        lilbool = False
    
    # The list ought to be empty because I am sure that there is not 'dakkavore' tag.
    print('Values in biglist:', biglist)
    assert len(biglist) == 0

# Testing a post method that goes into postman-echo. (It echos back the same stuff)
# This is simply meant for me to learn to test a post method, since there isn't
# any post stuff in the original app.py that I am primarily testing.
def test_post_pizza():
    print("------------------------ Next: test_post_pizza")
    url = 'http://127.0.0.1:5000/pizza/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {
        "name": "True Meatlovers Pizza",
        "ingredients": [
            "Sauteed Reindeer", "Bacon", "Ham",
            "Kebab", "Salami", "Pepperoni"
            ]
    }
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))   

    # print response full body as text
    print(resp.text) 
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201
    assert "id" in resp.text
    assert "ingredients" in resp.text
    assert "name" in resp.text
    
def test_post_pizza_bad():
    print("------------------------ Next: test_post_pizza_bad")
    url = 'http://127.0.0.1:5000/pizza/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {
        "ingredients": [
            "Eekum", "bookum"
            ]
    }
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))   

    # print response full body as text
    print(resp.text) 
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 400
    