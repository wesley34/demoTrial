import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluate_clean():
    data = request.get_json();
    data = data.get("tests")
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    answer_list = []
    for i in data:
        print("asd",i)
        snap = data.get(i).get("floor")
        print(snap)
        result = 0
        is_ok_left, answer_left =  move(snap,0,1,0) 
        if is_ok_left:
            result =  answer_left
            answer_list.append(result)
            
  
        is_ok_right,answer_right = move(snap,0,-1,0)
        if is_ok_right:
            result =  answer_right
            answer_list.append(result)

    answer_dict = {}
    j = 0
    for i in data:
       
        answer_dict[i] = answer_list[j]
        j+=1
    final_dict = {}
    final_dict["answers"] = answer_dict
    logging.info("My result :{}".format(answer_list))
    return json.dumps(final_dict)



def move(data,current,step,current_step_used):
    # base case
    #print(current+move)
    if current+step > len(data) or current+step < 0:
        return False, -100

    target_cleanesss = data[current+step] 
    #print("Target",target_cleanesss)
    if target_cleanesss == 0 :
        data[current+step] += 1
    else:
        data[current+step] -= 1
    #print(data)
    for i in data:
        if i != 0:
            is_ok_left, answer_left =  move(data,current+step,-1,current_step_used+1) 
            if is_ok_left:
                return is_ok_left,answer_left
            is_ok_right,answer_right = move(data,current+step,+1,current_step_used+1)
            if is_ok_right:
                return is_ok_right,answer_right
    print("Hello")
    print("FOund",current_step_used+1)
    return True,current_step_used+1
