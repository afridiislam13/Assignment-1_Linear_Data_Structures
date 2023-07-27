# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

# Example usage:
array = [2, 4, 3, 6, 8, 9, 7, 1]
target = 10
result = find_pairs_with_sum(array, target)

print("Pairs with sum", target, "are:")
for pair in result:
    print(pair)

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

try:
    arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
    reverse_array_in_place(arr)
    print("Reversed Array:", arr)
except ValueError:
    print("Invalid input. Please enter integers separated by space.")

# Q3. Write a program to check if two strings are a rotation of each other?

def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_rotations(string1, string2):
    print("The two strings are rotations of each other.")
else:
    print("The two strings are not rotations of each other.")

# Q4. Write a program to print the first non-repeated character from a string?

def find_first_non_repeated_char(input_string):
    char_frequency = {}

    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    for char in input_string:
        if char_frequency[char] == 1:
            return char
    return None

input_str = input("Enter a string: ")
first_non_repeated_char = find_first_non_repeated_char(input_str)

if first_non_repeated_char is not None:
    print(f"The first non-repeated character is: {first_non_repeated_char}")
else:
    print("There are no non-repeated characters in the string.")

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

num_disks = int(input("Enter the number of disks: "))
tower_of_hanoi(num_disks, 'A', 'B', 'C')

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(postfix_expression):
    stack = []
    for char in postfix_expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = char + operand1 + operand2
            stack.append(prefix_expression)
    return stack.pop()

postfix_expression = input("Enter the postfix expression: ")
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)

# Q7. Write a program to convert prefix expression to infix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expression):
    stack = []
    for char in reversed(prefix_expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f"({operand1}{char}{operand2})"
            stack.append(infix_expression)
    return stack.pop()

prefix_expression = input("Enter the prefix expression: ")
infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)

# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code_snippet):
    stack = []
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in code_snippet:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    return len(stack) == 0

code_snippet = input("Enter the code snippet: ")
if are_brackets_closed(code_snippet):
    print("All brackets are properly closed.")
else:
    print("Brackets are not closed properly in the code snippet.")

# Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        item = stack.pop()
        aux_stack.push(item)

    while not aux_stack.is_empty():
        item = aux_stack.pop()
        stack.push(item)

# Test the program
stack = Stack()
elements = input("Enter elements for the stack separated by space: ").split()
for element in elements:
    stack.push(element)
print("Original Stack:", stack.items)
reverse_stack(stack)
print("Reversed Stack:", stack.items)

# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = Stack()
elements = list(map(int, input("Enter elements for the stack separated by space: ").split()))
for element in elements:
    stack.push(element)
print("Smallest number in the stack:", stack.get_min())

