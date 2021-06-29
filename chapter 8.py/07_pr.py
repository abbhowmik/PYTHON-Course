# this = "      Harry is a good boy        "
# print(this)
# print(this.strip())

def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()


the = "    Harry is a good boy and also a good coder    "
n = remove_and_split(the, "Harry")
print(n)
