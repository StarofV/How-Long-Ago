import datetime
def check():
  user_input = int(input("Enter the year you were born: "))
  year = datetime.date.today().year
  print(user_input, " Was ", -user_input + year, " years ago")
check()
