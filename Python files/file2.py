
# file2.py
from file1 import MyClass

def main():
    # Create an instance of MyClass
    obj = MyClass("John")

    # Call the greet method
    greeting = obj.greet()

    # Print the result
    print(greeting)

if __name__ == "__main__":
    main()
