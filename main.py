# Data taken from https://www.x-rates.com/table/?from=AUD&amount=1

# Reading raw data from .txt file
with open('currencyData_28012021.txt') as file:
    raw_data = file.readlines()

# Defining a currency dictionary
currencyDictionary = {}

# Parsing data to get required fields
for row in raw_data:
    parsed_data = row.split("\t")
    currencyDictionary[parsed_data[0]] = parsed_data[1]

# User input for amount
user_data_in = int(input("Enter amount: "))

# Displaying all currencies
print("Currency options:")
[print(item) for item in currencyDictionary.keys()]

# Prompting user to enter exact currency name
currency = input("\nPlease select a currency from the above list: ")

# Converted currency
print(f"{user_data_in} AUD is equal to {user_data_in * float(currencyDictionary[currency])} {currency}")