#!/usr/bin/python3


import requests, csv

data = requests.get("https://jsonplaceholder.typicode.com/posts")
json_data = data.json()

def fetch_and_print_posts():
    print(data.status_code)

    for dict in json_data:
        print(dict["title"])

def fetch_and_save_posts():
    new_data = [{key:value for key, value in dicts.items() if key != "userId"} for dicts in json_data]
    with open("posts.csv","w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file,fieldsnames = new_data[0].keys())

