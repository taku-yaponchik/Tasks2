numbers1=[1,2,5,9]
numbers2=[1,2,4,9]
new_number=[]
for i in numbers1:
    if i not in numbers2:
        new_number.append(i)
print(new_number)