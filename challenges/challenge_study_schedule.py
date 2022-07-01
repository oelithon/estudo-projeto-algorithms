def study_schedule(permanence_period, target_time):
    count_target_repeat = 0
    if type(target_time) != int:
        return None
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            count_target_repeat += 1

    return count_target_repeat


# print(study_schedule(
#     [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2
# ))
