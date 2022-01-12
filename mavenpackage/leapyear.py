
def leapyear(year):
    
    if (year % 4) == 0:       
        
        if (year % 100) == 0:   
           
            if (year % 400) == 0:   
                return True         
            else:
                return False
        else:
             return True       
    else:
        return False

    
year = int(input("Enter the number: "))

if(leapyear(year)):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year". format(year))

