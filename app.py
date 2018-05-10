#!flask/bin/python
from http import HTTPStatus

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from .data import get_dict_data, get_suggestion_content

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/all')
def all_data():
    return jsonify(get_dict_data())


@app.route('/vision', methods=['POST'])
@cross_origin()
def vision():
    try:
        data = request.files['image']

        subscription_key = 'a00ae1f36d324283b8f1de56ca7a2c60'
        assert subscription_key

        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"

        headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Tags,Categories,Description,Color'}

        response = requests.post(vision_analyze_url, headers=headers, params=params, json=None, data=data)
        response.raise_for_status()
        analysis = response.json()

        image_caption = analysis["description"]["captions"][0]["text"]
        tags = analysis["tags"]

        # based on caption decide waste CO2 ammount
        '''
        1.28kg CO2 per bottle of wine
        1.2kg CO2 per 12-croissant package 1.2
        Not recycled : 8.4 kg Co2e per kilogram of glass
        Recycled : 1.4 kg Co2e per kilogram of glass
        Not recycled : 6 kg Co2e per kilogram of new plastic
        Recycled : 3.5 kg Co2e per kilogram of plastic
        4.14 kg CO2 per kilogram of water bottle
        0.64789 kg per kg of copying paper
        0.8 kg per kg of paper cup ?
        3.5 kg per kg of plastic cup ?

        '''
        thing = ''

        if 'food' in image_caption or 'orange' in image_caption or 'apple' in image_caption or 'pear' in image_caption:
            thing = 'Food Waste'
        if 'red' in image_caption or 'sign' in image_caption:
            thing = 'Candy Wrapper'

        if 'can' in image_caption or 'beer' in image_caption or 'soda' in image_caption:
            thing = 'Aluminum Can'

        if 'cup' in image_caption:
            if 'paper' in image_caption:
                thing = 'Paper Cup'

            else:
                thing = 'Plastic Cup'
            '''
            if 'coffee' in image_caption:
                thing = 'Mug'	

            '''

        if 'bottle' in image_caption:
            thing = 'Plastic Bottle'
            if 'wine' in image_caption:
                thing = 'Wine Bottle'
        if 'beverage' in image_caption:
            thing = 'Wine Bottle'

        return jsonify({
            'caption': image_caption,
            'product': thing,
            'data': get_suggestion_content(thing)
        }), HTTPStatus.OK
    except Exception as e:
        return {
                   "message": "Internal Server Error",
                   "error": e
               }, HTTPStatus.INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(debug='True')
