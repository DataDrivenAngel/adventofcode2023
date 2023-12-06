text = open("4.txt",'r')
data = text.read().split('\n')

## day 1
total = 0
for enumer, line in enumerate(data):
    card = line.split(':')[1]
    numbers,winners = card.split('|')
    numbers = numbers.strip()
    winners = winners.strip()
    numbers = numbers.replace('  ',' ').split(' ')
    winners = winners.replace('  ',' ').split(' ')
    numbers = [int(n) for n in numbers]
    winners = [int(w) for w in winners]

    win_count = 0
    for n in numbers:
        if n in winners:
            win_count = win_count + 1
    if win_count == 1:
        points = 1
        total = total + points
    
    elif win_count > 1:
        points = 2**(win_count-1)
        total = total + points
print(total)

## 24175 is correct


