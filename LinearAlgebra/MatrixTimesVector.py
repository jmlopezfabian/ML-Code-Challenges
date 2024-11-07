def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	
	ans = []
	
	for row in a:
		acum = 0
		for j in range(len(row)):
			acum += row[j] * b[j]
		ans.append(acum)
	return ans