def sort_dict_by_value(dict, n):
    dict_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    dict_sorted = {k: v for k, v in dict_sorted}
    dict_sorted_reduced = {k: dict_sorted[k] for k in list(dict_sorted)[:n]}
    return(dict_sorted_reduced)


def print_output(dict_groups):
    monthly, overall = dict_groups

    for key, value in monthly.items():
        print(f"{key}:")
        for key_val, value_val in value.items():
            print(f"{convert_hms(value_val)} {key_val}".lstrip())
        print("")

    for key_overall, value_overall in overall.items():
        print(f"{convert_hms(value_overall)} {key_overall}".lstrip())


def convert_hms(seconds_total):
    hours = seconds_total // (60*60)
    seconds_total %= (60*60)
    minutes = seconds_total // 60
    seconds_total %= 60
    return "%2i:%02i:%02i" % (hours, minutes, seconds_total)


def calc_seconds(time_splitted_arr):
    if len(time_splitted_arr) != 3:
        return([])
    return(int(time_splitted_arr[0])*3600 + int(time_splitted_arr[1])*60 + int(time_splitted_arr[2]))


def calc_sum_activities(n):
    inpt = ''
    dict = {}
    month_dict = {}
    activities_total_dict = {}

    while inpt != '.':
        inpt = input()
        inputs = inpt.split()
        if len(inputs) == 0:
            continue
        if inputs[0] == inputs[(len(inputs)-2)] and len(inputs) > 1:
            d, m, y = inputs[0].split('.')
            key = f"{m}/{y}"
            activities = " ".join(inputs[2:(len(inputs)-2)])
            start_time_seconds = calc_seconds(inputs[1].split(':'))
            end_time_seconds = calc_seconds(inputs[(len(inputs)-1)].split(':'))
            total = end_time_seconds - start_time_seconds
            
            if key not in dict:
                dict[key] = []
            
            if activities not in month_dict:
                month_dict[activities] = []
            
            dict[key].append([total, activities])
            
            if month_dict[activities]:
                month_dict[activities] += total
            else:
                month_dict[activities] = total
            
    for key, value in dict.items():
        activities_dict = {}
        for val in value:
            if val[1] not in activities_dict:
                activities_dict[val[1]] = []

            if activities_dict[val[1]]:
                activities_dict[val[1]] += val[0]
            else:
                activities_dict[val[1]] = val[0]
        
        if key not in activities_total_dict:
            activities_total_dict[key] = []

        if activities_total_dict[key]:
            activities_total_dict[key] += sort_dict_by_value(activities_dict, n)
        else:
            activities_total_dict[key] = sort_dict_by_value(activities_dict, n)
            
    return(
        activities_total_dict, 
        sort_dict_by_value(month_dict, n)
    )


if __name__=="__main__":
    print_output(calc_sum_activities(10))
