import json
from pprint import pprint
from flask import Flask, jsonify, abort
import unicodedata

cardData = ''
with open('json_data/AllSets.json') as data_file:
    cardData = json.load(data_file)
    #testName = "Descend upon the Sinful"

    #for set_id in cardData:
    #    cardsList = cardData[set_id]["cards"]
    #    for card in cardsList:
    #        nameToTest = card["name"]
    #        if nameToTest == testName:
    #            print("Found it "+nameToTest)
    #            card["imageURL"] = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid="+str(card["multiverseid"])+"&type=card"
    #            pprint(card)
    #            break

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)
app = Flask(__name__)

@app.route(('/'))
def index():
    return "Hello World"

@app.route('/mtgcards/info/card/<string:card_name>', methods=['GET'])
def get_card_image_url(card_name):
    card_name = normalize_caseless(card_name)
    pprint("looking for card "+card_name)
    for set_id in cardData:
        cardsList = cardData[set_id]["cards"]
        for card in cardsList:
            nameToTest = normalize_caseless(card["name"])
            if nameToTest == card_name:
                print("Found it "+nameToTest)
                card["imageURL"] = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid="+str(card["multiverseid"])+"&type=card"
                #pprint(card)
                return jsonify(card)
    abort(404)

#@app.route(('/mtgcards/card')


if __name__ == '__main__':
    app.run(debug=True)