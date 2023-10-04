#%%
# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x: int):
    return (3 * x)

print(triple(3))

# %%
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#


def subtract(a: int, b: int):
    return (a - b)

print(subtract(3, 2))

# %%
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
list1 = [('foo', 1), ('bar', 3)]

def dictionary_maker(x: tuple):
    return dict((i[0], i[1]) for i in x)

print(dictionary_maker(list1))


# %%
