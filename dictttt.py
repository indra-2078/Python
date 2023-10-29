# # importing the module
import ast
  
# reading the data from the file
with open('new.txt') as f:
    data = f.readline()
    print(str(data))
    data = (data.replace("}{",","))
    print(data)
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Data type after reconstruction : ", type(d))
a = print(d)
b = d['my name']
print(b)
