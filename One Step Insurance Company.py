
# Title: Insurance Premium Calculator
# Program Description: This program calculates the insurance premium for customers based on their policy details.
# It takes into account the number of cars insured, additional coverage options, and payment method.
# The default values for the insurance calculation are read from the "OSICDef.dat" file.
# After processing the policy information, the data is saved to the "Policies.dat" file.
# The program provides a receipt for each policy and displays a progress bar during processing.
# Written By: Janna Coles
# Started on: July 17, 2023
# Finished on: July 26, 2023



# Import necessary modules
import datetime
import time

# Function to load default insurance parameters from the OSICDef.dat file
def load_defaults(defaults_file):
    # Read data from the file and parse the values
    with open("OSICDef.dat", 'r') as file:
        lines = file.readline().strip().split(',')
        next_policy_number = int(lines[0])
        basic_rate = float(lines[1])
        discount_rate = float(lines[2])
        liability_cost = float(lines[3])
        glass_cost = float(lines[4])
        loaner_car_cost = float(lines[5])
        hst_rate = float(lines[6])
        processing_fee = float(lines[7])

    # Return the loaded parameters
    return next_policy_number, basic_rate, discount_rate, liability_cost, glass_cost, loaner_car_cost, hst_rate, \
        processing_fee

# Function to save updated default insurance parameters to the OSICDef.dat file
def save_defaults(filename, next_policy_number, basic_premium, discount_additional_cars, liability_coverage_cost,
                  glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee):
    data_to_save = f"{next_policy_number},{basic_premium:.2f},{discount_additional_cars:.2f},"
    data_to_save += f"{liability_coverage_cost:.2f},{glass_coverage_cost:.2f},{loaner_car_cost:.2f},"
    data_to_save += f"{hst_rate:.2f},{processing_fee:.2f}"

# Format the updated parameters and save to the file
    with open(filename, 'w') as file:
        file.write(data_to_save)

# Function to calculate the insurance premium based on policy details
def calculate_insurance_premium(num_cars, options, basic_rate, discount_rate, liability_cost, glass_cost,
                                loaner_car_cost, hst_rate, processing_fee):

    # Calculate the basic premium, extra charges, subtotal, and total cost
    basic_premium = basic_rate * num_cars

    # Apply the discount for additional cars
    if num_cars > 1:
        basic_premium -= (num_cars - 1) * (basic_rate * discount_rate)

    extra_costs = 0

    if options[0] == 'Y':
        extra_costs += num_cars * liability_cost

    if options[1] == 'Y':
        extra_costs += num_cars * glass_cost

    if options[2] == 'Y':
        extra_costs += num_cars * loaner_car_cost

    total_premium = basic_premium
    subtotal = total_premium + extra_costs
    hst_amount = subtotal * (hst_rate / 100)
    total_cost = subtotal + hst_amount

    return total_premium, extra_costs, subtotal, total_cost

