import pandas as pd
from datetime import datetime
from main import bhtg03Worksheet, bhtg03Collumns

def get_thang_nam(file_03):
    # noinspection PyTypeChecker
    data = pd.read_excel(file_03, sheet_name=bhtg03Worksheet, usecols=bhtg03Collumns)
    data_header = data.columns.values.tolist()
    first_col = data[data_header[0]] # first col that has thang_nam
    check_list = first_col.str.contains("năm", regex=False).tolist()
    thang_nam_loc = check_list.index(True)
    thang_nam = data[data_header[0]][thang_nam_loc]
    # thang_nam = data["QTD Nhân Dân Hồng Thành "][2]
    thang_nam = thang_nam.replace(' năm ', "/")
    return thang_nam


# def chuyển định dạng ngày tháng
def turn_to_month_year(date_string):
    date_obj = datetime.strptime(date_string, "%Y%m%d")
    formatted_date = f"tháng {date_obj.strftime('%m/%Y')}"
    return formatted_date