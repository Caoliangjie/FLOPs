import csv
with open('diff_val.csv', 'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    with open('diff_val.txt', 'r',encoding='utf-8') as filein:
        for line in filein:
            for i in range(len(line)):
              if (line[i]=='.'):
                print(line[:i-1])
                line_list = line[0:i-1].strip('\n').split('\t')
            #print(line)
                spamwriter.writerow(line_list)
                break
