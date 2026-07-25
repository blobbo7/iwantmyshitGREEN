import os, random
randwords = ["Tree", "Green", "Purple", "Walter", "Emo"]
os.system('cat thisiswhatchanges.txt')

file1 = open("thisiswhatchanges.txt", "w") # change file
random.shuffle(randwords)
file1.writelines(randwords)
file1.close()

os.system('git add .')
os.system(f'git commit -m "{random.choice(randwords)}"')
os.system('git push')
