import random
names_string=input("enter names separated by a comma\n")
names=names_string.split(", ")
name=random.choice(names)
print(f"{name} will pay the bill")
#another way of doing it

namez=len(names)
random_nam=random.randint(0, namez-1)
random_name=names[random_nam]
print(f"{random_name} is gonna pay the bill :)")