import os
import numpy as np
from PIL import Image


def read_scan(fn, no_images, window_h, scan_len):
    dir_name = fn.replace('.OCT', '')
    os.mkdir(dir_name)

    I = []

    try:
        with open(fn, 'rb') as fid:
            for i in range(no_images):
                data = np.fromfile(fid, dtype=np.float32, count=window_h * scan_len)
                I.append(data.reshape((scan_len, window_h)))

        minimum = 650
        for nr_skanu in range(no_images):
            b1 = I[nr_skanu]
            maximum = np.max(b1)

            b1 = 255 * ((b1 - minimum) / (maximum - minimum))
            b1[b1 < 0] = 0
            b1 = np.uint8(b1)
            I1 = np.flipud(b1.T)

            if nr_skanu > 99:
                przedrostek = str(nr_skanu)
            elif nr_skanu > 9:
                przedrostek = f"0{nr_skanu}"
            else:
                przedrostek = f"00{nr_skanu}"

            nazwapliku = f"Skan_nr_{przedrostek}.jpg"
            Image.fromarray(I1).save(os.path.join(dir_name, nazwapliku))
        # messagebox.showinfo("Info", "Process completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        # messagebox.showerror("Error", f"An error occurred: {e}")
