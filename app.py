#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request
import urllib.request
import json

app = Flask(__name__)

JSON_URL = 'http://open-api.myhelsinki.fi/v1/activities/' # ?limit=20


# Hakee aktiviteetit, katon jos tartten.
def get_activities():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())

# Return activity['tags'] dictionaryn value arvot listana.
def printtags(activities):
    return list(activities['tags'].values())

# Search activities['data'] with given input to find activities with matching tags
# Pidän tän täs silt varalt et tätä tarttee.
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

# Pidän tän täs silt varalt et tätä tarttee.
def post_activities(data, chosen):

    list = []

    # loop every value in data
    for x in data:
        # loop every value in data['tags'] in x position/value
        for y in x['tags']:
            # if chosen(user input) value found inside, then add finnish name to list
            if chosen in y['name']:
                list.append(x['name']['fi'])
                # if chosen found in tags, do not go through all tags (might give duplicates otherwise)
                break

# Flask jutut.

# Aktiviteetit
@app.route('/app/activities', methods=['GET'])
def return_activities(activities = get_activities()):
    return jsonify({'activities': activities['data']})

# Tägit
@app.route('/app/tags', methods=['GET'])
def return_tags(activities = get_activities()):
    return jsonify({'tags': printtags(activities)})

# Hae aktiviteettejä tägien mukaan
@app.route('/app/activities/search', methods=['GET'])
def return_activitysearch():
    tags = request.args.get('tags')

    with urllib.request.urlopen("http://open-api.myhelsinki.fi/v1/activities/?tags_search="+tags) as response:
        return json.loads(response.read())


if __name__ == '__main__':
    app.run(debug=True)
