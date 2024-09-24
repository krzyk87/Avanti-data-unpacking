from utils import *

data_dir = '../DATA/AVANTI_DOMINIKA'
scan_list = list(list_scans_dir(data_dir))

for scan_path in scan_list:
    copy_central(scan_path)
