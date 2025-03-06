# Open and read the entire content
f = open('data.txt', 'r')
read_data = f.read()
print("Reading the entire file as a string:")
print(read_data)
f.close()

# Open and read file into a list of lines
f = open('data.txt', 'r')
method1 = list(f)
f.close()
print("\nReading file into a list (Method 1):")
print(method1)

f = open('data.txt', 'r')
method2 = f.readlines()
f.close()
print("\nReading file into a list (Method 2):")
print(method2)
