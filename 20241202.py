
def get_direction(input1, input2):
    if input1 < input2:
        return 'increasing'
    if input1 > input2:
        return 'decreasing'
    return 'stall'


def is_safe(input1, input2, initial_direction):
    safety_threshold = 3
    variance = abs(input1 - input2)
    current_direction = get_direction(input1, input2)

    if current_direction == 'stall':
        return False
    
    if variance > safety_threshold or current_direction != initial_direction:
        return False

    return True


def evaluate_report(report):
    initial_direction = get_direction(report[0], report[1])

    for i in range(len(report) - 1):
        input1 = report[i]
        input2 = report[i+1]
        report_is_safe = is_safe(input1, input2, initial_direction)

        if report_is_safe != True:
            return False

    return True

def analyze_reports(reports):
    safe_report_count = 0
    for report in reports:
        report_is_safe = evaluate_report(report)
        if report_is_safe == True:
            safe_report_count += 1

    return safe_report_count

# Test Cases
assert get_direction(1,2) == 'increasing'
assert get_direction(2,1) == 'decreasing'
assert get_direction(1,1) == 'stall'

assert is_safe(1,2, 'increasing') == True
assert is_safe(1,1, 'increasing') == False
assert is_safe(2,1, 'decreasing') == True
assert is_safe(2,1, 'increasing') == False
assert is_safe(1,5, 'increasing') == False

assert evaluate_report([7,6,4,2,1]) == True
assert evaluate_report([1,2,7,8,9]) == False
assert evaluate_report([8,6,4,4,1]) == False
assert evaluate_report([9,7,6,2,1]) == False

assert (analyze_reports([
    [7,6,4,2,1], # pass
    [1,2,7,8,9], # fail
    [9,7,6,2,1], # fail
    [1,3,2,4,5], # fail
    [8,6,4,4,1], # fail
    [1,3,6,7,9], # pass
])) == 2
