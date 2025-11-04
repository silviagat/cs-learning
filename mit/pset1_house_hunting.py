total_cost = float(input("What's the total cost of your dream house? "))
annual_salary = float(input("What's your annual salary? "))
portion_saved = float(input("How much do you want to save each month? (decimal) "))

portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_of_months = 0

while current_savings < down_payment:
    current_savings_monthly =  current_savings*r/12 + portion_saved*monthly_salary
    current_savings += current_savings_monthly
    number_of_months +=1
print(f"You need {number_of_months} months to save for the down payment.")