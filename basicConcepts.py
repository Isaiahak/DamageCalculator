# Python Cheat Sheet

## Basics:

### Comments:
# Single-line comment
"""
Multi-line comment
"""

### Variables and Data Types:
variable_name = 10
integer_var = 10
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True

### Print:
print("Hello, World!")

### Input:
user_input = input("Enter something: ")

## Control Flow:

### Conditionals:
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if no conditions are True

### Loops:
for item in iterable:
    # code to execute for each item

while condition:
    # code to execute while condition is True

## Functions:

### Defining Functions:
def my_function(parameter1, parameter2):
    # code here
    return result

### Calling Functions:
result = my_function(arg1, arg2)

## Data Structures:

### Lists:
my_list = [1, 2, 3, 4, 5]
element = my_list[0]
sublist = my_list[1:3]
my_list.append(6)
my_list.remove(3)

### Dictionaries:
my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict['key1']
my_dict['key3'] = 'value3'
del my_dict['key2']

## File Handling:

### Reading from a File:
with open('filename.txt', 'r') as file:
    content = file.read()

### Writing to a File:
with open('filename.txt', 'w') as file:
    file.write('Hello, File!')

## Exception Handling:

### Try-Except Blocks:
try:
    # code that might raise an exception
except SomeException as e:
    # handle the exception

## Modules and Libraries:

### Importing Modules:
import os
current_directory = os.getcwd()

## Advanced Concepts:

### Asynchronous Programming:

#### Async/Await:
import asyncio

async def my_async_function():
    # asynchronous code here
    result = await async_operation()
    return result

async def async_operation():
    # asynchronous operation
    return result

# Run an asynchronous function
asyncio.run(my_async_function())

#### aiohttp for HTTP Requests:
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# Example usage
html_content = asyncio.run(fetch_url('https://example.com'))
print(html_content)

### Multithreading and Multiprocessing:

#### Threading:
import threading

def my_thread_function():
    # code to run in the thread

# Create a thread
my_thread = threading.Thread(target=my_thread_function)

# Start the thread
my_thread.start()

# Wait for the thread to finish
my_thread.join()

#### Multiprocessing:
import multiprocessing

def my_process_function():
    # code to run in the process

# Create a process
my_process = multiprocessing.Process(target=my_process_function)

# Start the process
my_process.start()

# Wait for the process to finish
my_process.join()

### Decorators:

#### Function Decorator:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # code before the function
        result = func(*args, **kwargs)
        # code after the function
        return result
    return wrapper

@my_decorator
def my_decorated_function():
    # original function code

#### Class Decorator:
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # code before the function
        result = self.func(*args, **kwargs)
        # code after the function
        return result

@MyDecorator
def my_decorated_function():
    # original function code

### Context Managers:

#### Custom Context Manager:
class MyContextManager:
    def __enter__(self):
        # code to run when entering the context
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # code to run when exiting the context
        pass

# Usage
with MyContextManager() as my_object:
    # code within the context

#### Using Contextlib:
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # code to run when entering the context
    yield
    # code to run when exiting the context

# Usage
with my_context_manager():
    # code within the context