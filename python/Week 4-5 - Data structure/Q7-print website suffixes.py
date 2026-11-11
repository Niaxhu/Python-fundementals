#Given a sample list ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#Write a python program to print website suffixes (com , org , net ,in) from this list


webs = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

#for quick, i use list comprehension. You can use iteration

suffixes = [ w[w.rfind("."):] for w in webs]
print("Result: ", suffixes)

#you can improve the output by remove ".". I let you do it
# also, you can check if there is "." before extracting the data

#another way, you can use split() with "." as separator, then get the last value
#with this approach, you don't need to remove the "."
suffixes = [ w.split(".")[-1] for w in webs]
print("Result: ", suffixes)