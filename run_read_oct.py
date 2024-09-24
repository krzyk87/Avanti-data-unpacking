import glob
import os
from read_scan_type import read_scan


def list_dir(dirpath):
    for f in sorted(glob.glob(os.path.join(dirpath, "*/*.oct"))):
        yield f


data_dir = '../DATA/AVANTI_DOMINIKA'
image_list = list(list_dir(data_dir))

if __name__ == '__main__':
    for file_path in image_list:
        print(f'Unpacking: {file_path}')
        if "3D Retina" in file_path:
            read_scan(file_path, no_images=144, window_h=640, scan_len=385)
        elif "Raster" in file_path:
            read_scan(file_path, no_images=21, window_h=768, scan_len=1020)
        elif "Retina Map" in file_path:
            read_scan(file_path, no_images=13, window_h=640, scan_len=803)
        elif "Cross Line" in file_path:
            read_scan(file_path, no_images=4, window_h=768, scan_len=1020)
        elif "Line" in file_path:
            read_scan(file_path, no_images=2, window_h=960, scan_len=1020)
        else:
            print(f"Unknown scan type! {file_path}")
