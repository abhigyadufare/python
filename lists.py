# Creating new lists of boolean
test_ratings = [1, 2, 3, 4, 5]

test_liked = [i>=4 for i in test_ratings]
print(test_liked)
