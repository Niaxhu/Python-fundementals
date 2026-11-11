
#Given a string containing letters and digits, extract only the digit characters.Example: text = "Room 446ZC, Building QM, Floor 4"
# Note: you can use the string method isdigit() on each character. Or check each character if belong to
# a list of ‘0’,..,’9’

text = "Room 446ZC, Building QM, Floor 4"
selected_chars = ""

for c in text:
    if c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        selected_chars = selected_chars + c
print(selected_chars)

#method 2
#selected_chars = ""
#for c in s:
    #if c >= '0' and c <= '9':
        #selected_chars = selected_chars + c