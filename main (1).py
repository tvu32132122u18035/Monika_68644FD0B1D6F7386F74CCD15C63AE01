year=int(input(" Enter the year:")) 
if(year%4==0 and year%100!=0):
  print("{} if a leap year.".format(year) )
elif(year%400==0) :
  print("{} is a leap year. ".format(year) )
else:
  print(" {} is not a leap year.".format(year) )