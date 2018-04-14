import  csv
with open('file.csv','a',newline='') as file:
    filelds=('country','area')
    writer=csv.writer(file)
    writer.writerow(filelds)

    test=[(1,2321),(2,3211)]
    test.append()
    for i in test:
        writer  .writerow(i)
