import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluate_salads():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    number_of_salads = data.get("number_of_salads");
    salad_prices_street_map = data.get("salad_prices_street_map");
    result = solution(number_of_salads,salad_prices_street_map)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def solution(number_of_salads,salad_prices_street_map):
    print(number_of_salads)
    print(salad_prices_street_map)
    min_money = 9123459
    for stores in salad_prices_street_map:
        salad_counter = 0
        money = 0
        for salad in stores:
            if salad != "X":
                salad_counter+=1
                money += int(salad)
        if salad_counter >= number_of_salads:
            if money < min_money:
                min_money = money
    if min_money == 9123459:
        min_money = 0
    
    return min_money





