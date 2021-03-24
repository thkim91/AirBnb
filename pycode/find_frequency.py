import csv

def read_data(file_name):
    file_name_to_read = file_name
    f = open(file_name_to_read,'r',encoding='utf-8')
    csv_reader = csv.reader(f)
    list_of_row = []
    for row in csv_reader:
        list_of_row.append(row)
    return(list_of_row[1:])

data = read_data("modified_AirBnb.csv") # type your name of the file
data_length = len(data)

price_pool = {'3.36 or less':0,'4.42 or less':0,'5.48 or less':0, '6.54 or less':0, 'more than 6.54':0}
overall = {'3.36 or less':0,'4.42 or less':0,'5.48 or less':0, '6.54 or less':0, 'more than 6.54':0}
for i in range(data_length):
    price = float(data[i][0])
    yes_or_no = int(data[i][15])

    if price <= 3.36:
        overall['3.36 or less'] += 1 
        if yes_or_no == 1:
            price_pool['3.36 or less'] += 1
    elif price <= 4.42:
        overall['4.42 or less'] += 1
        if yes_or_no == 1:
            price_pool['4.42 or less'] += 1
    elif price <= 5.48:
        overall['5.48 or less'] += 1
        if yes_or_no == 1:
            price_pool['5.48 or less'] += 1
    elif price <= 6.5:
        overall['6.54 or less'] += 1
        if yes_or_no == 1:
            price_pool['6.54 or less'] += 1
    else:
        overall['more than 6.54'] += 1
        if yes_or_no == 1:
            price_pool['more than 6.54'] += 1

answer = []
for i in range(len(overall)):
    answer.append([list(overall.keys())[i], list(price_pool.values())[i],list(overall.values())[i]])

f = open('find_frequency_gym.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['price','gym_number','overall_number'])
for i in range(len(overall)):
    wr.writerow(answer[i])
f.close()

