def is_uppercase(inp):
    checker = True
    for i in inp:
        if i == i.upper():
            continue
        elif i != i.upper():
            checker = False
    return checker