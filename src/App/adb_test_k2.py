import os

if __name__ == '__main__':

    # record this execute dir.
    original_path = os.getcwd()
    print("project dir :",  original_path)

    # get and change to directory of adb tool inside this project
    parent_path = os.path.abspath("..")
    adb_dir = os.path.join(parent_path, 'platform-tools')
    os.chdir(adb_dir)

    # execute adb cmd
    adb = 'adb devices'
    os.system(adb)

    os.system("pause")