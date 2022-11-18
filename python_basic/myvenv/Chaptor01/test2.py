class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] 판매 -> 판매가격 : [{self.price}]")

    def discard(self):
        if self.isdropable:
            print(f"[{self.name} 버리기]")
        else:
            print(f"[{self.name} 버리기 불가능]")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}] 착용 {self.effect}")


class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}] 사용 {self.effect}")
