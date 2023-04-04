def computepay():
    try:
        xy=input('Enter Hours:')
        xyz=input('Enter Rate:')
        abc = int(xy)
        abcd = int(xyz)
        if abc > 40:
            fty = abc-40
            ftyd = fty *1.5 *abcd
            ab = ftyd + 40 *abcd
            print(ab)
        elif abc < 40:
            ghi = abc*abcd
            print(ghi)
    except:
        print ('Error, please enter numeric input')
computepay()













