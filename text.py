"""
q14.Convert Words to Their Length

Given:

words = ["Python", "Java", "SQL", "Programming"]

Using list comprehension and len(), create a list containing the length of each word.

"""

words = ["Python", "Java", "SQL", "Programming"]

length=[len(x) for x in words]
print(length)