while True:
    string = input('Enter a string: (q to exit)')
    if string == 'q':
        break
    char = input('> ')
    count = 0
    for i in string.lower():
        if i == char:
            count += 1
    print(f'The amont of char is: {count}')