# Function to get the first day of the next month from the given date
# Calculate the next month and return the date
def get_next_month(date):
    year = date.year + (date.month // 12)
    month = (date.month % 12) + 1
    return date.replace(year=year, month=month, day=1)

# Function to convert a string to title case
# Convert the string to title case and return
def get_title_case(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

# Function to get a yes/no choice from the user
# Get user input and validate the choice
def get_yes_no_choice(prompt):
    while True:
        choice = input(prompt).upper()
        if choice in ('Y', 'N'):
            return choice
        else:
            print("Invalid input. Please enter Y or N.")

# Function to get a valid province code from the user
# Get user input and validate the province code
def get_province_choice(prompt):
    valid_provinces = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']
    while True:
        province = input(prompt).upper()
        if province in valid_provinces:
            return province
        else:
            print("Invalid province. Please enter a valid two-letter abbreviation (e.g., ON, BC).")

# Function to get the payment method from the user
 # Get user input and validate the payment method
def get_payment_method(prompt):
    valid_methods = ['FULL', 'MONTHLY']
    while True:
        method = input(prompt).upper()
        if method in valid_methods:
            return method
        else:
            print("Invalid payment method. Please enter 'Full' or 'Monthly'.")

# Function to format an amount as currency
# Format the amount as currency and return
def format_currency(amount):
    return "${:,.2f}".format(amount)

# Function to display the receipt for a policy
# Display the receipt for the policy
def display_receipt(policy_number, date, first_name, last_name, address, city, province, postal_code, phone_number,
                    num_cars, options, payment_method, total_premium, extra_charges, subtotal, total_cost, next_payment_date,
                    hst_rate, processing_fee):


    print()
    print()
    print()
    print("*" * 80)
    print(" " * 27, "One Stop Insurance Company")
    print(" " * 32, "106 Major Street")
    print(" " * 33, "Roddickton, NL")
    print(" " * 35, "A0K4P0")
    print(" " * 29, "Phone: (709) 457-2814")
    print(" " * 30, "Fax: (709) 457-3814")
    print("=" * 80)
    print()
    print(
        f"POLICY NUMBER: {policy_number: <10}                               INVOICE DATE: {date.strftime('%Y-%m-%d'): <10}")
    print()
    print("-" * 80)
    print()
    print(f"CUSTOMER INFORMATION                              POLICY INFORMATION")
    print()
    print("-" * 80)
    print()
    print(f"Name: {get_title_case(first_name)} {get_title_case(last_name)}                                 Number of Cars Insured:      {num_cars: <3d} ")
    print(f"Address: {address}                       Extra Liability Coverage:  {'Yes' if options[0] == 'Y' else 'No': <3s}")
    print(f"City: {get_title_case(city): <12}                                Optional Glass Coverage:   {'Yes' if options[1] == 'Y' else 'No': <3s}")
    print(f"Province: {province: <10}                              Optional Loaner Car:       {'Yes' if options[2] == 'Y' else 'No': <3s}")
    print(f"Postal Code: {postal_code: <10}                           Payment Method:        {payment_method: <7s}")
    print(f"Phone Number: {phone_number: <12}")
    print()
    print("-" * 80)
    print()
    print(F"POLICY PREMIUMS TOTALS")
    print()
    print("-" * 80)
    print(f"Insurance Premium Charge:                                              {format_currency(total_premium): <10s}")
    print(f"Total Extra Charges:                                                     {format_currency(extra_charges): <10s}")
    print(f"Subtotal:                                                              {format_currency(subtotal): <10s}")
    print(f"HST({hst_rate:.2f}%):                                                             {format_currency(total_cost - subtotal): <10s}")
    print(f"Total Cost:                                                            {format_currency(total_cost): <10s}")
    print("-" * 80)

    if payment_method == 'MONTHLY':
        monthly_payment = (total_cost + processing_fee) / 8
        print(f"Monthly Payment (including processing fee):                              {format_currency(monthly_payment): <10s}")
        print(f"Next Monthly Payment Due:                                             {next_payment_date.strftime('%Y-%m-%d'): <10s}")

    print("*" * 80)

# Function to show a slow progress bar during processing
# Display a progress bar with a delay
def slow_progress_bar():
    print("Processing...")
    for _ in range(10):
        time.sleep(0.5)  # Half-second delay for the progress bar
        print(".", end="", flush=True)
    print()  # New line after the progress bar

# Main function to execute the insurance premium calculator
# Initialize default file names and load default parameters
def main():
    defaults_file = "OSICDef.dat"
    policies_file = "Policies.dat"

    next_policy_number, basic_rate, discount_rate, liability_cost, glass_cost, loaner_car_cost, hst_rate, processing_fee = load_defaults(
        defaults_file)

# Start processing policies and generating receipts
# Get policy details from the user
# Calculate the insurance premium and total cost
# Generate and display the receipt for the policy
    while True:
        print("Enter the customers policy details")
        print()
        first_name = input("Enter the customers First Name: ").title()
        last_name = input("Enter the customers Last Name: ").title()
        address = input("Enter the customers Street Address: ").title()
        city = get_title_case(input("Enter the customers City: ")).title()
        province = get_province_choice("Enter the customers Province (Two-letter abbreviation): ").upper()
        postal_code = input("Enter the customers Postal Code: ").upper()
        phone_number = input("Enter the customers Phone Number(9999999999): ")
        num_cars = int(input("Enter the number of cars being insured: "))
        extra_liability = get_yes_no_choice("Extra Liability Coverage (Y/N): ").upper()
        glass_coverage = get_yes_no_choice("Optional Glass Coverage (Y/N): ").upper()
        loaner_car = get_yes_no_choice("Optional Loaner Car (Y/N): ").upper()
        payment_method = get_payment_method("Enter the Payment Method (Full/Monthly): ")

        options = [extra_liability, glass_coverage, loaner_car]

        # Calculate insurance premium without the extra coverage charges
        total_premium, extra_charges, subtotal, total_cost = calculate_insurance_premium(num_cars, options, basic_rate,
                                                                                         discount_rate, liability_cost,
                                                                                         glass_cost, loaner_car_cost,
                                                                                         hst_rate, processing_fee)

        invoice_date = datetime.datetime.now()
        next_payment_date = get_next_month(invoice_date)

        # Pass the calculated values to display_receipt()
        display_receipt(next_policy_number, invoice_date, first_name, last_name, address, city, province, postal_code, phone_number, num_cars, options, payment_method, total_premium, extra_charges, subtotal, total_cost, next_payment_date, hst_rate, processing_fee)

        slow_progress_bar()
        print("Policy information processed and saved.")
        print("=" * 80)

        with open(policies_file, 'a') as file:
            file.write(f"{next_policy_number}, {invoice_date.strftime('%Y-%m-%d')}, {first_name}, {last_name}, {address}, "
                       f"{city}, {province}, {postal_code}, {phone_number}, {num_cars}, {extra_liability}, {glass_coverage}, "
                       f"{loaner_car}, {payment_method}, {total_cost:.2f}\n")

        next_policy_number += 1

        save_defaults(defaults_file, next_policy_number, basic_rate, discount_rate, liability_cost, glass_cost,
                      loaner_car_cost, hst_rate, processing_fee)

        done = input("Enter another policy? (Y/N): ").upper()
        if done != 'Y':
            break

    # After entering all policies, display the receipts for all customers
    with open(policies_file, 'r') as file:
        policies = file.readlines()

    print("\n===== RECEIPTS FOR ALL CUSTOMERS =====")
    for policy in policies:
        policy_data = policy.strip().split(", ")
        policy_number, invoice_date, first_name, last_name, address, city, province, postal_code, phone_number, \
            num_cars, extra_liability, glass_coverage, loaner_car, payment_method, total_cost = policy_data

        date_obj = datetime.datetime.strptime(invoice_date, "%Y-%m-%d")
        total_cost = float(total_cost)

        display_receipt(int(policy_number), date_obj, first_name, last_name, address, city, province, postal_code,
                        phone_number, int(num_cars), [extra_liability, glass_coverage, loaner_car], payment_method,
                        total_cost - processing_fee, total_cost, get_next_month(date_obj), hst_rate)


if __name__ == "__main__":
    main()
