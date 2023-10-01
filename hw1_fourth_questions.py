# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#

import csv

list_of_countries = []

with open('/Users/guillemmirabentrubinat/Library/CloudStorage/OneDrive-Personal/BSE/Computing for Data Science/Problem Sets/hw1/covid.csv', 'r') as file:
    
    reader = csv.reader(file)

    for row in reader:
        if row[0] == 'Country':
            continue
        
        print(row)
        list_of_countries.append(row)

for row in list_of_countries:
    print(row)


list_of_plus_500 = []
list_of_plus_1000 = []
list_of_plus_5000 = []

for country in list_of_countries:
    if int(country[4]) > 5000:
        list_of_plus_5000.append(country)
    
    elif int(country[4]) > 1000:
        list_of_plus_1000.append(country)
    
    elif int(country[4]) > 500:
        list_of_plus_500.append(country)
    
    else:
        continue

#death_confirmed_ratio_500 = []
#death_confirmed_ratio_1000 = []
#death_confirmed_ratio_5000 = []

def ratio_maker(list):
    ratio_list = []
    
    for country in list:
        ratio = int(country[2]) / int(country[1])
        ratio_list.append(ratio)
    
    average = sum(ratio_list) / len(ratio_list)
    return round(average * 100, 4)

print('The average ratio of deaths to confirmed cases is:')
print(f'For countries above 500 active cases: {ratio_maker(list_of_plus_500)} %')
print(f'For countries above 1000 active cases: {ratio_maker(list_of_plus_1000)} %')
print(f'For countries above 5000 active cases: {ratio_maker(list_of_plus_5000)} %')

'''
PD: first we checked the procedure with a not DRY code to make sure it worked and afterwards we made it DRY. Find below the not DRY part of the code:

for country in list_of_plus_500:
    ratio = int(country[2]) / int(country[1])
    death_confirmed_ratio_500.append(ratio)

for country in list_of_plus_1000:
    ratio = int(country[2]) / int(country[1])
    death_confirmed_ratio_1000.append(ratio)

for country in list_of_plus_5000:
    ratio = int(country[2]) / int(country[1])
    death_confirmed_ratio_5000.append(ratio)

average_500 = sum(death_confirmed_ratio_500) / len(death_confirmed_ratio_500)
average_1000 = sum(death_confirmed_ratio_1000) / len(death_confirmed_ratio_1000)
average_5000 = sum(death_confirmed_ratio_5000) / len(death_confirmed_ratio_5000)

print(f'The average ratio of deaths to confirmed cases is:\nFor countries above 500 active cases: {round(average_500 * 100, 2)}%\nFor countries above 1000 active cases: {round(average_1000 * 100, 2)}%\nFor countries above 5000 active cases: {round(average_5000 * 100,2)}%')

'''
