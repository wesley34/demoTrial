import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluate_revisitgeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    shapeCoordinates = data.get("shapeCoordinates");
    lineCoordinates = data.get("lineCoordinates")
    shapeCoordinates_list = []
    lineCoordinates_list = []
    for i in shapeCoordinates:
        shapeCoordinates_list.append([i.get("x"),i.get("y")])
    for i in lineCoordinates:
        lineCoordinates_list.append([i.get("x"),i.get("y")])
    result = interset_factory(shapeCoordinates_list,lineCoordinates_list)
    
    answer = []
    for i in result:
        answer.append({"x":i[0],"y":i[1]})
 

    logging.info("My result :{}".format(result))
    return jsonify(answer)


def interset_factory(shapeCoordinates_list,lineCoordinates_list):
    all_lines_from_shape= line_factory(shapeCoordinates_list)
    all_lines_from_points= line_factory(lineCoordinates_list)
    print("all_lines_from_shape",all_lines_from_shape)
    print("all_lines_from_points",all_lines_from_points)
    result = []
    for i in all_lines_from_points:
        for j in all_lines_from_shape:
            intercept = line_intersection(i,j)
            if intercept != None and intercept not in result:
                result.append(intercept)
   
    return result

def line_factory(shapeCoordinates_list):
    all_lines_from_shape = []
    for j in range(len(shapeCoordinates_list)-1):
        all_lines_from_shape.append([shapeCoordinates_list[j],shapeCoordinates_list[j+1]])
    all_lines_from_shape.append([shapeCoordinates_list[0],shapeCoordinates_list[-1]])
    return all_lines_from_shape

def line_intersection(line1, line2):
   
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div


    # if 60 == round(x * 100)/100  or -21 == round(x * 100)/100 :
    #     print("DEbug")
    #     print(x,y)
    #     print(line1,line2)
    if x > line2[0][0]  and x >line2[1][0] or x < line2[0][0] and  x < line2[1][0] or y > line2[0][1]  and y >line2[1][1] or y < line2[0][1]  and y < line2[1][1]  :
        return None
    
    return round(x * 100) / 100, round(y * 100) / 100


def calculate_shape_slopes(x1,y1,x2,y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return [a,b]