import csv
with open('diff.csv', 'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    with open('diff.txt', 'r',encoding='utf-8') as filein:
        for line in filein:
            for i in range(len(line)):
              if (line[i]=='0')and(line[i-1]=='_'):
                print(line[:i-1])
                line_list = line[0:i-1].strip('\n').split('\t')
            #print(line)
                spamwriter.writerow(line_list)
                break
