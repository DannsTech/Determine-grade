#Daniela Paez Rodriguez
#2022-03-08
#Grading module

##def main(first, second, third, fourth, fifth):
first = int(input("First test grade:"))
second = int(input("Second test grade:"))
third = int(input("Third test grade:"))
fourth = int(input("Fourth test grade:"))
fifth = int(input("Fifth test grade:"))


def determineGrade(score):
    if score >= 90 and score <= 100:
        print("test score:A")
    if score >= 80 and score <= 89:
        print("test score:B")
    if score >= 70 and score <= 79:
        print("test score:C")
    if score >= 60 and score <= 69:
        print("test score:D")
    if score < 60:
        print("test score:F")



print("First test score:")
determineGrade(first)
print("Second test score:")
determineGrade(second)
print("Third test score:")
determineGrade(third)
print("Fourth test score:")
determineGrade(fourth)
print("Fifth test score:")
determineGrade(fifth)


def calcAverage(num_one, num_two, num_three, num_four, num_five):
    average = num_one + num_two + num_three + num_four + num_five
    average = average / 5
    print("average:", int(round(average, 1)))

calcAverage(first, second, third, fourth, fifth)
