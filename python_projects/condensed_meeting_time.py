def condensed_meeting_time(a_list):
    """
    take a list of meeting times and
    returns a list of condensed ranges

    """
    # first find the len of list
    # if list have just one tuple then return

    new = []
    if len(a_list) <= 1:
        return a_list

    if len(a_list) == 2 and a_list[0] < a_list[1]:
        return a_list
    else:
        while len(new) < 2:
            if a_list[0][0] < a_list[1][0]:
                new.append((a_list[0][0]))
            else:
                new.append((a_list[0][1]))
            print new
        # for i in a_list:
        #     for j in i:
        #         if max < j:
        #             max = j,
        #         else:
        #             if min < j:
        #                 return min
        #             else:
        #                 min = j
        #     print max, min



print condensed_meeting_time([(0, 1)])
print condensed_meeting_time([(0, 1), (2, 3)])
print condensed_meeting_time([(3, 1), (2, 3)])
