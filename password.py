import re
a = raw_input("enter the password")
x = True
while x:
    if (len(a)<6):
        print "The password length is too small"
        break
    elif (len(a)>8):
        print "The password length is big"
        break
    elif not re.search("[a-z]",a):
        print "The password doesent contain small characters"
        break
    elif not re.search("[A-Z]",a):
        print "The password doesent contain uppercase characters"
        break
    elif not re.search("[0-9]",a):
        print "The password doesent contain numbers"
        break
    elif not re.search("[$@#]",a):
        print "The password doesent contain valid characters"
        break
    else:
        print "valid password"
        x = False
if x == True:
    print "not valid password"



