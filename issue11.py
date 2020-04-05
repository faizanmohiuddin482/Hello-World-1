num = input("Enter the number:  ")
try:
    num = int(num)
    raise ValueError("Non numeric value")
    for i in range(0, num):
        print("hello world")
except:
	print("Sorry, that entry is invalid")
	
