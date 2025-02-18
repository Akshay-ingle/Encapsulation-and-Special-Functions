class myClass:
    __privatevar=27;
    def __privMeth(self):
        print("'I'm inside class my Class")
    def hello(self):
        print('privat Variable value:',myClass.__privatevar)
foo=myClass()
foo.hello()
foo.__privMeth            