custom_string = 'X-MAPDS-Confidence:0.8475' 

at_index = custom_string.find(':')
extracted_string = custom_string[at_index + 1:]
output = float(extracted_string)
print(type(output))
print(output)