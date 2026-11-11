#Count the number of strings where the string length is 2 or more and the first and last character are same
string_1 = ["Happy", "cute", "pretty", "adorable", "funny", "kind", "dad", "sas", "aw", "q"]

selected_list_string = []

for i in  range(len(string_1)):
    if len(string_1[i]) >= 2:
        selected_list_string.append(string_1[i])
print("selected_list_string", selected_list_string)
