import random
import string

# List of example user names
usernames = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"]

# Email domains
email_domains = ["gmail.com", "yahoo.com"]

# Street names
streets = ["Baker Street", "Elm Street", "Maple Street", "Pine Street"]

# Cities
cities = ["Springfield", "Shelbyville", "Ogdenville", "North Haverbrook"]

# Function to generate random strings
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate realistic email addresses
def generate_realistic_email(name, email_set):
    while True:
        domain = random.choice(email_domains)
        email = name.lower() + '.' + generate_random_string(5) + "@" + domain
        if email not in email_set:
            email_set.add(email)
            return email

# Function to generate realistic order IDs
def generate_realistic_order_id(name, order_id_set):
    while True:
        order_id = name[:3].upper() + str(random.randint(100, 999)) + '-' + generate_random_string(2).upper()
        if order_id not in order_id_set:
            order_id_set.add(order_id)
            return order_id

# Function to generate realistic addresses
def generate_realistic_address(name, address_set):
    while True:
        street = random.choice(streets) + ' ' + str(random.randint(1, 100))
        city = random.choice(cities)
        zipcode = str(random.randint(10000, 99999))
        address = f"{name},{street},{city},{zipcode}"
        if address not in address_set:
            address_set.add(address)
            return address

# Open files for writing
with open("user_emails.csv", "w") as email_file, open("user_orders.csv", "w") as order_file, open("user_addresses.csv", "w") as address_file:
    # Sets to store used emails, order_ids, and addresses to ensure uniqueness
    used_emails = set()
    used_order_ids = set()
    used_addresses = set()
    
    # Generate 1000 entries
    for _ in range(1000):
        username = random.choice(usernames)
        email = generate_realistic_email(username, used_emails)
        order_id = generate_realistic_order_id(username, used_order_ids)
        address = generate_realistic_address(username, used_addresses)
        
        # Write data to files
        email_file.write(f"{username},{email}\n")
        order_file.write(f"{username},{order_id}\n")
        address_file.write(f"{address}\n")

print("User emails, orders, and addresses generated successfully!")
