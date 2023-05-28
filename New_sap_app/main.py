from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox)

import sys
from sap import SapGui
from nx_standard import NxStandard
from simi_update import SimiUpdate
from ui_main2 import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Automation of standardized tasks")



        #SYSTEM PAGES
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_sap.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sap))
        self.btn_simi.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_simi))
        self.btn_nx.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_nx))

        self.btn_select.clicked.connect(self.open_file)

        #LOGIN IN SAP SYSTEM
        self.btn_login.clicked.connect(self.login_sap)

        #Export routing excel file
        self.btn_export.clicked.connect(self.routing_export)

        #Export traveler excel file
        self.btn_export_traveler.clicked.connect(self.traveler_export)
        self.btn_select_traveler.clicked.connect(self.select_path)

        #SIMI
        self.btn_simi_update_operation.clicked.connect(self.update_operation)

        #NX2206 UPDATE
        self.btn_select_2.clicked.connect(self.select_nx_path)
        self.btn_update_template.clicked.connect(self.update_template)


    def open_file(self):
        self.file = QFileDialog.getExistingDirectory(self, "Select folder")
        self.txt_file.setText(self.file)

    def select_path(self):
        self.traveler = QFileDialog.getExistingDirectory(self, "Select folder")
        self.txt_file_traveler.setText(self.traveler)

    def select_nx_path(self):
        self.update_nx_file = QFileDialog.getExistingDirectory(self, "Select folder")
        self.txt_nx_file.setText(self.update_nx_file)

    def update_template(self):
        self.nx_standard = NxStandard()

        nx_path = self.txt_nx_file.text()
        self.nx_standard.copy_nx_file(nx_path)

    def login_sap(self):
        self.sap = SapGui()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("login")
        msg.setText("Login Successfully")
        msg.exec_()

    def routing_export(self):
        part_name = self.txt_part_name.text()
        routing_path = self.txt_file.text()
        self.sap.excelExport(part_name)
        self.sap.copyCut_excel_file(routing_path)

    def traveler_export(self):
        traveler = self.txt_part_traveler.text()
        traveler_path = self.txt_file_traveler.text()
        self.sap.operation_OOTF(traveler)
        self.sap.copyCut_traveler_file(traveler_path)

    def update_operation(self):
        self.simi_update = SimiUpdate()
        operation_number = self.txt_simi_operation_number.text()
        operation_description = self.txt_simi_operation_name.text()
        work_center = self.txt_simi_operation_wc.text()
        part_number = self.txt_simi_part_number.text()
        operation_revision = self.txt_simi_operation_rev.text()
        self.simi_update.simi_operation(operation_number, operation_description, work_center, part_number, operation_revision)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

















