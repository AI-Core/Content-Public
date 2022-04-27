class A:
    
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        print("I am class A")

    def multiply(self):
        return self.Name + self.Age

class B(A):
    
    def __init__(self):
        super().__init__("Blair")
        print("I am class B")

    def sum(self):
       return super().multiply(3, 4)
        

class C(A):
    
    def __init__(self):
        super().__init__()
        print("I am class C")

    def sum(self, a, b, c):
        return a + b + c

class D(B, C):
    
    def __init__(self):
        super().__init__()
        print("I am class D")



class_A_1 = A(23, 15)
print(class_A_1.multiply())

