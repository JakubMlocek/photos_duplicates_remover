from PIL import Image
import imagehash
import os

def hash_of_image(path):
    return imagehash.average_hash(Image.open(path)) #returns value of the hash function for photo given in path

def get_duplicates(path): #returns a list of photos which hashes were covered before
    used_hashes = set()
    duplicated = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path_to_current_photo = path+filename
            curr_hash = hash_of_image(path_to_current_photo)
            if curr_hash in used_hashes:
                duplicated.append(path_to_current_photo)
            else:
                used_hashes.add(curr_hash)
    return duplicated

def remove_files(files):
    for file in files:
        os.remove(file)

def remove_file(file):
    os.remove(file)

def get_paths_to_photos_in_dir(path):
    paths = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path_to_current_photo = path+filename
            paths.append(path_to_current_photo)
    return paths 


