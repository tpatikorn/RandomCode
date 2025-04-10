from difflib import SequenceMatcher


def similar_ratio(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()


station_list = ["บางซื่อ", "บางแค", "หัวลำโพง", "ห้วยขาแข้ง", "บ้านผ่านฟ้า", "แยกหน้าวัด", "หมอชิด",
                "ลำปาง", "เชียงใหม่", "เชียงใหม่", "บางประม้า", "บางทีก็ไป", "บางทีก็ไม่ไป", "บางกอก"]

if __name__ == "__main__":  # declare main function python-style
    while True:
        station = input("ไปสถานีไหน")
        ratios = list(filter((lambda t: t[1] > 0.5),
                             map(lambda s: (s, similar_ratio(s, station)),
                                 station_list)))
        ratios.sort(reverse=True, key=lambda t: t[1])
        if len(ratios) > 0 and ratios[0][1] == 1.00:
            print("จองไป", station, "สำเร็จ")
        elif station == 'สถานี':
            print("รายชื่อสถานีทั้งหมด", station_list)
        elif len(ratios) == 0:
            print("ไม่พบสถานีใกล้เคียง กรุณาลองใหม่ หรือพิมพ์ 'สถานี' เพื่อดูราชื่อสถานี")
        else:
            print("พบสถานีที่ใกล้เคียง: ", list(map(lambda x: "{} ({:.2f}%)".format(x[0], x[1] * 100), ratios)))
