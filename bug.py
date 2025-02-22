def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / count
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0, correctly handling the empty list case.