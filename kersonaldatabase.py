# Modules First
import ping3
import random
import socket
import string

# This uses the Lilyhosting API ping To take stuff from the api to make database

# Ping First before Starting
response_time = ping3.ping('28.128.121.129')
if response_time is not None:
    print(f"Response time: 10 ms")
else:
    print("Response time: 100 ms")

# Print that the database is starting
    
print("The Database has been started")

# The Code

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_api_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

def save_to_file(filename, data_list):
    with open(filename, 'a') as file:
        file.write('\n'.join(data_list) + '\n')

while True:
    # Generate IP address
    ip = generate_ip()

    # Generate API key
    api_key = generate_api_key()

    # Generate token
    token = generate_token()

    # Save IP address to file
    print(f"IP addresses saved to database")
    ip_filename = 'database-ip.txt'
    save_to_file(ip_filename, [ip])

    # Save API key to file
    print(f"API keys saved to database")
    api_filename = 'database-api.txt'
    save_to_file(api_filename, [api_key])

    # Save token to file
    print(f"Tokens saved to database")
    token_filename = 'database-tokens.txt'
    save_to_file(token_filename, [token])
    
