import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluate_magic():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    result = data
    logging.info("My result :{}".format(result))
    return json.dumps(9900)



