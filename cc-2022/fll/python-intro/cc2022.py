print ("alaa")
print ("abdulmuhaymin")
print ("samiha")
print ("ryan")
print ("mohammad")
print ("Naushad")
print ("noor")
print ("maryam")
print ("destina")

numberOfSubjects = 5


def average(sum_of_grades, number_of_grades):
    return sum_of_grades / number_of_grades

# get_text(name) -> name grades average
# get_text("alaa") -> "alaa grades average"


def get_text(name):
    return name + "'s Grades Average "


abdulmuhaymin_grades = (96 + 50 + 100 + 50 + 90)
samiha_grades = (94 + 84 + 82 + 50 + 95)
naushad_grades = (72 + 75 + 74 + 50 + 90)
maryam_grades = (94 + 100 + 100 + 60 + 90)
noor_grades = (100 + 89 + 55 + 50 + 87)
destina_grades = (86 + 84 + 100 + 50 + 100)
ryan_grades = (100 + 90 + 99 + 50 + 90)
mohammad_grades = (88 + 75 + 100 + 50 + 92)

print (get_text("abdulmuhaymin ") + str(average(abdulmuhaymin_grades, numberOfSubjects)))
print (get_text("samiha") + str(average(samiha_grades, numberOfSubjects)))
print (get_text("Naushad") + str(average(naushad_grades, numberOfSubjects)))
print (get_text("maryam") + str(average(maryam_grades, numberOfSubjects)))
print (get_text("noor") + str(average(noor_grades, numberOfSubjects)))
print (get_text("destina") + str(average(destina_grades, numberOfSubjects)))
print (get_text("ryan") + str(average(ryan_grades, numberOfSubjects)))
print (get_text("mohammad") + str(average(mohammad_grades, numberOfSubjects)))

''' average is sum/number'''

