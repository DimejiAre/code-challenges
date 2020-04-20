# Greedy Algorithm
"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]
"""

def get_products_of_all_ints_except_at_index(int_list):
    
    if len(int_list) < 2:
        raise Exception()
    
    result = [None] * len(int_list)
    product = 1
    
    for i in range(len(int_list)):
        result[i] = product
        product *= int_list[i]
        
    product = 1
    for i in range(len(int_list) -1, -1, -1):
        result[i] = product * result[i]
        product *= int_list[i]
        
    return result
    

    # if len(int_list) < 2:
    #     raise Exception()
    # answer = []
    # visited_product = 1
    # for i in range(len(int_list)):
    #     value = visited_product
    #     for j in range(i+1, len(int_list)):
    #         value *= int_list[j]
    #     visited_product *= int_list[i]
    #     answer.append(value)


    # return answer
