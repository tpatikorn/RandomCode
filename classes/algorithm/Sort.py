def bubble_sort(array):
    swap = False
    while not swap:
        print(array)
        for i in range(0, len(array) - 1):  # len-2 = ตัวรองสุดท้าย
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                swap = True
            print(array)
        print()
        # ทำซ้ำจนกว่าจะไม่มีการสลับเลย


# แบ่ง list เป็น 2 ช่วง: sorted กับ unsorted
# เริ่ม: ตัวแรกของ list อยู่ใน sorted ที่เหลือ unsorted
# วนซ้ำ n-1 ครั้ง
#   เลือกตัวแรกของ unsorted
#   แทรกตัวแรกลงใน sorted ให้ถูกที่ถูกลำดับ

# i=1 number = array[1] = 3 step1  [5| 3, 4, 1, 4, 6, 7, 1, 2, 7, 3]
# i=2 number = array[2] = 4 step1  [3, 5| 4, 1, 4, 6, 7, 1, 2, 7, 3]
# i=3 number = array[3] = 1 step1  [3, 4, 5| 1, 4, 6, 7, 1, 2, 7, 3]
# i=3 number = array[3] = 1 step1  [3, 4, 1, 5| 4, 6, 7, 1, 2, 7, 3]
# i=3 number = array[3] = 1 step2  [3, 1, 4, 5| 4, 6, 7, 1, 2, 7, 3]
# i=3 number = array[3] = 1 step3  [1, 3, 4, 5| 4, 6, 7, 1, 2, 7, 3]
# i=4 number = array[4] = 4 step1  [1, 3, 4, 5| 4, 6, 7, 1, 2, 7, 3]
# i=4 number = array[4] = 4 step1  [1, 3, 4, 4, 5| 6, 7, 1, 2, 7, 3]
def insertion_sort(array):
    for i in range(1, len(array)):
        number = array[i]
        j = i - 1
        print(array)
        while j >= 0:
            if number < array[j]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
            elif number >= array[j]:
                break
            j = j - 1
        print()


def selection_sort(array):
    pass


input_array1 = [5, 3, 4, 1, 5, 6, 7, 1, 2, 7, 3]
bubble_sort(input_array1)
print(input_array1)

input_array2 = [5, 3, 4, 1, 5, 6, 7, 1, 2, 7, 3]
insertion_sort(input_array2)
print(input_array2)

input_array3 = [5, 3, 4, 1, 5, 6, 7, 1, 2, 7, 3]
selection_sort(input_array3)
print(input_array3)

input_array4 = [5, 3, 4, 1, 5, 6, 7, 1, 2, 7, 3]
input_array4.sort()
print("444", input_array4)
