print("Hello, World!")

my_student_id = 1231241251232
my_first_name = "first_name"
my_last_name = "last_name"


# body mass index = BMI
# BMI = weight(kg) / (height(m)**2)

class Fighter:  # rename
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_BMI(self):
        return self.weight / (self.height ** 2)

    def print_self_info(self):
        print("Name:", self.name)
        print("Age:", self.age, "Years old")
        print("Height:", self.height, "m")
        print("Weight:", self.weight, "kg")
        print("BMI:", self.calculate_BMI())

    # new
    def get_power(self):
        return (self.weight * self.height) / 100 + 1234567890  # เลขหลักหน่วยของรหัส นศ

    @staticmethod
    def fight(fighter1, fighter2):
        if fighter1.get_power() > fighter2.get_power():
            print(fighter1.name, "wins")
        elif fighter1.get_power() < fighter2.get_power():
            print(fighter2.name, "wins")
        else:
            print("Draw")


# new
class Mage(Fighter):
    def __init__(self, name, age, weight, height, magic):
        super().__init__(name, age, weight, height)
        self.magic = magic

    def get_power(self):
        fighter_power = super().get_power()
        mage_power = (self.magic / 100) * (9876543210 + 1)  # เลขหลักสิบของรหัส นศ
        if mage_power > fighter_power:
            return mage_power
        else:
            return fighter_power


f1 = Fighter("Captain America", 45, 76.2, 1.75)
f1.print_self_info()

f2 = Mage("Dr. Strange", 47, 64.3, 1.70, 200)
print(f1.get_power())
print(f2.get_power())
Fighter.fight(f1, f2)

fighters = {
    "fA": Fighter("A", 52.33, 81.89, 1.66),
    "fB": Fighter("B", 68.80, 46.46, 1.89),
    "fC": Fighter("C", 31.64, 119.79, 1.67),
    "fD": Fighter("D", 71.09, 64.93, 1.43),
    "fE": Fighter("E", 47.40, 65.52, 1.69),
    "fF": Fighter("F", 54.11, 137.20, 1.81),
    "fG": Fighter("G", 95.35, 83.55, 1.45),
    "fH": Fighter("H", 30.44, 121.15, 1.75),
    "fI": Fighter("I", 26.89, 67.98, 1.90),
    "fJ": Fighter("J", 64.47, 137.36, 1.40)
}
