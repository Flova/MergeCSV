import csv
import pprint
import sys
import tkinter as tk
from tkinter import filedialog


def read_csv(path,data,start):
    print("----- Start reading " + path + " -----")
    raw = open(path, 'r', encoding = 'ISO-8859-1')
    content = csv.DictReader(raw, delimiter=';')
    headers = content.fieldnames
    b_save = False
    if(start == None):
        b_save = True
    for row in content:
        if (start == row and b_save == False):
            b_save = True
            continue
        if (b_save == True):
            #print(str(row) + "\n")
            data.append(row)
    print("----- Finished reading " + path + " -----\n")
    return (data, headers)


def run():
    root = tk.Tk()
    # file_path = ["foo1.csv","foo.csv"]
    files = filedialog.askopenfilenames(parent=root,title='Choose a file')
    file_path = root.tk.splitlist(files)
    last_line = None
    data = []
    headers = []
    for path in file_path:
        (data, headers) = read_csv(path, data, last_line)
        last_line = data[-1]
    output_path = filedialog.asksaveasfilename(parent=root,title='Save the File')
    out_file  = open(output_path, "w")
    writer = csv.DictWriter(out_file, fieldnames=headers, delimiter=';')
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    print(data)
    print(len(data))

if __name__ == '__main__':
    run()
