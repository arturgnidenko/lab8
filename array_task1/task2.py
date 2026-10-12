import numpy as np

matrix = np.random.randint(0, 31, size=(3, 3))
print("Вихідний масив 3х3:")
print(matrix)

modified_matrix = matrix * 2 + matrix
print("\nМасив після перемноження на 2 і додавання вихідного:")
print(modified_matrix)

corners = [
    modified_matrix[0, 0],   # верхній лівий
    modified_matrix[0, -1],  # верхній правий
    modified_matrix[-1, 0],  # нижній лівий
    modified_matrix[-1, -1]  # нижній правий
]

product = np.prod(corners)
print(f"\nДобуток елементів у кутах масиву: {product}")
