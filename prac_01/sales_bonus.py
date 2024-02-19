"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
if sales <= 1000
    bonus = sales * 0.10
else
    bonus = sales * 0.15
display bonus

"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15
print(f"total bonus is ${bonus:.2f}")


