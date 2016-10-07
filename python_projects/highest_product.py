# Interview cake question 3
# Given a list of integer get the max product
# by mutiplying you can get from three int

def highest_product(a_list):
    result = 1
    counter = 0
    if len(a_list) < 3:
        print "To fine highest product of three we need list len more then 3"
        return a_list
    if len(a_list) == 3:
        for i in a_list:
            result *= i
        return result
    if len(a_list) > 3:



    product_list = []
    result = 1
    result2 = 1

    i = 0
    j = 0
    k = 0

    for i in a_list:
        result *= i
    for j in a_list[::-1]:
        result2 *= j

    product_list.append(result)
    product_list.append(result2)
    print product_list


print(highest_product([2,3]))
print(highest_product([2,3,4]))