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

data = read_data("modified1.csv") # type your name of the file
data_length = len(data)

is_it_there = []
for i in range(data_length):
    elements = (data[i][6].split(','))
    each_result = []

    if 'Pool' in elements:
        each_result += [1]
    else:
        each_result += [0]
    
    if 'Hot tub' in elements:
        each_result += [1]
    else:
        each_result += [0]

    if 'Free parking on premises' in elements:
        each_result += [1]
    else:
        each_result += [0]

    if 'Gym' in elements:
        each_result += [1]
    else:
        each_result += [0]
    
    is_it_there.append(each_result)
    
# f = open('modified2.csv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f)
# wr.writerow(['pool','hot tub','parking','gym'])
# for i in range(data_length):
#     wr.writerow(is_it_there[i])
# f.close()