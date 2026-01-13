# Write your solution here

def read_input(mes: str,bl: int,bh: int)->int:
    while True:
        try:
            input_str = input(mes)
            number = int(input_str)
            if bl <= number <= bh:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print(f"You must type in an integer between {bl} and {bh}")

