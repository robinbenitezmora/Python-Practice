import csv

import requests

status_dict = {'Website': 'Status'}

def main():
    with open('websites.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            website = row[0]
            response = requests.get(website)
            status = 'Up' if response.status_code == 200 else 'Down'
            status_dict[website] = status

    with open('websites_status.csv', 'w') as file:
        writer = csv.writer(file)
        for key, value in status_dict.items():
            writer.writerow([key, value])

if __name__ == '__main__':
    main()
    