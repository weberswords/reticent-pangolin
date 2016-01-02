import sys

script, filename = sys.argv
tuition_input = open(filename)
nrfee = 6200
house_fee = 3500
meal_fee = 2000
rCredit = 130
nrCredit = 285
final_total = 0

for line in tuition_input:
    line = line.split()
    if len(line) == 1:
        stud_processed = int(line[0])
        print("Students to process: %d" % stud_processed)
    elif len(line) > 1:
        stud_done = 0
        total_due = 0
        tuition = 0
        invalid_request = 0
        # while stud_done < stud_processed:
        student_ID = line[0]
        print("\nStudent ID: %s" % student_ID)
        initials = line[1]
        print("Student Initials: %s" % initials.upper())
        residency = line[3]
        if residency.upper() == "R":
            tuition = int(line[2])*rCredit
            print("Residency: resident")
        elif residency.upper() == "N":
            tuition = int(line[2])*nrCredit
            total_due += nrfee
            housing = line[4]
            print("Residency: non-resident")
            if housing.upper() == "O":
                continue
            elif housing.upper() == "H":
                total_due += house_fee
                meal_plan = list[5]
                print("Housing: $ %d" % house_fee)
                if meal_plan.upper() == "N":
                    continue
                elif meal_plan.upper() == "M":
                    total_due =+ meal_fee
                    print("Meals: $ %d" % meal_fee)
        # if int(list[2]) < 1:
        #     print("Insufficient credits.")
        #     invalid_request += 1
        # elif int(list[2]) > 21:
        #     print("Too many credits.")
        #     invalid_request += 1
        else:
            print("Credits: %d" % list[2])
        print("Tuition: $ %d" % tuition)
        print("Total Due: $ %d" % total_due)
        stud_done += 1
        final_total += total_due

print("FINAL TOTALS")
print("Valid request count: %d" % stud_processed)
print("Invalid request count: %d" % invalid_request)
print("Total fees due: $ %d" % final_total)

