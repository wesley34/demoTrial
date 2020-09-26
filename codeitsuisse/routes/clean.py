import logging
import json
from collections import defaultdict
from flask import request, jsonify
from flask.globals import current_app;

from codeitsuisse import app;
###
class Util:
    @staticmethod
    def move(node, target_step,current_position):
        # check limit
        current_status = current_position+target_step
        is_not_in_range =  current_status > len(node) or current_status < 0
        if is_not_in_range:
            return None
        else: 
            if node[current_position+target_step] == 0:
                node[current_position+target_step] = 1
            else:
                node[current_position+target_step] -= 1
            return node

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, parent_node, child_node):
        self.graph[parent_node].append(child_node)
##

logger = logging.getLogger(__name__)
visited = defaultdict(bool)
g = Graph()
@app.route('/clean_floor', methods=['POST'])
def evaluate_clean():
    data = request.get_json()
    
    data = data.get("tests")
    test_case = []
    for i in data:
        print(i)
        test_case.append(BFS(data.get(i).get("floor")))

    result_dict = {}
    j = 0
    for i in data:
        
        result_dict[i] = test_case[j]
        j+=1
    ans = {"answers": result_dict}
  
    logging.info("data sent for evaluation {}".format(data))
   
    return json.dumps(ans)

def possible_movement(current_node,current_pos,current_depth):
    if current_pos >= len(current_node) or current_pos < 0:
        return None
    else:
        
        if current_node[current_pos] == 0:
            current_node[current_pos] = 1
        else:
            current_node[current_pos] -= 1
        return current_node

def BFS(init_node):
    target = [0]*len(init_node)
    
    
    # as we expand this node
    visited[tuple(init_node)] = True
    graph = defaultdict(list)
    queue = []
    queue.append([init_node,0,0])
    
    
    
    
    while queue:
        current_node,current_pos,current_depth = queue.pop(0) 
        print(current_node,current_pos,current_depth)
        visited[tuple(current_node)] = False
        if current_node == target:
            return current_depth
        ###
        right_node = possible_movement(current_node,current_pos+1,current_depth+1)
        left_node = possible_movement(current_node,current_pos-1,current_depth+1)
        if right_node != None:
            graph[tuple(current_node)].append([right_node,current_pos+1,current_depth+1])
            queue.append([right_node,current_pos,current_depth+1])
        if left_node != None:
            graph[tuple(current_node)].append([left_node,current_pos-11,current_depth+1])
            queue.append([left_node,current_pos,current_depth+1])
        ###

        for child_node in graph[tuple(current_node)]: 
            child_node,current_pos,current_depth = child_node

            if child_node == target:
                return current_depth

            if visited[tuple(child_node)] == False: 
                ###
                right_node = possible_movement(current_node,current_pos+1,current_depth+1)
                left_node = possible_movement(current_node,current_pos-1,current_depth+1)
                if right_node != None:
                    graph[tuple(current_node)].append(right_node)
                    queue.append([left_node,current_pos,current_depth+1])
                if left_node != None:
                    graph[tuple(current_node)].append(left_node)
                    queue.append([left_node,current_pos,current_depth+1])
                ###
                visited[tuple(child_node)] = True


