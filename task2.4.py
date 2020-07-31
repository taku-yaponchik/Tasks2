# 4) Ask user keeps two time stamps up to a second. Your task is to find the user user maintains two timestamps up to a second.

txt=input("Please enter the text: ")
x=len(txt)
txt_lower=txt_upper=0
for letter in txt:
    if letter.isupper():
        txt_upper+=1
    elif letter.islower():
        txt_lower+=1
print(txt_upper/x*100,'%')
print(txt_lower/x*100,'%')

