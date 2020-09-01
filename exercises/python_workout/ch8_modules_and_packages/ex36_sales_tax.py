# Problem: create a module to calculate a final sale total and import into this exercise for use
# Input: details of sale (pre-tax amount, region, hour of day)
# Output: final sale price

import freedonia

print('Simple sales tax test')
print('---------------------\n')

print('Region rate table (not adjusted for time of day)')
for region, rate in freedonia.tax_rates.items():
    print(f'{region}: {rate*100}%')

print('\nSamples')
print(f'$100 pre-tax, Chico total after midnight = {freedonia.calculate_with_tax(100, "Chico", 0):.2f}')
print(f'$100 pre-tax, Chico total after noon = {freedonia.calculate_with_tax(100, "Chico", 12):.2f}')
print(f'$100 pre-tax, Chico total at 11 PM = {freedonia.calculate_with_tax(100, "Chico", 23):.2f}')
