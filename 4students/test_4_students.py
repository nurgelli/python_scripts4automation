welcome = input('Welcom, are you ready for the test (yes/no): ')

if welcome.lower() != 'yes' or 'y':
    print('Lets jump in!')
else:
    print('Maybe next time!')
    quit()