import json

filename = 'müll2022.txt'

dict1 = []

fields = ['tag', 'date', 'name']
datefields = ['day', 'month', 'year']

with open(filename, encoding='utf-8') as file:
    for line in file:
        if line.__contains__('.2022'):
            description = list(line.strip().replace(",", " ").split(None, 3))

            i = 0
            dict2 = {}
            dict3 ={}
            while i < len(fields):
                dates = description[1].split(".")
                dict3[datefields[i]] = dates[i]

                dict2[fields[i]] = description[i]
                dict2[fields[1]] = dict3
                i = i + 1
            dict1.append(dict2)

out_file = open("müll.json", 'w')
json.dump(dict1, out_file, indent=3)
out_file.close()
