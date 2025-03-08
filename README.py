# 1. Handling value error Exception
try:
    num = int("hello")
except ValueError:
    print("Invalid input! Cannot convert to an integer.")
    
 # 2.  Handling file not found Error While Reading a File
try:
    with open("unknown.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  
    
 # 3. Handling Attribute Error
try:
    number = 10
    number.append(5)  # Integers don’t have an `append` method
except AttributeError as e:
    print(f"Attribute Error: {e}")
    
 # 4. Handling module not found error
try:
    import unknown_module
except ModuleNotFoundError:
    print("Module not found! Please install it first.")
    
 # 5. Handling keyboard interrupt User Presses Ctrl+C or Stops Execution)  

       
 # 6. Handling memory error (When System Runs Out of Memory)
try:
    big_list = [1] * (10**10)  # Trying to create a very large list
except MemoryError:
    print("Memory limit exceeded!") 
           
 # 7. Handling recursion Error (Too Many Recursive Calls)  
def infinite_recursion():
    return infinite_recursion()

try:
    infinite_recursion()
except RecursionError:
    print("Recursion depth exceeded!")  
    
 # 8. Handling name error (Using Undefined Variables) 
try:
    print(unknown_variable)
except NameError:
    print("Variable is not defined!")   
    
 # 9. Handling restrictions error (trying to Access Restricted Files)
try:
    with open("/root/secret.txt", "r") as f:
        content = f.read()
except PermissionError:
    print("Permission denied! You don’t have access to this file.")  
    
 # 10. Handling stop iteration in Iterators
my_iter = iter([1, 2, 3])

try:
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))  # This will cause StopIteration
except StopIteration:
    print("No more elements in the iterator!")
