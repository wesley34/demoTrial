import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluate_social():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data = data.get("tests")
    result = []
    for i in range(0,len(data)):
        
        seats = data.get(str(i)).get("seats")
        people = data.get(str(i)).get("people")
        spaces = data.get(str(i)).get("spaces")
        result.append(solution(seats,people,spaces))
  
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def solution(seats,people,spaces):
    if seats < people:
        return 0
    total_sum = 0
    for i in range(0,int((seats-people))):
        total_sum+=find(seats-i-1,people-1,spaces)
    return total_sum

def find(seats,people,spaces):
    print(seats,people,spaces)
    total_sum = 0
    if seats < 0:
        return 0
    if people == 0:
        if seats >= 0:
            print("OK")
            return 1
    print("check spaces")
    print(spaces,int(seats))
    for i in range(spaces,int((seats))):
        total_sum+=find(seats-i-1,people-1,spaces)
    return total_sum


