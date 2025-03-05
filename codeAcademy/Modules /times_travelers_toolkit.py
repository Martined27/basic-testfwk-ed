from datetime import datetime as dt 
from decimal import Decimal
from random import choice,randint
import custom_module

current_date = dt.today().strftime("%B %d, %Y")
current_datetime = dt.now()
current_date = current_datetime.strftime("%B %d, %Y")
current_time = current_datetime.strftime("%H:%M:%S")
print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")

#####################
base_cost = Decimal('1000.00')
current_year = dt.now().year
target_year = 2050  
def calculate_final_cost(base_cost, current_year, target_year):
    year_difference = abs(current_year - target_year)
    final_cost = base_cost * Decimal(year_difference)
    return f"{final_cost:.2f}"

base_cost = Decimal('1000.00')
current_year = dt.now().year
formatted_final_cost = calculate_final_cost(base_cost, current_year, target_year)


print(formatted_final_cost)
#####################
start_year = 1900
end_year = 2100

random_year = randint(start_year, end_year)

print(random_year)
#####################
destinations = ["Ancient Rome", "Medieval Europe", "Future Mars Colony", "Renaissance Florence", "Dinosaur Era"]

random_destination = choice(destinations)
print(random_destination)

message = custom_module.generate_time_travel_message(random_year, random_destination, formatted_final_cost)

# Print the message
print(message)