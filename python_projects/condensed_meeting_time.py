def condensed_meeting_time(meetings):
    """
    take a list of meeting times and
    returns a list of condensed ranges

    """
    # first find the len of list
    # if list have just one tuple then return

    sorted_list = sorted(meetings)


    merged_meetings = [sorted_list[0]]


    for current_meeting_start, current_meeting_end in sorted_list[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, last_merged_meeting_end)

        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))
    return merged_meetings



print condensed_meeting_time([(0, 1)])
print condensed_meeting_time([(0, 1), (2, 3)])
print condensed_meeting_time([(1, 4), (2, 3), (4, 5)])
