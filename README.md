# convert_to_jpg
This is a repo for converting RAW images to JPG. It uses multiprocessing to speed up the process up to 0.84 s 23MBper file, in which each raw file is on size 

Hi this is me Ardi!

The code purposes is to convert RAW file such as .NEF or .ARW from camera, to .jpg.

Here is the guide to use this code!

0. Download 02_dependencies.bat and 03_convert_to_jpg.py
1. Make sure you place all you raw files into 1 folder, better if only raw file inside
2. Double-click on dependencies.bat to install all dependencies or run >>start dependencies.bat on your terminal
3. Open up convert_to_jpg.py, follow the instruction in code's comment.
4. All the files will be exported inside your specified file, inside image_converted

NB: to initiate the class, you just need to fill in

path = path to your raw files folder \n
batchsize = how big is the batch, it is arbitrary, but last time I tried, 60 has the best performance \n
dir_to_save = where in the image_converted you want to save the jpg files, it will be the title of your jpg files folder
