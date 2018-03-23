import datetime
user_input = int(input("Enter the year you were born: "))
def check():
  year = datetime.date.today().year
  print(f"You were born in {user_input). That was {user_input-year} years ago!)
check()
