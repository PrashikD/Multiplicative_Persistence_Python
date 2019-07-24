def diamonds(rows):
    i = 1
    j = 0
    space = " "
    star = "*"
    while i <= rows:
        print(space*(rows - i) + star*(2*i-1))
        i += 1



diamonds(6)


