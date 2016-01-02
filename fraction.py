#This program will convert any fraction entered to its simplified whole number and fraction version. The input will be
#ints for numerator, denominator, and the slash will be stored as a char value. The output will be int values for the
#numerator and whole number if applicable. The denominator output will be absolute value of input denominator.
while True:
    fraction = raw_input("Give me a fraction (i.e. 5 / 4): ")
    fraction_list = fraction.split()
    numerator = int(fraction_list[0])
    denominator = int(fraction_list[2])
    if len(fraction_list) < 3:
        print("That's not how you type that. Did you forget a space?")
    if denominator == 0:
        print("You can't have 0 as a denominator. Try again.")
        exit()
    print ("Your fraction is %d/%d" % (numerator, denominator))

    whole_num = int(numerator/denominator)
    remainder = abs(numerator % denominator)
    ans_denom = abs(denominator)

    for number in range(1, ans_denom):
        if ans_denom % number == 0 and remainder % number == 0:
            gcf = number
            print(gcf)

    end_remain = remainder/gcf
    print(end_remain)
    ans_denom = ans_denom/gcf
    print(ans_denom)

    if end_remain == 0:
        print("%d/%d = %d" % (numerator, denominator, whole_num))
    elif whole_num == 0:
        print("%d/%d = %d/%d" % (numerator, denominator, end_remain, ans_denom))
    else:
        print("%d/%d = %d %d/%d" % (numerator, denominator, whole_num, end_remain, ans_denom))