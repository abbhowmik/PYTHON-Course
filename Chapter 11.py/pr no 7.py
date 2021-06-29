class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        a = ""
        index = 0
        for i in self.vec:
            a += f'{i} a{index} +'
            index += 1
        return a[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        b = 0
        for i in range(len(self.vec)):
            b += self.vec[i] * vec2.vec[i]
        return b

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 4, 5])
v2 = Vector([1, 2, 3])
print(len(v1))
print(len(v2)
