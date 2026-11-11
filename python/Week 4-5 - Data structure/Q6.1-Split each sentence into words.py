text = ["Life is beautiful", "No need to overthink", "Meditation help in overcoming depression"]

selected_words = []
#Method 1: can use iteration
for s in text:
    parts = s.split()
    for p in parts:
        if p not in ["is", "in", "to", "no"]:
            selected_words.append(p)


print("Words: ", selected_words)

#Method 2: list comprehension
#selected_words = [w for s in text for w in s.split() if w not in ["is", "in", "to", "no"]]

#print("Words: ", selected_words)


