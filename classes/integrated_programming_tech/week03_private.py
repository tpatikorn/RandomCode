# public = ใครก็ใช้ได้ = นอก class เข้าถึงได้
# private = เฉพาะ "เรา" เข้าถึงได้ = เรียกใช้ได้เฉพาะจากใน class, นอก class ใช้ไม่ได้
# protected = คุ้มครอง เฉพาะผู้ได้รับอนุญาติ = เรียกใช้ได้เฉพาะจากใน class และ class ลูกหลาน, นอกนั้นใช้ไม่ได้

# scope

class Calculator2:
    def __init__(self, brand, year):
        self.__set_name__(brand, year)

    def __set_name__(self, brand, year):
        self.name = str(brand) + str(year)

    @staticmethod
    def plus(num1, num2):
        return num1 + num2

    @staticmethod
    def mult(num1, num2):
        return num1 * num2

Calculator2.mult(5,4)

calc = Calculator2("RMUTSB", "2022")
calc.__set_name__("MARCH", "2021")
print(calc.name)