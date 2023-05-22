import pyperclip

str = input("paste the string of the leetcode title here: ")
str = str.replace(". ", "_")
str = str.replace(" ", "-")
if str[-3:] != ".py":
    str += ".py"

print("Your new str has been copied.")
print(str)
pyperclip.copy(str)