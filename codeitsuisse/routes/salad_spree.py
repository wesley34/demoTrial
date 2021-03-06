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
    print(jsonify(salad_prices_street_map))
    result = solution(number_of_salads,salad_prices_street_map)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def get_cheapest_queue(cheapest_at_the_store,current_price):
    
    for i in reversed(range(len(cheapest_at_the_store))):
        if cheapest_at_the_store[i] > current_price:
            cheapest_at_the_store[i] = current_price
            break
    cheapest_at_the_store.sort()
    
    return cheapest_at_the_store



def solution(number_of_salads,salad_prices_street_map):
    min_money = 99999999999
    original = 99999999999
    if number_of_salads > len(salad_prices_street_map[0]):
        return 0 
    for store in salad_prices_street_map:

        consec_counter = 0
        one_store_total_price = 0
        temp = []

        for i in range(len(store)):
            if store[i] != "X":
                consec_counter+=1
                current_price = int(store[i])
                temp.append(current_price)
            
            if store[i] == "X" or i == len(store)-1:
                if consec_counter >= number_of_salads:
                    # sort it
                    temp.sort()
                    # get the answer
                    for i in range(number_of_salads):
                        one_store_total_price += temp[i]
                    if min_money > one_store_total_price:
                        min_money = one_store_total_price
                
                one_store_total_price = 0
                temp = []
                consec_counter = 0

       
    

    if min_money == original:
        min_money = 0
    return{ "result": min_money}




