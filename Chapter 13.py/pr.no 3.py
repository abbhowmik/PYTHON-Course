try:

    l = [str(i*7) for i in range(1, 11)]
    print(l)
    vertical = '\n'.join(l)
    print(vertical)
except Exception as e:
    print(e)
