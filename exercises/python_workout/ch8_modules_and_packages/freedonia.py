# Problem: calculate the final total for a sale of goods.  Tax rate varies on time of day and region.
# Input: pre-tax sale amount, region, hour of day
# Output: final total

class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


class RegionNotFoundError(Exception):
    pass


tax_rates = {'Chico': .5,
             'Groucho': .7,
             'Harpo': .5,
             'Zeppo': .4}


def percentage_of_day(hour: int) -> float:
    """ Find the time of day percentage """

    if hour < 0:
        raise HourTooLowError(f'{hour} is < 0')
    elif hour >= 24:
        raise HourTooHighError(f'{hour} is >= 24')
    else:
        return hour/24


def calculate_with_tax(sale_amount: float, region: str, hour: int) -> float:
    """ Calculate the final sale after tax"""

    if region not in tax_rates:
        raise RegionNotFoundError(f'{region} was not found in the tax table')

    return sale_amount + (sale_amount * tax_rates[region] * percentage_of_day(hour))
