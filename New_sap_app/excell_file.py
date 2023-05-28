import win32com.client as win32
import os
import shutil


def close_excel_file():

    excel = win32.Dispatch('Excel.Application')
    excel.Workbooks.Close()
    excel.Application.Quit()
    return close_excel_file




