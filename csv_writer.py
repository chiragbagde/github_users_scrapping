import os
import csv


def initialize_workbook():
    path = "E:\\django-supermind-assignment\\github_users.csv"
    fields = ['Name', 'github', 'Description',
              'location', 'github url', 'email']
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


def csv_writer(List):
    path = "E:\\django-supermind-assignment\\github_users.csv"
    if not (os.path.exists('github_users.csv')):
        initialize_workbook()
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(List)


if __name__ == "__main__":
    print("Writing to CSV")
    print("Finished writing to CSV")
