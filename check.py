import datetime
def check():
  user_input = int(input("Enter the year you were born: "))
  year = datetime.date.today().year
  print(f"You were born in {user_input). That was {user_input-year} years ago!)
check()
