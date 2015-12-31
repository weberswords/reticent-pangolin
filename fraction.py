#This program will convert any fraction entered to its simplified whole number and fraction version. The input will be
#ints for numerator, denominator, and the slash will be stored as a char value. The output will be int values for the
#numerator and whole number if applicable. The denominator output will be absolute value of input denominator.
while True:
    fraction = input("Give me a fraction (i.e. 5 / 4): ")
    fraction_list = fraction.split()
    if len(fraction_list) < 3:
        print("That's not how you type that. Did you forget a space?")
        continue
    numerator = int(fraction_list[0])
    denominator = int(fraction_list[2])
    if denominator == 0:
        print("You can't have 0 as a denominator. Try again.")
        exit()
#print fraction
    print ("So your fraction is %d / %d" % (numerator, denominator))

#numerator/denominator
    whole_num = int(numerator/denominator)

#remainder
    remainder = abs(numerator % denominator)

#absolute value of denominator
    ans_denom = abs(denominator)

#print whole number with fraction
    def answer():
        if remainder == 0:
            print("%d/%d = %d" % (numerator, denominator, whole_num))
        elif whole_num == 0:
            print("%d/%d = %d/%d" % (numerator, denominator, remainder, ans_denom))
        else:
            print("%d/%d = %d %d/%d" % (numerator, denominator, whole_num, remainder, ans_denom))

    answer()
#simplify fraction
