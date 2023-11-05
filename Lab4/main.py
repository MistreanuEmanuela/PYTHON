# 1 stack
from copy import copy

print("-------------------------------------``1``---------------------------------------------------")


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, x):
        self.stack_list.append(x)

    def pop(self):
        if len(self.stack_list) != 0:
            value = self.stack_list[-1]
            self.stack_list = self.stack_list[:-1]
            return value
        else:
            return None

    def peek(self):
        if len(self.stack_list) != 0:
            value = copy(self.stack_list[-1])
            return value
        else:
            return None

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        return False

    def size(self):
        return len(self.stack_list)

    def __str__(self):
        queue_str = ""
        for item in self.stack_list:
            queue_str += str(item) + " "
        return queue_str


my_stack1 = Stack()
print("Pop stack1:", my_stack1.pop())
print("Peek stack1:", my_stack1.peek())
my_stack1.push(1)
print("stack1", my_stack1)
print("Peek stack1:", my_stack1.peek())
my_stack2 = Stack()
my_stack2.push(5)
my_stack1.push(2)
my_stack1.push(3)
my_stack1.push(4)
print("stack1", my_stack1)
print("stack2", my_stack2)
print("Pop stack1:", my_stack1.pop())
print("Pop stack1:", my_stack1.pop())
print("Peek stack2:", my_stack2.peek())
print("stack1", my_stack1)
print("stack2", my_stack2)
print(my_stack2.is_empty())
print(my_stack2.size())
my_stack2.pop()
print("stack2:", my_stack2)
print(my_stack2.is_empty())


print("-------------------------------------``2``---------------------------------------------------")


# 2. Queue


class Queue:
    def __init__(self):
        self.queue_list = []

    def push(self, x):
        self.queue_list.append(x)

    def pop(self):
        if len(self.queue_list) != 0:
            value = self.queue_list[0]
            self.queue_list = self.queue_list[1:]
            return value
        else:
            return None

    def peek(self):
        if len(self.queue_list) != 0:
            value = copy(self.queue_list[0])
            return value
        else:
            return None

    def is_empty(self):
        if len(self.queue_list) == 0:
            return True
        return False

    def size(self):
        return len(self.queue_list)

    def __str__(self):
        queue_str = ""
        for item in self.queue_list:
            queue_str += str(item) + " "
        return queue_str


my_q1 = Queue()
print("Pop q1:", my_q1.pop())
print("Peek q1:", my_q1.peek())
my_q1.push([1, 1])
print("Peek q1:", my_q1.peek())
peek_q1 = my_q1.peek()
peek_q1.append(2)
print(peek_q1)
print("Peek q1:", my_q1.peek())
my_q2 = Queue()
my_q2.push(5)
my_q1.push(2)
my_q1.push(3)
my_q1.push(4)
print("q1: ", my_q1)
print("q2: ", my_q2)
print("Pop q1:", my_q1.pop())
print("Pop q1:", my_q1.pop())
print("Peek q2:", my_q2.peek())
print("q2: ", my_q2)
print(my_q2.is_empty())
print(my_q2.size())
my_q2.pop()
print(my_q2.is_empty())

print("-------------------------------------``3``---------------------------------------------------")


class Matrix:
    def __init__(self, n, m):
        if n > 0 and m > 0:
            self.rows = n
            self.columns = m
            self.matrix = [[0 for _ in range(m)] for _ in range(n)]
        else:
            raise Exception("matrix should have a positive size")

    def set(self, i, j, x):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            self.matrix[i][j] = x
        elif i < 0 or i >= self.rows:
            raise Exception(f"index i = {i} out of bounds")
        elif j < 0 or j >= self.columns:
            raise Exception(f"index j = {j} out of bounds")

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            return self.matrix[i][j]
        elif i < 0 or i >= self.rows:
            raise Exception(f"index i = {i} out of bounds")
        elif j < 0 or j >= self.columns:
            raise Exception(f"index j = {j} out of bounds")

    def transpose(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i in range(self.columns):
            for j in range(self.rows):
                new_matrix[i][j] = self.matrix[j][i]
        return new_matrix

    def multiply(self, other_matrix):
        if self.columns != other_matrix.rows:
            raise Exception("You can multiply these two matrix, be careful with the sizes.")
        multiply_matrix = [[0 for _ in range(other_matrix.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                for k in range(other_matrix.columns):
                    multiply_matrix[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
        return multiply_matrix

    def transformation(self, lambda_funct):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = lambda_funct(self.matrix[i][j])

    def __str__(self):
        matrix_str = ""
        for i in range(self.rows):
            matrix_str += str(self.matrix[i]) + "\n"
        return matrix_str


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Matrix1:")
print(matrix)

transposed_matrix = matrix.transpose()
print("Transposed Matrix1:")
print(transposed_matrix)

matrix2 = Matrix(3, 3)
matrix2.set(0, 0, 1)
matrix2.set(0, 1, 2)
matrix2.set(0, 2, 3)
matrix2.set(1, 0, 4)
matrix2.set(1, 1, 5)
matrix2.set(1, 2, 6)
matrix2.set(2, 0, 7)
matrix2.set(2, 1, 8)
matrix2.set(2, 2, 9)

print("Matrix2:")
print(matrix2)

matrix_p = matrix.multiply(matrix2)
print("Matrix Result:")
print(matrix_p)

matrix.transformation(lambda x: x-2)
print("Transformed Matrix:")
print(matrix)