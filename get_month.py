import pandas as pd


def get_thang_nam(file_03):
    # noinspection PyTypeChecker
    data = pd.read_excel(file_03, sheet_name="Sheet1", usecols="A,E:G,J")
    data_header = data.columns.values.tolist()
    first_col = data[data_header[0]] # first col that has thang_nam
    check_list = first_col.str.contains("năm", regex=False).tolist()
    thang_nam_loc = check_list.index(True)
    thang_nam = data[data_header[0]][thang_nam_loc]
    # thang_nam = data["QTD Nhân Dân Hồng Thành "][2]
    thang_nam = thang_nam.replace(' năm ', "/")
    return thang_nam
