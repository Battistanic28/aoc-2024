# run `python3 input/day_2/script.py from root to generate formatted input`
from input.day_2.output import array_2d

def get_direction(input1, input2):
    if input1 < input2:
        return 1
    if input1 > input2:
        return -1
    return 0

def is_safe(report, bypass_enabled=False):
        safety_threshold = 3
        initial_direction = get_direction(report[0], report[1])

        for i in range(len(report)-1):
            input1 = report[i]
            input2 = report[i+1]
            current_direction = get_direction(input1, input2)
            variance = abs(input1 - input2)

            if initial_direction != current_direction:
                 return False
            if variance < 1 or variance > safety_threshold:
                 return False 
            
        return True


def analyze_reports(reports, bypass_enabled=False):
    safe_report_count = 0
    for report in reports:
        report_is_safe = is_safe(report, bypass_enabled)
        if report_is_safe == True:
            safe_report_count += 1

    return safe_report_count



# ~~~ Test Cases ~~~
tricky_report = [12,2,3,4,5] # unsolved case - report[0] is the single problem
mock_reports = [    
    [7,6,4,2,1], # pass
    [1,2,7,8,9], # fail
    [9,7,6,2,1], # fail
    [1,3,2,4,5], # fail
    [8,6,4,4,1], # fail
    [1,3,6,7,9], # pass
]
assert get_direction(1,2) == 1
assert get_direction(2,1) == -1
assert get_direction(1,1) == 0

assert is_safe([7,6,4,2,1]) == True
assert is_safe([1,2,7,8,9]) == False
assert is_safe([8,6,4,4,1]) == False
assert is_safe([9,7,6,2,1]) == False

assert (analyze_reports(mock_reports)) == 2


# ~~~ Solve ~~~ 
array_2d_int = [[int(item) for item in row] for row in array_2d]
print(analyze_reports(array_2d_int, True))