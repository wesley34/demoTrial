import logging
import json
import copy as cp

from flask import request, jsonify

from collections import defaultdict
from codeitsuisse import app;

logger = logging.getLogger(__name__)
movement = [[-1,-1],[0,-1],[1,-1], #0 2
            [-1,0],[0,0],[1,0],
            [-1,1],[0,1],[1,1]]    # 6 8 
bounds = [[-1,-1],[1,1]]
game_map = ""
x_width = 0
y_width = 0
infected_number = 0
zero_infected_people = 0
@app.route('/infected', methods=['POST'])
def evaluate_infected():
    global game_map
    global x_width
    global y_height
    global infected_number
    global zero_infected_people
    global all_cluster_dict
    all_cluster_dict = defaultdict(list)
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    game_map = data
    y_height = len(data)
    x_width = len(data[0])
    infected_number = 0
    zero_infected_people = 0

    result = data
    last_game_map = ""
    while last_game_map != game_map:
        map_change()
        last_game_map = cp.deepcopy(game_map)
        map_change()
        map_change()
    all_cluster = find_all_cluster()
    check_cross_overlap(all_cluster)
    print(all_cluster)
    print(all_cluster_dict)
    logging.info("My result :{}".format(result))
    return json.dumps({"answer": game_map})

def check_cross_overlap(all_cluster):
    for i in range(len(all_cluster)):
        for j in range(i,len(all_cluster)):
            if doOverlap(*all_cluster[i],*all_cluster[j]):
                all_cluster_dict[i].append(j)

def doOverlap(l1, r1, l2, r2): 
      
    # If one rectangle is on left side of other 
    if(l1[1] <= r2[1] or l2[1] <= r1[1]): 
        return False
  
    # If one rectangle is above other 
    if(l1[0] >= r2[0] or l2[0] >= r1[0]): 
        return False
  
    return True

def find_all_cluster():
    all_cluster = []
    for x in range(x_width):
        for y in range(y_height):
            if game_map[y][x] == "1":
                all_cluster.append(find_cluster(y,x))
    return all_cluster

def find_cluster(y,x):
    batch = []
    for bound in bounds:
        y += bound[1]
        x += bound[0]
        if y > y_height:
            y -= 1
        if x > x_width:
            x -= 1
        if x < 0:
            x += 1
        if y < 0:
            y += 1
        batch.append([y,x])
    return batch

def map_change():
    for x in range(x_width):
        for y in range(y_height):
            if game_map[y][x] == "1":
                infect(y,x)
    

def infect(y,x):
    for move in movement:
        target_y = y + move[1]
        target_x = x + move[0]
        if game_map[target_y][target_x] == "0":
            game_map[target_y][target_x] = 1