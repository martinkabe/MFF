    
def convert_hms(seconds_total):
    hours = seconds_total // (60*60)
    seconds_total %= (60*60)
    minutes = seconds_total // 60
    seconds_total %= 60
    return "celkem: %2i:%02i:%02i" % (hours, minutes, seconds_total)


def calc_seconds(time_splitted_arr):
    if len(time_splitted_arr) != 3:
        return([])
    return(int(time_splitted_arr[0])*3600 + int(time_splitted_arr[1])*60 + int(time_splitted_arr[2]))


def calc_sum_activities():
    total_seconds = 0
    inpt = ''
    while inpt != '.':
        inpt = input()
        inputs = inpt.split()
        if len(inputs) == 0:
            continue
        if inputs[0] == inputs[(len(inputs)-2)] and len(inputs) > 1:
            start_time_seconds = calc_seconds(inputs[1].split(':'))
            end_time_seconds = calc_seconds(inputs[(len(inputs)-1)].split(':'))
            total_seconds += (end_time_seconds - start_time_seconds)
    return(convert_hms(total_seconds))


if __name__=="__main__":
    print(calc_sum_activities())
