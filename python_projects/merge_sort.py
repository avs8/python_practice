def merge_sort(a_list):
    i = 0
    j = 0
    new_list = []
    #first check length of list is more then 1

    if len(a_list) < 2:
        return a_list

    # devide the list in two half
    # get mid index of list
    mid_length = int(len(a_list)/2)

    right_list = merge_sort(a_list[:mid_length])
    left_list = merge_sort(a_list[mid_length:])



    while i < len(right_list) and j < len(left_list):
        if right_list[i] < left_list[j]:
            new_list.append(right_list[i])
            i += 1
        else:
            new_list.append(left_list[j])
            j += 1



    new_list += right_list[i:]
    new_list += left_list[j:]
    return new_list


print merge_sort([1, 4, 3, 4])


