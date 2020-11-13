class MyClass(object):
    def __init__(self, string="", num=0):
        self.__num = num
        self.__string = str(string)

    def num(self):
        return self.__num

    def string(self):
        return  self.__string

    def set_num(self, num):
        self.__num = num

    def set_string(self, string):
        self.__string = string

    def __str__(self):
        return 'MyClass ({}, "{}")'.format(self.__num, self.__string)


a = MyClass("aaaaaaa", 4)
print(a.num())
print(a.string())
a.set_num(29)
a.set_string("asdf")
print(a)
