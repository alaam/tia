# variable integer
abdulmuhaymin_grades = {"Arabic": 96, "ELA": 50, "Science": 100, "Social": 50, "Islam": 90}


# function
def average(grades):
    return (grades.get("Arabic")
            + grades.get("Islam")
            + grades.get("Social")
            + grades.get("Science")
            + grades.get("ELA")) / len(grades)


# hw: find the lowest grade
def highest_grade(grades):
    max_grade = grades.get(grades.keys().pop())
    for grade in grades.values():
        if grade > max_grade:
            max_grade = grade
    return max_grade


def average_using_for(grades):
    grades_sum = 0
    for grade in grades:
        grades_sum = grades_sum + grade
        print ("grade is " + str(grade))
        print ("sum is " + str(grades_sum))

    return grades_sum / len(grades)


# function
def get_text(name):
    return name + "'s Grades Average "


print ("Keys are " + str(abdulmuhaymin_grades.keys()))
print ("Values are " + str(abdulmuhaymin_grades.values()))

print ("abdulmuhaymin highest grade is " + str(highest_grade(abdulmuhaymin_grades)))
print (get_text("abdulmuhaymin ") + str(average(abdulmuhaymin_grades)))

''' average is sum/number'''

