import os

"""
    Searches for the directory for files containing a keyword
"""

directory = 'files/pokemon/variants'
filename = os.listdir(directory)
keyword = '-'
original = filename
other = []
searched = []
for index, value in enumerate(filename):
    a = keyword in filename[index]
    if a:
        searched.append(filename[index])
        # os.remove(directory + '/' + filename[index])
    else:
        other.append(filename[index])
        # os.remove(directory + '/' + filename[index])

print(other)
print(searched)
