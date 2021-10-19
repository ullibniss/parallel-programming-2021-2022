import random

def array_gen(amount: int=10, size: int=10000000):
	
	for i in range(amount):
        	mas = [random.randint(0, 2147483647) for a in range(size)]
		mas_str = ''
		mas_str.join(mas)
        	with open(f"array{num}.txt", "w") as file:
			for el in mas:
                		file.write(f"{el} ")
			
if __name__ == '__main__':
	array_gen()
