import os
import shutil
import sys
import random
import math

def create_directory(dir, delete_if_exists=False):
    if os.path.exists(dir):
        if delete_if_exists:
            shutil.rmtree(dir)
            os.mkdir(dir)
        else:
            pass
    else:
        os.mkdir(dir)


def generate_random_array(n):
    a = [i for i in range(0, n, 1)]
    for i in range(0, n - 1, 1):
        random_num = random.randint(i, n - 1)
        a[i], a[random_num] = a[random_num], a[i]
    return a


def create_dataset_partitions(imagenet_folder, train_val_split):
    imagenet_final_folder = os.path.join(os.getcwd(), "imagenet")
    create_directory(imagenet_final_folder, delete_if_exists=True)
    imagenet_train_folder = os.path.join(imagenet_final_folder, "train")
    imagenet_val_folder = os.path.join(imagenet_final_folder, "val")
    create_directory(imagenet_train_folder, delete_if_exists=True)
    create_directory(imagenet_val_folder, delete_if_exists=True)
    for dir in os.listdir(imagenet_folder):
        image_dir = os.path.join(imagenet_folder, dir)
        images = os.listdir(image_dir)
        image_dir_len = len(images)
        rand_arr = generate_random_array(image_dir_len)
        train_index_end = math.floor((train_val_split / 100) * image_dir_len)
        for i in range(0, image_dir_len, 1):
            image_name = images[rand_arr[i]]
            image_path = os.path.join(image_dir, image_name)
            if i <= train_index_end:
                output_path = os.path.join(imagenet_train_folder, image_name)
            else:
                output_path = os.path.join(imagenet_val_folder, image_name)
            shutil.copy(image_path, output_path)


if __name__ == '__main__':
    imagenet_folder = sys.argv[1]
    train_val_split = sys.argv[2]
    train_val_split = float(train_val_split)
    print("ImageNet Input Folder:", imagenet_folder)
    create_dataset_partitions(imagenet_folder, train_val_split)
