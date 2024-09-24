import glob
import os
import shutil


def list_scans_oct(dirpath):
    for f in sorted(glob.glob(os.path.join(dirpath, "*/*.oct"))):
        yield f


def list_scans_dir(dirpath):
    for f in sorted(glob.glob(os.path.join(dirpath, "*/*"))):
        if os.path.isdir(f):
            yield f


def copy_central(scan_path):
    scan_name = os.path.split(scan_path)[-1]
    central_no = 0
    if "3D Retina" in scan_name:
        central_no = round(141/2)
    elif "Raster" in scan_name:
        central_no = round(21/2)
    elif "Retina Map" in scan_name:
        central_no = round(13/2)
    elif "Cross Line" in scan_name:
        central_no = 0
    elif "Line" in scan_name:
        central_no = 0
    else:
        print(f"Unknown scan type! {scan_name}")

    if central_no > 9:
        nn = f"0{central_no}"
    else:
        nn = f"00{central_no}"

    file_name = os.path.join(scan_path, f"Skan_nr_{nn}.jpg")
    new_file_name = scan_path + f"_Skan_nr_{nn}.jpg"
    print(new_file_name)
    shutil.copy(file_name, new_file_name)
