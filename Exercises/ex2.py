age_minimum, height_minimum = 10 , 140

age_input = input("Enter age: ")
age = float(age_input)
if  age>=age_minimum:
        height_input = input("Enter height: ")
        height =float(height_input)
        if  height>=height_minimum:
                print("the costumer able to enter")
        else:
                print("the costumer cannot  enter")
else:
        print("the costumer cannot enter")
