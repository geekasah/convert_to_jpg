import os
import rawpy
from PIL import Image
import time
from multiprocessing import Pool
import shutil

# scrolled down to the main function
# note: folder of jpg files will be saved inside image_converted/dir_to_save folder

class FileToConvert:
    def __init__(self, path, batchsize, dir_to_save): # initialization
        self.path = path # path to raw files
        self.file_name = [file for file in os.listdir(self.path) if not(file.endswith('.jpg'))] # list of file inside path
        self.batchsize = batchsize # size of the batch (arbitrary)
        self.dir_to_save = os.path.join('image_converted', dir_to_save) # name of the directory to save the jpg image

    def batch(self): # divide folder into group of files called batch
        i = 0
        batch_list = []
        while i<(len(self.file_name)-1):
            batch_list.append(self.file_name[i:i+self.batchsize])
            i+=self.batchsize
        return batch_list
    
    def convert(self,image): # convert raw to jpg
        try:
            raw = rawpy.imread(self.path+'/'+image) # reading raw file
            rgb = raw.postprocess(use_camera_wb=True)
            Image.fromarray(rgb).save(f'{self.dir_to_save}/{image[:-4]}.jpg', optimize=True) # exporting raw file
        except: # if file isnt raw
            print(f'This file --> {image} cannot be open')
            pass

    def process(self):
        batch_list = self.batch()
        os.mkdir(self.dir_to_save)
        for k, i in enumerate(batch_list): # processing per batch
            print(f'Batch {k+1} on progress...')
            start_temp = time.time()
            with Pool(8) as pool: # multiprocessing to speed up converting process
                pool.map(self.convert, i)
            end_temp = time.time()
            print(f'-----------------Time taken for batch {k+1} = {"{0:.3f}".format(end_temp-start_temp)}')
    
    def zipping(self): # zipping file, needed if want to download jpg file
        shutil.make_archive(self.dir_to_save, 'zip', self.dir_to_save)

if __name__ == '__main__':
    
    # Initiation, stop here if you only want to convert raw to jpg
    os.mkdir('image_converted')
    path = 'path/to/your/raw/folder' # specified path to the raw files FOLDER
    q = FileToConvert(path=path, batchsize=60, dir_to_save='your_jpg_folder_title') # create FileToConvert object

    # Converting all files
    start = time.time()
    q.process()
    end = time.time()
    print(f'Total time taken for this process is {"{0:.3f}".format(end-start)}')
    
    # will be used for online purposes
    '''zip_file = input('do you want to zip the file [y/N]')
    if zip_file:
        print('zipping file -------')
        q.zipping()
    else:
        print('thanks have a nice day!')'''
