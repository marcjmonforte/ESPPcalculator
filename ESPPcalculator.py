import sys

annual_salary = float(input("What is your annual salary?	"))
estimated_stock_price = float(input("What is the estimated stock price?	"))
max_shares_allowed = int(input("What is the max number of shares allowed?	"))
pay_rate = str(input("Are you paid on a monthly or bimonthly rate?	"))

if pay_rate == "monthly":
	pay_rate_value = 12
elif pay_rate == "bimonthly":
	pay_rate_value = 24

salary_per_pay_period = annual_salary / pay_rate_value
discounted_stock_price = estimated_stock_price * 0.85
max_total_purchase_price = discounted_stock_price * max_shares_allowed
total_salary_collected_over_plan = salary_per_pay_period * 12

suggested_contribution = max_total_purchase_price / total_salary_collected_over_plan
print("\nSuggested percent contribution of salary per pay period:	" + str(suggested_contribution))