nrfee = 6200
house_fee = 3500
meal_fee = 2000

stud_processed = input()

student_list = raw_input()
student_list = student_list.split()
student_ID = student_list[0]
initials = student_list[1]
cred_request = student_list[2]
residency = student_list[3]

print ("Student ID: %s \nInitials: %s \nCredits Requested: %s \nResidency: %s" % (student_ID, initials, cred_request, residency))
#
# if residency.upper() == "N":
#     tuition = cred_request*285 #cred non-res
# elif residency.upper() == "R":
#     tuition = cred_request*130 #cred res
# else:
#     return None


# student1 = list(raw_input())
# student_list.update(student1)

# print(student_list)
# student_ID
# initials
# credit_requested
# res_status R or N
# hous_req H or O
# meal_req M or N

# if resident =/= housing; meal plans
#
# student #:
# initials:
# residency status:
# credits:
# tuition:
# total due:
#
# FINAL TOTALS
# valid request count
# invalid request count
# total fees due
