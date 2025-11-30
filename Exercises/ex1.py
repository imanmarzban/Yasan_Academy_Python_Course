vehicle_capacity = 10
vehicle_fee,entry_fee,food_fee = 150,20,5
def try_parse_int(value):
    try:
        return True, int(value)
    except (ValueError, TypeError):
        return False, None

student_count = 0
while True:
        student_count = input("How many students do you have? || input  *  E  *  for exit! ")
        if student_count.lower() == 'e':
                student_count = 0
                break
        result = try_parse_int(student_count)
        if result[0] and result[1]>0 :
                student_count = result[1]
                break
        print("Invalid input ! Try again")

if student_count :
        vehicle_count = student_count / vehicle_capacity if not (student_count % vehicle_capacity) else (student_count // vehicle_capacity)+1
        vehicle_cost_per_student = vehicle_fee * vehicle_count / student_count
        print(f"cost_per_student is : {vehicle_cost_per_student + food_fee + entry_fee}K")
