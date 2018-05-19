import sys

annual_salary = float(sys.argv[1])
estimated_stock_price = float(sys.argv[2])
max_shares_allowed = int(sys.argv[3])

salary_per_pay_period = annual_salary / 12
discounted_stock_price = estimated_stock_price * 0.85
max_total_purchase_price = discounted_stock_price * max_shares_allowed
total_salary_collected_over_plan = salary_per_pay_period * 12

print(max_total_purchase_price / total_salary_collected_over_plan)