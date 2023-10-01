# %%

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

# %%

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
        # Get the 'jobs' list for the user (default to an empty list)
        user_jobs = entry.get('jobs', [])

        # Iterate through the jobs for the current user
        for job in user_jobs:
            # Update the job counts dictionary
            if job in job_counts:
                # Increment the count if the job already exists
                job_counts[job] += 1
            else:
                # Initialize the count if the job is encountered for the first time
                job_counts[job] = 1

    return job_counts


data = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
        {'user': 'jane', 'jobs': ['finance', 'software']},
        {'user': 'jack', 'jobs': ['engineer', 'software', 'lawyer']}]

count_jobs(data)
# %%

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
        # Get the 'jobs' list for the user (default to an empty list)
        user_jobs = entry.get('jobs', [])

        # Iterate through the jobs for the current user
        for job in user_jobs:
            # Update the job counts dictionary
            if job in job_counts:
                # Increment the count if the job already exists
                job_counts[job] += 1
            else:
                # Initialize the count if the job is encountered for the first time
                job_counts[job] = 1

    # Find the most popular job and its count
    most_popular = max(job_counts.items(),
                       key=lambda x: x[1], default=(None, 0))

    return most_popular


data = [{'user': 'john', 'jobs': ['software', 'engineer']},
        {'user': 'jane', 'jobs': ['finance', 'software']},
        {'user': 'jack', 'jobs': ['engineer', 'software', 'lawyer']}]

most_popular_job(data)
