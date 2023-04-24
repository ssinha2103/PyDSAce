### Functions and Function Arguments

Functions are reusable pieces of code that perform a specific task. They allow you to modularize your code and improve its readability and maintainability.

#### Defining a Function

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

#### Function with a Return Value

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
```

#### Default Argument Values

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # Output: 9 (exponent defaults to 2)
print(power(3, 3))  # Output: 27 (exponent is set to 3)
```

#### Keyword Arguments

```python
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(age=30, name="Alice")
```

#### Arbitrary Number of Arguments

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

#### Arbitrary Number of Keyword Arguments

```python
def print_key_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(a=1, b=2, c=3)
```