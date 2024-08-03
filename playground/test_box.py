import pdb
import re


# x = [1, 3, 4]
# y = 2
# z = 3

# result = y + z
# print(result)
# pdb.set_trace()
# result2 = y + x
# print(result2)

text = "My telephone number is 408-555-1234"
re.search(r"\d{3}-\d{3}-\d{4}", text)

"""
Using groups:
We can use groups for any general task that involves grouping together
regular expressions (so that we can later break them down).
Using the phone number example, we can separate groups of regular expressions
using parenthesis:
"""
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
results.group()

"""
Can then also call by group position.
remember groups were separated by parenthesis ()
Something to note is that group ordering starts at 1. Passing in 0 returns everything
"""
results.group(1)


# Test sandbox
# text = "apple with juicy"
# pattern = r"[^\bjuicy]"  # Matches any vowel
# matches = re.findall(pattern, text)
# print(matches)  # Output:

# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
# text = "Hello, would you like 1 some catfish?"
# texttwo = "Hello, would you like to take a catnap?"
# textthree = "Hello, have you seen this caterpillar?"
# text4 = "Hello, would you like some catfish?"

# pattern = r"(^Hello)(.*)(\d)(.*)(\bcat(fish|nap|claw)\b)"
# result = re.search(pattern, texttwo)

# print(result)
# print(result.group(3))
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
