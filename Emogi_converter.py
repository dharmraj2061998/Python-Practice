message = input("> ")
words =message.split(" ")

emojis = {
    ":)":"đ", 
    ":(":"âšī¸"
    }
output =""
for word in words:
    output += emojis.get(word,word) + " "
print(output)