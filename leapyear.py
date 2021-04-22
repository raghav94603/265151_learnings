def check_leap(year):
   # leap=False
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                print("Leap Year")
            else:
                print("Not a leap year")
        else:
            print("Leap Year")

    else:
        print("Not a leap year")

year=int(input())
print(check_leap(year))