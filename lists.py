# Creating new lists of boolean
test_ratings = [1, 2, 3, 4, 5]

test_liked = [i>=4 for i in test_ratings]
print(test_liked)



# Say you're doing analytics for a website. You need to write a function that returns the percentage growth in the total number of users relative to a specified number of years ago.

# Your function percentage_growth() should take two arguments as input:

# num_users = Python list with the total number of users each year. So num_users[0] is the total number of users in the first year, num_users[1] is the total number of users in the second year, and so on. The final entry in the list gives the total number of users in the most recently completed year.
# yrs_ago = number of years to go back in time when calculating the growth percentage
# For instance, say num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078].

# if yrs_ago = 1, we want the function to return a value of about 0.036. This corresponds to a percentage growth of approximately 3.6%, calculated as (2001078 - 1930992)/1930992.
# if years_ago = 7, we would want to return approximately 0.66. This corresponds to a percentage growth of approximately 66%, calculated as (2001078 - 1204334)/1204334.


# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-1-yrs_ago])/num_users[len(num_users)-1-yrs_ago]
    growth_formatted = "{:.3f}".format(growth)
    return growth_formatted

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))
