class X:
    def execute(self):
        print("X executed")

class Y:
    def execute(self):
        print("Y executed")

class Z(X, Y):
    def execute(self):
        print("Z executed")

class Final(Z):
    def run(self):
        self.execute()

# Create an object of Final and call run()
f = Final()
f.run()
