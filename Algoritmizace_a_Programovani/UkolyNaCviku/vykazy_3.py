def sort_dict_by_value(dict, n):
    dict_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    dict_sorted = {k: v for k, v in dict_sorted}
    dict_sorted_reduced = {k: dict_sorted[k] for k in list(dict_sorted)[:n]}
    return(dict_sorted_reduced)


def print_output(dict_groups):
    for key, value in dict_groups.items():
        print(f"{convert_hms(value)} {key}")


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
    month_dict = {}
    while inpt != '.':
        inpt = input()
        inputs = inpt.split()
        if len(inputs) == 0:
            continue
        if inputs[0] == inputs[(len(inputs)-2)] and len(inputs) > 1:
            key = " ".join(inputs[2:(len(inputs)-2)])
            if key not in month_dict:
                month_dict[key] = []
            start_time_seconds = calc_seconds(inputs[1].split(':'))
            end_time_seconds = calc_seconds(inputs[(len(inputs)-1)].split(':'))
            total = end_time_seconds - start_time_seconds
            if month_dict[key]:
                month_dict[key] += total
            else:
                month_dict[key] = total
    return(sort_dict_by_value(month_dict, n))


if __name__=="__main__":
    print_output(calc_sum_activities(10))
