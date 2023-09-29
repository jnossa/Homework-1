# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x:int):
    return (3 * x)

#%%
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def substract(a: int, b: int):
    return(a - b)
#%%
# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

def dictionary_maker(x:tuple):
    return dict((i[0], i[1]) for i in x )
#%%

############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#
#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv: dict, job: str):
    return [k['user'] for k in cv if any([True if j == job else False for j in k["jobs"]])]

#%%

#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def count_jobs(data):
    job_counts = {}  
    for entry in data:
        user_jobs = entry.get('jobs', [])  # Get the 'jobs' list for the user (default to an empty list)
        
        # Iterate through the jobs for the current user
        for job in user_jobs:
            # Update the job counts dictionary
            if job in job_counts:
                job_counts[job] += 1  # Increment the count if the job already exists
            else:
                job_counts[job] = 1  # Initialize the count if the job is encountered for the first time

    return job_counts

data = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
        {'user': 'jane', 'jobs': ['finance', 'software']},
        {'user': 'jack', 'jobs': ['engineer', 'software', 'lawyer']}]

count_jobs(data)
#%%

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(data):
    job_counts = {}  # Initialize an empty dictionary to store job counts

    # Iterate through each dictionary in the list
    for entry in data:
        user_jobs = entry.get('jobs', [])  # Get the 'jobs' list for the user (default to an empty list)
        
        # Iterate through the jobs for the current user
        for job in user_jobs:
            # Update the job counts dictionary
            if job in job_counts:
                job_counts[job] += 1  # Increment the count if the job already exists
            else:
                job_counts[job] = 1  # Initialize the count if the job is encountered for the first time

    # Find the most popular job and its count
    most_popular = max(job_counts.items(), key=lambda x: x[1], default=(None, 0))

    return most_popular

data = [{'user': 'john', 'jobs': ['software', 'engineer']},
        {'user': 'jane', 'jobs': ['finance', 'software']},
        {'user': 'jack', 'jobs': ['engineer', 'software', 'lawyer']}]

most_popular_job(data)
#%%

##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases



###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
