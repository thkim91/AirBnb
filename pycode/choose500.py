import csv
import random

def read_data(file_name):
    file_name_to_read = file_name
    f = open(file_name_to_read,'r',encoding='utf-8')
    csv_reader = csv.reader(f)
    list_of_row = []
    for row in csv_reader:
        list_of_row.append(row)
    return(list_of_row[:]) # change to [1:] if want to have every rows

data = read_data("modified3-2.csv") # type your name of the file
   
group_of_items = data[1:]         
num_to_select = 500                           
list_of_random_items = random.sample(group_of_items, num_to_select)

f = open('choose500-1.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(data[0])
for i in range(len(list_of_random_items)):
    wr.writerow(list_of_random_items[i])
f.close()