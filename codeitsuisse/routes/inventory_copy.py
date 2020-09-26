import logging
import json
import copy as cp

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management123', methods=['POST'])
def evaluate_inventory_1():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
   
    result = []
    
    for test_case in data:
        result.append(solution(test_case["searchItemName"],test_case["items"]))

    result = data[0]["items"]

    logging.info("My result :{}".format(result))
    return json.dumps({"searchItemName":data[0]["searchItemName"],
                        "items":result})
    

def solution(searchItemName,searchResult):
    print(searchItemName)
    print(searchResult)
    return [1,2,3]