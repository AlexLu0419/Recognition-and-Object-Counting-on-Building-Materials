import os
import csv
from PIL import Image

root = '.'
directory = ['big', 'medium', 'small']
total_data = []

for name in directory:
    data = []

    for i in range(7):
        n = i + 1
        

        try:
            image_list = os.listdir(f'{root}/dataset/{n}/{name}')
        except:
            continue

        for im in image_list:
            try:
                im_c = Image.open(f'{root}/dataset/{n}/{name}/{im}')
                temp = [f'dataset/{n}/{name}/{im}', n]
                data.append(temp)
            except:
                continue
            
    total_data += data

    for d in data:
        print(d)

    with open(f'{root}/dataset_{name}.csv', 'w') as csvfile:
        w = csv.writer(csvfile)
        for r in data:
            w.writerow(r)
            print(r)

with open(f'{root}/dataset_total.csv', 'w') as csvfile:
    w = csv.writer(csvfile)
    for r in total_data:
        w.writerow(r)
        print(r)