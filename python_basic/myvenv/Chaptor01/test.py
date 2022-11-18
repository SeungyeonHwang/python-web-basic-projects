import random

# 부모 Class
class Monster:
    max_num = 1000

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"[{self.name}]지상에서 이동하기")


# 자식 Class
class Wolf(Monster):
    pass  # 정의만 하고 싶을 때 사용


class Shark(Monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기")


class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불 뿜기", "꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0, 2)]}")


wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
dragon.skill()
