from PIL import Image
import imagehash
import os


class DuplicatesRemover:
    def __init__(self, dir):
        self.dir = dir

    def hash_of_image(self,path):
        return imagehash.average_hash(Image.open(path)) #returns value of the hash function for photo given in path

    def get_duplicates(self,path): #returns a list of duplicated photos using hash checking
        used_hashes = set()
        duplicated = []
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                path_to_current_photo = path+filename
                curr_hash = self.hash_of_image(path_to_current_photo)
                if curr_hash in used_hashes:
                    duplicated.append(path_to_current_photo)
                else:
                    used_hashes.add(curr_hash)
        return duplicated

    def remove_files(self,files):
        for file in files:
            os.remove(file)

    def remove_file(self,file):
        os.remove(file)

    def get_paths_to_photos_in_dir(self):
        paths = []
        for filename in os.listdir(self.dir):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                path_to_current_photo = self.dir+filename
                paths.append(path_to_current_photo)
        return paths 

    def remove_all_duplicated_photos_in_directory(self):
        paths = self.get_paths_to_photos_in_dir()
        self.remove_files(paths)






