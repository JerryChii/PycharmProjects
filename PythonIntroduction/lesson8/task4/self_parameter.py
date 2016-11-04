class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current = self.current + amount

    def get_current(self):
        return self.current

com = Complex()
com.create(1, 2)
#must call create first
print com.i

cal = Calculator()
print cal.get_current()
