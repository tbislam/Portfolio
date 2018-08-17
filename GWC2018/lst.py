"""l = [1,2,3,4]
for x in l:
    print(x)"""

j= [1,2,3,2,3,2]

answer = int(input("Choose a number"))


count = 0
#if answer in j:
#    for i in range(len(j)):
#        if j[i] == answer:
#            count += 1
#print(count)

for i in range(len(j)):
    if j[i] == answer:
        count += 1
print(count)
