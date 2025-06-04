import os
from os import listdir, path, rename, mkdir
import shutil

groups = ["train", "test"]
classes = ["C_OFF", "C_ON", "F_OFF", "F_ON"]


def create_subfolder(image_path):
    for g in groups:
        if not path.exists(path.join(image_path, g)):
            mkdir(path.join(image_path, g))
        for c in classes:
            if not path.exists(path.join(image_path, g, c)):
                mkdir(path.join(image_path, g, c))
            if not path.exists(path.join(image_path, g, c)):
                mkdir(path.join(image_path, g, c))


def mass_move_folder(src, dst):
    for file_name in listdir(src):
        if file_name.endswith(".jpg"):
            rename(path.join(src, file_name),
                   path.join(dst, file_name))
            if file_name.endswith("201.jpg"):
                print(file_name)
    print("done")


def mass_move_subfolder(image_path):
    for t in groups:
        for file_name in listdir(path.join(image_path, t)):
            if file_name.endswith(".jpg"):
                rename(path.join(image_path, t, file_name),
                       path.join(image_path, t,
                                 file_name[0:file_name.index("_", 3)],
                                 file_name))
                if file_name.endswith("201.jpg"):
                    print(file_name)
    print("done")


def mass_copy(src_path, dst_path):
    create_subfolder(dst_path)
    for g in groups:
        for c in classes:
            for file_name in listdir(path.join(src_path, g, c)):
                if int(file_name[-8:-4]) % 30 == 0:  # every second
                    shutil.copyfile(path.join(src_path, g, c, file_name),
                                    path.join(dst_path, g, c, file_name))
                    print(file_name)
    print("done")

if __name__ == "__main__":
    # this_image_path = "/ac_vids/extracted_images"
    # mass_move_subfolder(this_image_path)

    src_image_path = "H:/My Drive/Projects/ac_vids/extracted_images"
    dst_image_path = "H:/My Drive/Projects/ac_vids/extracted_images_sec"
    # mass_copy(src_image_path, dst_image_path)

    mass_move_folder("H:/My Drive/Projects/ac_vids/extracted_images/train/C_OFF",
                     "H:/My Drive/Projects/ac_vids/extracted_images/train/F_OFF")
    mass_move_folder("H:/My Drive/Projects/ac_vids/extracted_images/train/C_ON",
                     "H:/My Drive/Projects/ac_vids/extracted_images/train/F_ON")

    os.rename("H:/My Drive/Projects/ac_vids/extracted_images/train/F_ON",
              "H:/My Drive/Projects/ac_vids/extracted_images/train/ON")
    os.rename("H:/My Drive/Projects/ac_vids/extracted_images/train/F_OFF",
              "H:/My Drive/Projects/ac_vids/extracted_images/train/OFF")

    mass_move_folder("H:/My Drive/Projects/ac_vids/extracted_images/test/C_OFF",
                     "H:/My Drive/Projects/ac_vids/extracted_images/test/F_OFF")
    mass_move_folder("H:/My Drive/Projects/ac_vids/extracted_images/test/C_ON",
                     "H:/My Drive/Projects/ac_vids/extracted_images/test/F_ON")

    os.rename("H:/My Drive/Projects/ac_vids/extracted_images/test/F_ON",
              "H:/My Drive/Projects/ac_vids/extracted_images/test/ON")
    os.rename("H:/My Drive/Projects/ac_vids/extracted_images/test/F_OFF",
              "H:/My Drive/Projects/ac_vids/extracted_images/test/OFF")
