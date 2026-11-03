PASS_SCORE = 70
EXCELLENT_SCORE = 85

while True:
    student_count = int(input("Enter number of students : "))
    if student_count < 1:
        print("Invalid student count !")
    else:
        break 

excellent_count = 0
total_score = 0
passed = 0
lowest_score = 100

for student in range(1, student_count + 1):
    print(f"Student : {student}")

    while True:
        score = int(input("Enter score: "))
        if 0<= score <= 100:
            break
        print("Invalid score!!!!!!!")

    total_score += score
    if score >= PASS_SCORE:
        passed += 1
    if score < lowest_score:
        lowest_score = score

    if score >= EXCELLENT_SCORE:
        excellent_count += 1

average_score = total_score / student_count

print(f"Total score : {total_score}")
print(f"Average score : {round(average_score, 2)}")
print(f"Passed : {passed}")
print(f"Lower score: {lowest_score}")
print(f"Excellent score: {excellent_count}")
