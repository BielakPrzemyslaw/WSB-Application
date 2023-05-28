import win32com.client
import subprocess
import time
import sys
import os
import shutil
from datetime import datetime
from excell_file import close_excel_file
import sap_transaction


user = os.getenv('SAP_USER')
password = os.getenv('SAP_STARS')
now = datetime.now()
dt_string = now.strftime("%Y%m%d %H%M")
filename = dt_string + ".XLSX"

class SapGui():

    def __init__(self):
        self.path = r"C:/Program Files (x86)/SAP/FrontEnd/SAPgui/saplogon.exe"
        subprocess.Popen(self.path)
        time.sleep(5)

        self.SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not type(self.SapGuiAuto)== win32com.client.CDispatch:
            return

        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.OpenConnection(sap_transaction.open_connection, True)
        time.sleep(3)
        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").iconify()
        self.session.findById("wnd[0]").maximize()

        self.sapLogin()


    def sapLogin(self):

        try:
           #LOGIN SAP
           self.session.findById("wnd[0]").maximize()
           self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = sap_transaction.open_session
           self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = user
           time.sleep(5)
           self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password
           time.sleep(5)
           self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "EN"
           self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
           self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = 11
           self.session.findById("wnd[0]").sendVKey(0)
           self.session.findById("wnd[1]/usr/btnBUTTON_1").press()

        except:
            print(sys.exc_info()[0])



    def excelExport(self, part_name):

        try:

            self.session.findById("wnd[0]").maximize()
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "cewb"
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[1]/usr/ctxtCWB_WORKAREA-WORK_AREA").text = "UTAS ROUTING"
            self.session.findById("wnd[1]/usr/ctxtCWB_WORKAREA-WORK_AREA").caretPosition = 12
            self.session.findById("wnd[1]").sendVKey(0)
            self.session.findById(
                "wnd[0]/usr/subSELECTION_CRITERIA:SAPLCPSC:1300/ctxtMTK_CLASS_SEL-MATNR").text = part_name
            self.session.findById(
                "wnd[0]/usr/subSELECTION_CRITERIA:SAPLCPSC:1300/ctxtMTK_CLASS_SEL-WERKS").text = "2760"
            self.session.findById("wnd[0]").sendVKey(30)
            self.session.findById("wnd[0]").sendVKey(86)

            self.session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[1]").select()
            self.session.findById("wnd[1]/usr/cmbG_LISTBOX").setFocus()
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "Routing " + part_name + ".XLSX"
            self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
            self.session.findById("wnd[1]").sendVKey(0)
            self.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            self.session.findById("wnd[0]/tbar[0]/btn[15]").press()
            self.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
            time.sleep(3)
            close_excel_file()

        except:
            print(sys.exc_info()[0])

    def copyCut_excel_file(self, routing_path):
        dir1 = 'C:/Users/' + os.getlogin() + '/Documents/SAP/SAP GUI/'
        dir2 = routing_path + "/"

        for files in os.listdir(dir1):
            shutil.move(dir1 + files, dir2 + files)

        return



    def operation_OOTF(self, traveler):

         try:

             self.session.findById("wnd[0]").maximize
             self.session.findById("wnd[0]/tbar[0]/okcd").text = "CO02"
             self.session.findById("wnd[0]").sendVKey(0)
             self.session.findById("wnd[0]/usr/ctxtCAUFVD-AUFNR").text = traveler
             self.session.findById("wnd[0]/usr/ctxtCAUFVD-AUFNR").caretPosition = 9
             self.session.findById("wnd[0]").sendVKey(0)
             self.session.findById("wnd[0]/tbar[1]/btn[5]").press()
             self.session.findById("wnd[0]/tbar[1]/btn[40]").press()
             self.session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[1]").select()
             self.session.findById("wnd[1]").sendVKey(0)
             self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = traveler + ".XLSX"
             self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
             self.session.findById("wnd[1]").sendVKey(0)
             self.session.findById("wnd[0]").sendVKey(15)
             self.session.findById("wnd[0]").sendVKey(15)
             self.session.findById("wnd[0]").sendVKey(15)
             time.sleep(3)
             close_excel_file()

         except:
            print(sys.exc_info()[0])

    def copyCut_traveler_file(self, traveler_path):
        dir1 = 'C:/Users/' + os.getlogin() + '/Documents/SAP/SAP GUI/'
        dir2 = traveler_path + "/"

        for file2 in os.listdir(dir1):
            shutil.move(dir1 + file2, dir2 + file2)

        return








