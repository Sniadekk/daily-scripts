import cv2
import argparse
import os
import sys
import shutil
from skimage.measure import compare_ssim as ssim


def move_to_directory(file_name, directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    shutil.move("./%s" % file_name, "./%s/%s" % (directory_name, file_name))


orb = cv2.ORB_create()
def compare_images(input_image, photo_to_compare):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    kp_a, desc_a = orb.detectAndCompute(input_image, None)
    kp_b, desc_b = orb.detectAndCompute(photo_to_compare, None)
    matches = bf.match(desc_a, desc_b)
    similar_regions = [i for i in matches if i.distance < 70]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)




parser = argparse.ArgumentParser(
    description='Find similar photos to the one provided by user')
parser.add_argument('input_photo', metavar='file_name', type=str,
                    help="File name of photo that you want to compare with others in your current directory")
parser.add_argument('min_sim', metavar='min_sim', type=int,
                    help="Minimum percentage similarity of photos (integer)")

args = parser.parse_args()
min_sim = args.min_sim / 100

if not os.path.isfile(args.input_photo):
    print("This file doesn't exist")
    sys.exit()

files = [f for f in os.listdir('.') if os.path.isfile(
    f) and ".py" not in f and args.input_photo not in f]
# Resize photos so they won't be so large in memory
input_image = cv2.resize(cv2.imread(args.input_photo), (300, 300))


similar_photos = 0
for photo in files:
    photo_to_compare = cv2.resize(cv2.imread(photo), (300, 300))
    similarity = compare_images(input_image, photo_to_compare)
    print("%s - %s " % (photo, similarity))
    if similarity >= min_sim:
        similar_photos +=1
        move_to_directory(photo, "similar_photos")


