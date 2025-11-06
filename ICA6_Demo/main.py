class Dud:
    def __str__(self):
        return "Monoxide du carbon"
    def __repr__(self):
        return "Fire! Feu!"


dud = Dud()
print(dud)

class Nums:
    num = 3 #class variable, effectively static (C#)
    numbers = [1,2,3,4]
    x,y,z = 0,0,0

num_a = Nums()
num_b = Nums()

print(num_a.num)
num_a.num += 3  # makes an instance member,
                # and then adds 3 to the class member,
                # storing it to the instance member
print(num_a.num)
print(Nums.num) #access using the name of the class so that it's clear

#READ access looks locally for an instance first, then looks at the class
num_a.y = 67
print(num_a.y)
print(num_b.y)

class FncNums:
    num = 3
    def fnc(Wyatt):
        print(f"num = {Wyatt.num}")
        Wyatt.num = 9
        num = 12 #local variable
    def gnc (self, other, thing):
        print(f"{self} : {self.num}")
    def instanceMethod(self, name):
        FncNums.num += 1
        self.newName = name
        print(f'Instance Method : FncNums.num = {FncNums.num}, name = {self.newName}')
    @classmethod
    def class_method(cls, name):
        cls.num += 1
        FncNums.num += 1
        #self.NewName = name NO SE PUEDE! (you can't do this!)
        print(f'Class method: cls = {cls}, cls.num = {cls.num}, name = {name}')

    @staticmethod
    def staticMethod(name): #NO ACCESS TO CLASS MEMBERS; NO ACCESS TO INSTANCE MBRS
        print(f"Can we at least call FuncNums.num? {FncNums.num}")
nums = FncNums()
nums.fnc()
nums.gnc(2 , 99)
nums.instanceMethod("CMPE2850")
nums.staticMethod("Hello")
FncNums.staticMethod("Goodbye")
FncNums.class_method("Bonjour")
FncNums.instanceMethod(nums,"Au Revoir")

class Nums:
    count = 0
    static_nums = []
    mynum = 8
    def __eq__(self,other): #does this automatically override the !=??
        return Nums.mynum == other.mynum
    def __init__(self, initValue = 0):
        self.instance_member = initValue
        self.nums = [x for x in range(0,10)]
        self.nums[4] = -32
        Nums.count += 1

class Gums :
    nums = [1,2,3]
    mynum = 8
    def __init__(self, start = 20):
        self.nums = list(range(start, start + 10))

class Thumbs (Gums, Nums):
    def __init__(self):
        super().__init__(55)

th = Thumbs()
print(th.nums)

a = Nums()
a.nums[4] += 99
print(a.nums)

b = Gums()
print(b.nums)

c = Gums(40)
print(c.nums)
print(Gums.nums)

print(a==c)
print(a!=c)