chracter = {1:'male', 2:'female', 3:'stickman'}
chracterselect = int(input('Select your chracter:'))
if chracterselect == 1:
    print('You have selected male')
elif chracterselect == 2:
    print('You have selected female')
elif chracterselect == 3:
    print('You have selected stickman')
else:
    print('Invalid selection, try again')
