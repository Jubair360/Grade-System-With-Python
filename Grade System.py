number = int(input('Enter Your Number:'))

if (number>90 and number<=100):
    print('Brillinat Your Grade is Wow')
elif (number>100):
    print('Your Input is Wrong')
elif(number>80 and number<=90):
    print('Your Grade is A+')
elif(number>75 and number<=80):
    print('Your Grade is A')
elif(number>70 and number<=75):
    print('Your Grade is A-')
elif(number>65 and number<=70):
    print('Your Grade is B+')
elif(number>60 and number<=65):
    print('Your Grade is B')
elif(number>55 and number<=60):
    print('Your Grade is B-')
elif(number>50 and number<=55):
    print('Your Grade is C+')
elif(number>45 and number<=50):
    print('Your Grade is C')
elif(number>=40 and number<=45):
    print('Your Grade is D')
elif (number>0 and number<40):
    print('You are Fail')

else:
    print('Your Input Is Wrong')
