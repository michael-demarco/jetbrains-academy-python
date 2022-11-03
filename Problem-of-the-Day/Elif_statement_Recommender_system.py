age = int(input())

def switch(age):
    if age <= 16:
        print("Lion King")
    elif 17 <= age <= 25:
        print("Trainspotting")
    elif 26 <= age <= 40:
        print("Matrix")
    elif 41 <= age <= 60:
        print("Pulp Fiction")
    elif 60 < age:
        print("Breakfast at Tiffany's")

switch(age)
