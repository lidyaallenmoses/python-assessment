start =int(input("enter start number: \t"))
end =int(input("enter end number: \t"))
for n in range(start,end+1):
	if n % 2 ==0:
		print("even number",n )
	else:
		print("odd number",n)
