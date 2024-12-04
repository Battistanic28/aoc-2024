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

            if bypass_enabled and i <= len(report)-2:

                problem_index = i+1 if i >= 2 else 0

                if initial_direction != current_direction:
                    del report[problem_index]
                    return is_safe(report)
                if variance < 1 or variance > safety_threshold:
                    del report[problem_index]
                    return is_safe(report)
            else:              
                if initial_direction != current_direction:
                    return False
                if variance < 1 or variance > safety_threshold:
                    return False 
            
        return True


def analyze_reports(reports, bypass_enabled=False):
    safe_report_count = 0
    for report in reports:
        report_is_safe = is_safe(report, bypass_enabled)
        print(report, report_is_safe)
        if report_is_safe == True:
            safe_report_count += 1

    return safe_report_count



# ~~~ Test Cases ~~~
edge_cases = [
    [7, 10, 8, 10, 11],
    [29, 28, 27, 25, 26, 25, 22, 20]
] # all should be True

mock_reports = [    
    [12,2,3,4,5], # pass
    [7,6,4,2,1], # pass
    [1,2,7,8,9], # fail
    [9,7,6,2,1], # fail
    [1,3,2,4,5], # fail
    [8,6,4,4,1], # fail
    [1,3,6,7,9], # pass
]
# assert get_direction(1,2) == 1
# assert get_direction(2,1) == -1
# assert get_direction(1,1) == 0

# assert is_safe([7,6,4,2,1]) == True
# assert is_safe([1,2,7,8,9]) == False
# assert is_safe([8,6,4,4,1]) == False
# assert is_safe([9,7,6,2,1]) == False

# assert (analyze_reports(mock_reports)) == 2


# ~~~ Solve ~~~ 
# array_2d_int = [[int(item) for item in row] for row in array_2d]
# print(analyze_reports(array_2d_int, True))
print(analyze_reports(edge_cases, True))