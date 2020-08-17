# Problem: collect rainfall totals for cities and output the totals
# Input: string for city name and a number for rainfall total
# Output: report showing the sum totals for each input city

from collections import defaultdict


def collect_rain_totals():
    """ Ask user for rainfall for each city """

    rainfall_totals = defaultdict(float)

    while True:
        city_name = input('Please enter the city: ')

        if not city_name:
            break

        current_rain_amount = input(f'Please enter the rainfall for {city_name} in inches: ')

        try:
            rainfall_totals[city_name] += float(current_rain_amount)    # hmm... should check for negative rainfall?
        except (ValueError, TypeError):
            print('Rainfall needs to be a numeric format.')
            continue

    if len(rainfall_totals) > 0:
        for city_name, totals in rainfall_totals.items():
            print(f'{city_name.capitalize()}: {totals:.2f} inches')
    else:
        print('No rain totals collected!')


collect_rain_totals()
