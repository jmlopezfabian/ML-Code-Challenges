def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	transpose = []
	
	for j in range(len(a[0])):
		aux = []
		for i in range(len(a)):
			aux.append(a[i][j])
		transpose.append(aux)
	return transpose