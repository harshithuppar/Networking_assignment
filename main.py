import requests
import time
from tabulate import tabulate

subdomains = ['docs.google.com', 'calendar.google.com', 'sheets.google.com']

def check_status(subdomain):
    url = f'http://{subdomain}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return 'Up'
        else:
            return f'Down ({response.status_code})'
    except requests.ConnectionError:
        return 'Down (Connection Error)'
    except requests.Timeout:
        return 'Down (Timeout)'

def display_status_table():
    table_data = []
    for subdomain in subdomains:
        status = check_status(subdomain)
        table_data.append([subdomain, status])

    headers = ['Subdomain', 'Status']
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

def main():
    while True:
        display_status_table()
        print("Checking status...")

        # Wait for 1 minute before the next check
        time.sleep(60)  

if __name__ == "__main__":
    main()
