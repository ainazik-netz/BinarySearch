
fill = []
for i in range(200):
    fill.append(i)
fill.sort()
print(fill)
number = int(input('Enter required number,please: '))
low = 0
high = len(fill) 
mid = (low + high)//2
while low < high and mid != number:
    if number > mid:
        low = mid + 1
    else:
        high = mid - 1
if mid == number:
    print('Not found')
else:     
    print('Required number is',id)




