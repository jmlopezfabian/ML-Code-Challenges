import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		matrix_np = np.array(matrix).T
	else:
		matrix_np = np.array(matrix)
	means = [matrix_np[i].mean() for i in range(0, len(matrix_np))]
	return means