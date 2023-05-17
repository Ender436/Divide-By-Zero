num = 1
yourmom = True

while yourmom == True:
    x = 3

    try:
        print("trying to divide by zero")
        poopypoopoo = x/0
        print("3/0 = " + str(poopypoopoo))
        print("division by zero succeeded!")
        tree = input('enter "y" to exit, or "n" to continue\n')
        if tree == "y" or tree == "Y":
            yourmom = False

    except:
        print("attempt " + str(num) + " failed\n")
        num += 1