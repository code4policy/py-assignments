with open ('fayehenry.txt') as f:
	my_name = f.read()
message = "Hello, my name is " + my_name

print(message)

with open('output/hello.txt','w') as f:
	f.write(message)
	f.write('\n')