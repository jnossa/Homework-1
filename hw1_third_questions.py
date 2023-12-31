# %%
# EXERCISE 7
# Now imagine you have a certain data structure that contains information
# about different countries and the number of people who was registered
# with covid in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the number of registered
# cases is not the same (thus the length of the lists can differ)


# Create a function called "total_registered_cases" that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
# The function should return the total number of cases registered so far in that country

covid_data = {'Spain': [4, 8, 2, 0, 1],
              'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}


def total_registered_cases(covid_dict, country_name):
    for key, value in covid_dict.items():
        # Iterate through each item of the dictionary
        return sum(covid_dict.get(country_name, []))
    # Get the sum of the value (list) of the key "country_name"
    return total_cases


country_name = 'Italy'
# Define the country name

total_cases = total_registered_cases(covid_data, country_name)
# Call the function
print(total_cases)

# %%
# EXERCISE 8
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had

covid_data = {'Spain': [4, 8, 2, 0, 1],
              'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}
country_sum = {}


def total_registered_cases_per_country(covid_dict):
    for key, values in covid_dict.items():
        # iterate through each item of the dictionary
        sum_country = sum(values)
        # get the sum of the values
        country_sum[key] = sum_country
        # add the sum as value to each key
    return country_sum


country_sum = total_registered_cases_per_country(covid_data)
# call the function
print(country_sum)


# %%
# EXERCISE 9
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(covid_dict):
    max_case_country = ()
    # Initialize an empty tuple to store the country with the most cases
    cases_by_country = total_registered_cases_per_country(covid_data)
    # Call the function "total_registered_cases_per_country" to get the dictionary with the total cases per country
    for key, value in cases_by_country.items():
        # Iterate through each item of the dictionary
        return max(cases_by_country.items(), key=lambda x: x[1])
    # Get the country with the most cases


max_case_country = country_with_most_cases(covid_data)
# Call the function
print(max_case_country)
