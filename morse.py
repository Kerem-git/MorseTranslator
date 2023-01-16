import json

with open("morse.json","r") as f:
	json = json.load(f)

choice = input("""
##############################

https://github.com/Kerem-git

##############################

[1] encoding
[2] decoding


""")


text = input("text: ").lower()
tlist = []

def encode():
	for char in text:
		if char == " ":
			tlist.append("/")
		elif True:
			tlist.append(json[char])
		else:
			print("unexcepted character.")
	print(" ".join(tlist))


def decode():
	txt = text.split(" ")
	for char in txt:
		#print(char)
		if char == "/":
			tlist.append(" ")
		else:
			for elem in json:

				if json[elem] == char:
					tlist.append(elem)

	print("".join(tlist))



if choice == "1":
	encode()
elif choice == "2":
	decode()
else:
	exit()
