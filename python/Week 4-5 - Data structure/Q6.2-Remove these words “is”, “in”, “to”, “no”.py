#you can improve the output by removing "No"

text = ["Life is beautiful", "No need to overthink", "Meditation help in overcoming depression"]

selected_words = []

selected_words = [w for s in text for w in s.split() if w.lower() not in ["is", "in", "to", "no"]]

print("Words: ", selected_words)
