
import copy, sys, random, pandas, csv, os

from pandas import DataFrame

validnum = []

for i in range(5000):

    card = str(random.randint(1000000000000000, 9999999999999999))

    new = list(card[-2::-2])

    plush = list(card[::-2])

    for i in range(len(new)):
        new[i] = (int(new[i])) * 2

    for i in range(len(new)):
        new[i] = str(new[i])

    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    brand = ''
    for ele in plush:
        brand += ele

    dead = ''
    for ele in plush:
        dead += ele

    blurp = list(listToString(new))

    death = 0
    for i in range(len(blurp)):
        death = int(blurp[i]) + death

    clock = copy.copy(list(brand))
    ben = 0
    for i in range(len(clock)):
        ben = ben + int(clock[i])

    kill = str(ben + death)

    if kill[-1] == '0':
        if card[0] == '4':
            validnum.append([card, 'Visa'])

        elif card[0] == '3' and (card[1] == '7' or card[1] == '4'):
            validnum.append([card, 'Amex'])

        elif card[0] == '5' and (card[1] == '1' or card[1] == '2' or card[1] == '3' or card[1] == '4' or card[1] == '5'):
            validnum.append([card, 'Mastercard'])

        else:
            pass
    else:
        pass


df = DataFrame(validnum, columns=['Number', 'Company'])
with open('crdtnums.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Company', 'Number'])
    for i in range(len(validnum)):
        company = validnum[i][0]
        number = validnum[i][1]
        filewriter.writerow([company, number])

print(df)

