print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

month_name = input("Input the name of Month: ")

if month_name == "February":
    print("Number of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("Number of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("Number. of days: 31 days")
else:
    print("Month not exists")