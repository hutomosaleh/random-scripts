import os

directory = 'files/pokemon/original'
filename = os.listdir(directory)

for i in filename:
    with open('files/poke_list.txt', 'a') as poke:
        poke.write(i[:-4] + '\n')