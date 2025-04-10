import imageio.v3 as iio
from os import listdir, path, mkdir
from util import create_subfolder

video_path = "C:/Users/Thanaporn/Desktop/ac_vids/"
image_path = "/research/ac_vids/extracted_images"
file_list = listdir(video_path)
train_frames = 50 * 30
test_frames = 10 * 30

file_list = ["C_OFF_B_FLST_86.mp4"]
create_subfolder(image_path)

for file_name in file_list:
    if not file_name.endswith(".mp4"):
        print("skipped:", file_name)
        continue
    print("processing:", file_name)
    for idx, frame in enumerate(iio.imiter(path.join(video_path, file_name))):
        if idx < train_frames:  # first train_frames frames to train
            iio.imwrite(path.join(image_path, "train",
                                  file_name[0:file_name.index("_", 3)],
                                  f"{file_name[:-4]:s}_{idx:04d}.jpg"), frame)
        elif idx < train_frames + test_frames:  # next test_frames frames to test
            iio.imwrite(path.join(image_path, "test",
                                  file_name[0:file_name.index("_", 3)],
                                  f"{file_name[:-4]:s}_{idx:04d}.jpg"), frame)
        else:  # if exceeds train_frames + test_frames, done
            break
    print("finished:", file_name)
print("done")

