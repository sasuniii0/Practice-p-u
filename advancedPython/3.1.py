class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add (a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("this is the utility class for MathUtils")

a = MathUtils
print(a.add(4,6))
a.description()

MathUtils.description()
print(MathUtils.add(9,4))