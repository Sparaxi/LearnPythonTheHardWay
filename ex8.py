# With this i can set on how much I can show to the user, Example if i do formatter="{}
#1time it only shows 1 of each formatter.format But if i do it 2 times It shows 2 answers of formatter.format"
formatter = "{} {} {} {}"

#With formatter.format i'm telling python to do the following.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
            "Test",
            "Test 2",
            "Test 3",
            "Test 4"
))
