# C:\Users\user\Anaconda3\Scripts\ipython
import csv

def read_data(file_name):
    file_name_to_read = file_name
    f = open(file_name_to_read,'r',encoding='utf-8')
    csv_reader = csv.reader(f)
    list_of_row = []
    for row in csv_reader:
        list_of_row.append(row)
    return(list_of_row[1:]) # change to [1:] if want to have every rows

data = read_data("modified3.csv") # type your name of the file
data_length = len(data)

replace_bed_numbers = []
for i in range(data_length):
    if int(data[i][-1]) >= 5:
        replace_bed_numbers += ['5+']
    else:
        replace_bed_numbers += [data[i][-1]]

replace_bedroom_numbers = []
for i in range(data_length):
    if int(data[i][-2]) >= 4:
        replace_bedroom_numbers += ['4+']
    else:
        replace_bedroom_numbers += [data[i][-2]]

replace_bathroom_numbers = []
for i in range(data_length):
    if int(data[i][-3]) >= 4:
        replace_bathroom_numbers += ['4+']
    else:
        replace_bathroom_numbers += [data[i][-3]]

f = open('modified4.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['bathrooms','bedrooms','beds'])
for i in range(data_length):
    wr.writerow([replace_bathroom_numbers[i],replace_bedroom_numbers[i],replace_bed_numbers[i]])
f.close()