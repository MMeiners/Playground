# Problem: collect user inputs and return the average.  The scenario asks for the number of minutes needed to run
# 10 km (example was 10-20 minutes).
# Input: number of minutes, pressing enter without a response to calculate
# Output: average of inputs

def average_run_time():
    """Calculate the average values prompted for until no value entered"""

    running_total = 0.0
    number_of_runs = 0

    print('Enter the requested run times in minutes or leave blank and press enter to end')

    while True:
        try:
            current_run_time = input('Enter 10 km run time: ')

            if not current_run_time:
                break

            running_total += float(current_run_time)
            number_of_runs += 1
        except ValueError:
            print('Please enter a valid number or press enter with no response to end')

    if number_of_runs > 0:
        print(f'Average of {running_total/number_of_runs}, over {number_of_runs} runs')
    else:
        print('No runs entered!')


average_run_time()
