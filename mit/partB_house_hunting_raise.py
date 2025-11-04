total_cost = float(input("What's the total cost of your dream house? "))
annual_salary = float(input("What's your annual salary? "))
portion_saved = float(input("How much do you want to save each month? (decimal) "))
semi_annual_raise = float(input("What's your semi-annual raise? (decimal) "))

portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_of_months = 0

while current_savings < down_payment:
    current_savings +=  current_savings*r/12 + portion_saved*monthly_salary
    number_of_months += 1
    if number_of_months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
print(f"You need {number_of_months} months to save for the down payment.")