month = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
year = ('2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025')
list_key = []
for y in year:
    for m in month:
        key = f"Tháng {m}/{y}"
        list_key.append(key)


class MakeList:
    def __init__(self, month, mkh, type):
        self.month = month
        self.mkh = mkh
        self.type = type

    @staticmethod
    def starm_endm(startm, endm):
        return list_key[list_key.index(startm):list_key.index(endm)+1]


list_hdqt_5vdl=[
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.01.00021"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.06.00510"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.01.00084"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.01.00033"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.11.00965"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 01/2020", "Tháng 12/2022"), ["TV.07.00579"], "hdqt_bgd_bks"),
    MakeList(MakeList.starm_endm("Tháng 02/2020", "Tháng 01/2021"), ["TV.11.00955"], "5_vdl")
]