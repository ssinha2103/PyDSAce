### Control Flow Statements

Control flow statements are used to manage the flow of execution in a program. They allow you to execute certain code blocks based on conditions or repeat them a specific number of times.

#### If, Else, and Elif

```python
x = 42

if x > 50:
    print("x is greater than 50")
elif x == 42:
    print("x is equal to 42")
else:
    print("x is less than or equal to 50")
```

#### While Loop

```python
counter = 0

while counter < 5:
    print(f"Counter: {counter}")
    counter += 1
```

#### For Loop

```python
for i in range(5):
    print(f"Index: {i}")
```

You can also use a for loop to iterate over the elements of a list, tuple, or other iterable objects:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"Fruit: {fruit}")
```

#### Nested Loops

You can nest loops inside other loops:

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

#### Break and Continue

`break` and `continue` statements can be used to control the flow inside loops.

```python
for i in range(10):
    if i == 5:
        break  # Stop the loop when i is 5
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

These are the basic control flow statements in Python. They allow you to manage the execution of your code based on conditions and loops. For more information, please refer to the official Python documentation.
