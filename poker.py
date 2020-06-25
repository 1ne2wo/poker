#输入样例：（点数间，花色间用空格隔开）
#请分别输入white或black，点数，花色。
#white or black:white
#点数:9 10 j q k
#花色：s s s s s
#white or black:black
#点数:5 7 8 9 6
#花色:c c c c c
#white wins.
def poker(numbers,colors):
    new_numbers=[]
    numbers=numbers.split()
    colors=colors.split()
    k=0
    point=1
    key1=1
    key2=1

    for number in numbers:
        if number == 'j' or number == 'J':
            numbers[k] = '11'
        if number == 'q' or number == 'Q':
            numbers[k] =  '12'
        if number == 'k' or number == 'K':
            numbers[k] = '13'
        if number == 'a' or number == 'A':
            numbers[k] = '14'
        k+=1

    numbers = [ int(x) for x in numbers ]
    numbers = sorted(numbers,reverse=True)

    for i in range(4):
        if colors[i] != colors[i+1]:
            key1 = 0
        if numbers[i] != numbers[i+1]+1:
            key2 = 0

    if key1 == 1:
        point += 5

    if key2 == 1:
        point += 4
    p=len(list(set(numbers)))

    if p == 4:
        point+=1
    elif p == 3:
        point+=2
    elif p == 2:
        point+=3
    if point == 1 or point == 5 or point == 10:
        point+=0.01*numbers[0]

    return point
    

print('请分别输入white或black，点数，花色。')
side1 = input('white or black:')
numbers1 = input('点数: ')
colors1 = input('花色: ')
side2 = input('white or black:')
numbers2 = input('点数: ')
colors2 = input('花色: ')
point1 = poker(numbers1,colors1)
point2 = poker(numbers2,colors2)
if point1 > point2:
    win = 1
elif point1 < point2:
    win = 2
elif point1 == point2:
    win = 0
if win == 1:
    print(side1+' wins.')
elif win == 2:
    print(side2+' wins.')
elif win == 0:
    print('draw.')


