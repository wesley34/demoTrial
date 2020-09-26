import logging
import json
import copy as cp

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluate_inventory():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
   
    result = []
    for test_case in data:
        result.append(solution(test_case["searchItemName"],test_case["items"]))

    logging.info("My result :{}".format(result))
    return json.dumps({"searchItemName":data[0]["searchItemName"],
                        "items":result})
    

def solution(searchItemName,searchResult):
    print("Start")
 
    word_2 = searchItemName
    copy = searchItemName
    result = []
    for word_1 in searchResult:
        result.append(search_snap(word_1,word_2))
    return result
    #### algo part
    

def search_snap(word_1,word_2):
    word_1_counter = 0
    word_2_counter = 0
    copy = word_2
    
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    
    #print(word_1,word_2)
    markup = []
    while word_2_counter < len(word_2):
       
        #print(word_1[word_1_counter],word_2[word_2_counter])
        if word_1[word_1_counter] == word_2[word_2_counter]:
            word_1_counter += 1
            word_2_counter += 1
        else:
            # find word_1 the nearest exsit temr in word_2
            #print("Enter")
            find_space = word_2.find(" ",word_2_counter)
            found_pointer = word_2.find(word_1[word_1_counter],word_2_counter)
            is_found_larger_than_space = find_space < found_pointer and find_space != -1
            if is_found_larger_than_space:
                # + that string to word_2
                string_to_be_inserted = "+"+word_1[word_1_counter]
                markup.append([word_2_counter+1, string_to_be_inserted])
                word_1_counter+=1
                continue
            if found_pointer == -1 :
                #print("Find for -1 case")
                #print(word_1[word_1_counter],word_2[word_2_counter])
                # check if need replacement
                #print("you want to check")
                #print(word_2[word_2_counter+1], word_1[word_1_counter+1])
                check_ch = word_1[word_1_counter+1]
                
                    
                after_pointer = word_2.find(check_ch,word_2_counter)
                #print(word_1[word_1_counter],word_2[word_1_counter])
                #print("Check",check_ch)
                if check_ch == " ":
                    #print("HI")
                    after_pointer = -1
                if after_pointer != -1:
                    string_to_be_replaced = word_1[word_1_counter]
                    markup.append([word_2_counter, string_to_be_replaced])
                    word_2_counter+=1
                    word_1_counter+=1
                else: 
                    # + that string to word_2
                    string_to_be_inserted = "+"+word_1[word_1_counter]
                    markup.append([word_2_counter+1, string_to_be_inserted])
                    word_1_counter+=1
            else:   
                # - the in-between string
                for in_between in range(word_2_counter,found_pointer):
                    markup.append([in_between, "-"+copy[in_between]])
                word_2_counter = found_pointer
             
    question_list = [i for i in copy]
    print(markup)
    try:
        for i in markup:
            #print(i[0],i[1])
            question_list[i[0]] = i[1]
            answer = "".join(str(x) for x in question_list)
    except:
        pass
    
    answer = "".join(str(x) for x in question_list)
    
    return answer


