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
        return sum(covid_dict.get(country_name, []))
    return total_cases


country_name = 'Italy'
total_cases = total_registered_cases(covid_data, country_name)
print(total_cases)
