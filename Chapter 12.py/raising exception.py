def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('Your entered value is not valid')


a = increment('4')
print(a)
