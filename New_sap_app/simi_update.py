from csv import DictWriter
from datetime import datetime
import os
from pathlib import Path
import distutils.dir_util



class SimiUpdate():

    def simi_operation(self, operation_number, operation_description, work_center, part_number, operation_revision):

        # finding last folder
        rootdir = "C:/Users/bielakp/Desktop/Simi_import/Import/"

        last_subfolder = sorted(Path(rootdir).iterdir(), key=os.path.getatime)
        last_subfolder = os.listdir(rootdir)[-1]
        print(last_subfolder)
        # Create new folder
        today = datetime.now()
        year = today.strftime('%Y')
        month = today.strftime('%m')
        day = today.strftime('%d')

        update_folder = (year + '-' + month + '-' + day)
        os.mkdir("C:/Users/bielakp/Desktop/Simi_import/Import/" + update_folder)

        # copy file
        src = r"C:/Users/bielakp/Desktop/Simi_import/Import/" + last_subfolder
        dst = r"C:/Users/bielakp/Desktop/Simi_import/Import/" + update_folder
        distutils.dir_util.copy_tree(src, dst)
        print(update_folder)


        try:
        #Check row number
            rowcount  = 0
            for row in open(r"C:\Users\bielakp\Desktop\Simi_import\Import\{up}\import_operacje.csv".format(up = update_folder)):
                rowcount+= 1
            print("Number of lines present:-", rowcount)

            #Update
            field_names = ['operacja',
                    'nazwa',
                    'stanowisko',
                    'pn',
                    'licznik',
                    'zaklad',
                    'sekwencja',
                    'typ_marszruty',
                    'klucz_grupy_marszrut',
                    'numer_zmiany',
                        'data_ostatniej_zmiany',]

            operation = operation_number
            operation_name = operation_description
            station = work_center
            pn = part_number
            rev_op = operation_revision
            convert_rev = f'{rev_op}'

            dict = {'operacja' : operation,
                    'nazwa' : operation_name,
                    'stanowisko' : station,
                    'pn' : pn,
                    'licznik' : '0',
                    'zaklad' : 'HSW',
                    'sekwencja' : '0',
                    'typ_marszruty' : 'N',
                    'klucz_grupy_marszrut' : '0',
                    'numer_zmiany' : '0',
                    'data_ostatniej_zmiany' : convert_rev + ',,' }

            with open(r'C:\Users\bielakp\Desktop\Simi_import\Import\{up}\import_operacje.csv'.format(up = update_folder), 'a', newline='') as f_object:

                dictwriter_object = DictWriter(f_object, fieldnames=field_names, delimiter=';')

                dictwriter_object.writerow(dict)

                f_object.close()

        except:
            print("Next time")



