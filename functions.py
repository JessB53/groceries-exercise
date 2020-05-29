# custom-functions/my_functions.py

# TODO: define temperature conversion function here

def celsius_to_fahrenheit(c):
    return c * (9/5) + 32

#def celsius_to_fahrenheit(celsius_temp):
    # print(celsius_temp)
    # breakpoint()
    # f_temp = 9/5 * celsius_temp + 32
    # return f_temp

# TODO: define gradebook function here

def numeric_to_letter_grade(n):
    if n < 60:
        return "F"
    elif n < 70:
        return "D"
    elif n < 80:
        return "C"
    elif n < 90:
        return "B"
    else:
        return "A"

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    

    print("--------------------")
    score = float(input("Please input a numeric letter grade (from 0 to 100):"))
   # score = 87.5
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)