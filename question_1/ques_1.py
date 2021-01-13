import json
import numpy as np

input_list = []

size = int(input("Enter the number of elements"))

for i in range(0,size):
    ele = input()
    
    input_list.append(ele)

print (input_list)

temp_list = []

for i in range(0,size):
    if (input_list[i].isdigit() == True):
            x = int(input_list[i])
            
            temp_list.append(x)
    
#print (temp_list)

output_list = []

for i in range(0, len(temp_list)):
    if (temp_list[i] > 0):
        x = temp_list[i]

        output_list.append(x)
        
output_list.sort()
#print(output_list)
average = np.mean(output_list)

output_dict = {"valid_entries": len(output_list),
                "invalid_entries": len(input_list)-len(output_list),
                "min":output_list[0],
                "max":output_list[-1],
                "average":average}


#print (output_dict)

j = json.dumps(output_dict, indent=2)
print(j)
