# Build string with string formating
x = "There are %d types of people." % 10
# string variable
binary = "binary"
# string variable
do_not="don't"
# build new string variable with string formating with previous variables
y = "Those who know %s and those who %s" % (binary,do_not)

# Print x variable
print(x)
# Print y variable
print(y)

# Print using x variable with formating
print("I said: %r." % x)
# Print using y variable with formating
print("I also said: '%s'." % y)

# Boolean variable
hilarious = False
# String with boolean variable
joke_evaluation = "Isn't that joke so funny?: %r"

# String with formatting from variable
print(joke_evaluation % hilarious)

# w variable
w = "This is the left side of ..."
# e variable
e = "a string with a right side."

# print string composed with 2 string variables
print(w + e)
