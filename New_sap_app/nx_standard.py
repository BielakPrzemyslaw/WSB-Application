import os
import shutil
import distutils.dir_util


class NxStandard():

    def copy_nx_file(self, nx_path):
        dir1 = 'G:/DL/LT/NX/NX2206/'
        dir2 = nx_path + "/"

        for files in os.listdir(dir1):
            if os.path.isfile(files):
                shutil.copytree(dir1 + files, dir2 + files)


        return

