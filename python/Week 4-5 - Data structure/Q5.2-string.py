#Find the longest word

string_1 = ["Happy", "cute", "pretty", "adorable", "funny", "kind", "dad", "sas", "aw", "q"]


max_len = 0
selected_string = ""
for s in string_1:
    if len(s) > max_len:
        max_len = len(s)
        selected_string = s

print("Longest string: ", selected_string, " with ", max_len, " characters")



#method 2: use sorted
#sorted_list = sorted(selected_list_strings, key=len, reverse=True)
#selected_string = sorted_list[0]
#print("Longest string: ", selected_string, " with ", len(selected_string), " characters")

