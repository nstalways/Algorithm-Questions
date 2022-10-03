data_list = []

while True:
    data = list(map(int, input().split()))

    if sum(data) == 0:
        break
    else:
        data_list.append(data)

def checkFactorOrMultiple(val_list):
    a = val_list[0]
    b = val_list[1]

    if (b % a) == 0:
        print('factor')
    else:
        if (a % b) == 0:
            print('multiple')
        else:
            print('neither')

for data in data_list:
    checkFactorOrMultiple(data)