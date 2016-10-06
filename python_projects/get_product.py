# From Interview cake Question number 2
# if you have list of element
# get the product of element on each index except that integer


def get_products_of_all_ints_except_at_index(a_list):
    # list to store final data
    product_list = [None] * len(a_list)

    # now get the product of each integer before index

    result = 1
    i = 0

    while i < len(a_list):
        product_list[i] = result
        result *= a_list[i]
        i += 1

    #get the product of each interger after index

    result = 1
    i = len(a_list) - 1
    while i >= 0:
        product_list[i] *= result
        result *= a_list[i]
        i -= 1
    return product_list


print(get_products_of_all_ints_except_at_index([3, 2, 3, 4]))
