mydict = {
        'pani':'water',
        'machli':'fish',
        'ghut':'false',
        'kela':'banana',
        'mela':'fare'
}
print (f'You can select among this: {list(mydict.keys())}')
choice = input('Please Enter your choice : ')
print(f'The english word of {choice} is', mydict[choice])
