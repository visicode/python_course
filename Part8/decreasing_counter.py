# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.orig = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value>0:
            self.value-=1

    def set_to_zero(self):
        self.value=0

    def reset_original_value(self):
        self.value=self.orig
        
# Write the rest of the methods here!

if __name__ == '__main__':
    print("Part1:")
    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()

    print("Part2:")
    counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()

    print("Part3:")
    counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value()

    print("Part4:")
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()