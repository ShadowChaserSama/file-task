def add(name,score):
	if not name in data:
		with open('data.txt','a') as f:
			f.write(f'{name} {score} \n')

data = ''
with open('data.txt','r') as f:
			data = f.read()

print("""
1 - add
2 - show
3 - task2
""")

ch = int(input())
if ch == 1:
		name = input()
		score = input()
		add(name,score)
elif ch == 2:	
		names = data.split('\n')

		for i in names:
				x = i.split()
				L = sorted(x,key=lambda a : a[1])
				print(L)
elif ch == 3:
		names = data.split('\n')

		for i in names:
				x = i.split()
				for j in x:
					if 'm' in j:
						print(x)
