from codeitsuisse.routes.salad_spree import solution
import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluate_contract():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    infected = data.get("infected");
    origin = data.get("origin");
    cluster = data.get("cluster")
    result = solution(infected,origin,cluster)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def solution(infected,origin,cluster):
    print(infected)
    print(infected["name"])
    print(cluster[0]["name"])
    return {"abc":"abs"}



