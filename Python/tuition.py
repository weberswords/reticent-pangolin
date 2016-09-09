#Created December 2015

import sys

script, filename = sys.argv
tuition_input = open(filename)
nrfee = 6200
house_fee = 3500
meal_fee = 2000
rCredit = 130
nrCredit = 285
tuition = 0
stud_done = 0
final_total = 0
invalid_request = 0
stud_processed = tuition_input.readline()
stud_processed = int(stud_processed)
# stud_processed = 3

for line in tuition_input:
    total_due = 0
    line = line.split()
    if len(line) > 1:
        student_ID = line[0]
        initials = line[1]
        credits = int(line[2])
        residency = line[3]
        if credits not in range(1,22):
            invalid_request += 1
            print("\n%s" % student_ID)
            print(initials)
            print("You have either too few or too many credits. \nPlease check and try again.")
            continue
        print("\nStudent ID: %s" % student_ID)
        print("Student Initials: %s" % initials.upper())
        if residency.upper() == "R":
            tuition = int(line[2])*rCredit
            total_due += tuition
            print("Residency: resident")
            print("Credits: %d" % credits)
            print("Tuition: $ %d" % tuition)
        elif residency.upper() == "N":
            tuition = credits*nrCredit
            total_due += tuition
            total_due += nrfee
            print("Residency: non-resident")
            print("Credits: %d" % credits)
            print("Non-resident Fee: $ 6200")
            print("Tuition: $ %d" % tuition)
            housing = line[4]
            if housing.upper() == "O":
                pass
            elif housing.upper() == "H":
                total_due += house_fee
                print("Housing: $ %d" % house_fee)
                meal_plan = line[5]
                if meal_plan.upper() == "N":
                    pass
                elif meal_plan.upper() == "M":
                    total_due += meal_fee
                    print("Meals: $ %d" % meal_fee)
            else:
                pass
        print("Total Due: $ %d" % total_due)
    final_total += total_due
    stud_done += 1
    if stud_done == stud_processed:
        break
print("\nFINAL TOTALS")
valid_request = stud_processed - invalid_request
print("Valid request count: %d" % valid_request)
print("Invalid request count: %d" % invalid_request)
print("Total fees due: $ %d" % final_total)

