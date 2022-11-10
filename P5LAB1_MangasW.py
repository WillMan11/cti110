# CTI 110
# P5LAB - Leap Year
# MangasW
# 10/11/2022
def days_in_feb(year):
  isLeap = False
  # Can we divide evenly by four?
  if year % 4 == 0: # it might be
    isLeap = True
    # if it's a century, must be divisible by 400
    if year % 100 == 0:
      if year % 400 == 0:
        isLeap = True
      else:
        isLeap = False
  if isLeap:
    daysInFeb = 29
  else:
    daysInFeb = 28
  print(year, "has", daysInFeb, "days in February.")
        

def main():
  year = int(input("Enter a year: "))
  days_in_feb(year)



# start program
main()
