user1=(input("Your name: "))
print("Time: ")
h=int(input("Hour: "))
m=int(input("Minute: "))
s=int(input("Second: "))

print("Time 2 part:")
h2=int(input("Hour: "))
m2=int(input("Minute: "))
s2=int(input("Second: "))

print("The difference between the lengths of time in seconds.: ",int((s2+(m2*60)+((h2*60)*60))-(s+(m*60)+((h*60)*60))))
