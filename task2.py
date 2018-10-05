def crime_list(s):              
	f=open(s,"r")
	g=dict()
	o=dict()
	list1=[]
	list2=[]
	for line in s:
		line.strip()
		for lines in line.split(','):
			list1.append(lines[-1])
			list2.append(lines[-2])
	for a in list1:
		if a not in g:
			g[a]=1
		else:
			g[a]=d[a]+1
	for m in list2:
		if m not in o:
			o[m]=1
		else:
			o[m]+=1
	print("crime name",' '*15,"crimeid",' '*15,"crimecount")
	for b,c in g.items():
		for d,c in o.items():
			print(b,d,c, "\n")
file="Crime.csv"
crime_list(file)

