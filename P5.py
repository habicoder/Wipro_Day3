values=0
try:
	f=open('.//abc.txt','r')
	content=f.readlines()
	for line in content:
		values+=float(line.split(':')[1])
	f.close()
except Exception:
	print('Unable to open the file')
print(values)