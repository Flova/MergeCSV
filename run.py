import csv
import datetime
import tkinter as tk
import json
from tkinter import filedialog


def read_csv(path):
    print("----- Start reading " + path + " -----")
    data = set()
    raw = open(path, 'r', encoding = 'ISO 8859-1')
    if input("Neue Version? (y/n):") == "y":
        for i in range(12):
            raw.readline()
    content = csv.DictReader(raw, delimiter=';')
    headers = content.fieldnames
    for row in content:
        if row['Kundenreferenz'] not in ["Anfangssaldo","Endsaldo"]:
            data.add(json.dumps(row))
    print("----- Finished reading " + path + " -----\n")
    return data, headers


def merge_csv(file_path):
    data = set()
    headers = []
    for path in file_path:
        (data_tmp, headers) = read_csv(path)
        data = data.union(data_tmp)
    raw_list = []
    for data_set in data:
        raw_list.append(json.loads(data_set))
    return raw_list, headers


def sort(list):
    return sorted(list, key=lambda k: datetime.datetime.strptime(k['Buchungstag'], '%d.%m.%Y'))


def run():
    root = tk.Tk()
    # file_path = ["foo1.csv","foo.csv"]
    files = filedialog.askopenfilenames(parent=root,title='Choose a file')
    file_path = root.tk.splitlist(files)
    # Main Function
    (raw_list, headers) = merge_csv(file_path)
    # Sort by Date
    output_list = sort(raw_list)
    output_path = filedialog.asksaveasfilename(parent=root,title='Save the File')
    # output_path = "csv1lol.csv"
    out_file  = open(output_path, "w")
    writer = csv.DictWriter(out_file, fieldnames=headers, delimiter=';')
    writer.writeheader()
    for row in output_list:
        writer.writerow(row)
    # pprint.pprint(output_list)
    print("Datasets in final Dokument: " + str(len(output_list)))


if __name__ == '__main__':
    run()
