class Alpha:
    def process(self):
        print("Alpha processed")

class Beta(Alpha):
    def process(self):
        print("Beta processed")

class Gamma(Alpha):
    def process(self):
        print("Gamma processed")

class Delta(Beta, Gamma):
    pass

d = Delta()

d.process()

Beta.process(d)
Gamma.process(d)
Alpha.process(d)
