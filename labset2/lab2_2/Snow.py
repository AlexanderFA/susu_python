class Snow:
    flakes: int = 0

    def __add__(self, amount: int) -> int:
        self.flakes += amount
        return self.flakes

    def __sub__(self, amount: int) -> int:
        self.flakes -= amount
        return self.flakes

    def __mul__(self, amount: int) -> int:
        self.flakes *= amount
        return self.flakes

    def __truediv__(self, amount: int) -> int:
        self.flakes = round(self.flakes / amount)
        return self.flakes

    def make_snow(self, amount: int) -> None:
        print(amount * ('*' * self.flakes + '\n'))

    def __call__(self, amount: int = 0) -> None:
        self.flakes = amount
        print('Now snowflakes amount is', self.flakes)
