import os
import sys

def my_func(path):
    try:
        dir_list = os.listdir(path) # trying to get all file names in (path) directory in list dir_list
    except:
        return
    i = 0
    while i < len(dir_list):
        if "webm" in dir_list[i]:           # checking the i th element in dir_list is webm type 
            list_1 = dir_list[i].split("webm")
            a = list_1[0] + "mp4"
            print(a)
            try:
                os.system(
                    f'cmd /c "ffmpeg -i "{path + "/" + dir_list[i]}" -c:v copy "{path + "/" + a}" "')  # Executing CMD command 
            except:
                sys.exit(0)
            os.remove(path + "/" + dir_list[i])  # to remove previous webm video since mp4 is already saved, this line does not gets executed if some error occur at 16th line hence ensuring your data is not lost in any case
            i = i + 1
        else:
            my_func(path + "/" + dir_list[i])  # If the file is not a webm type, there is a chance that it is a directory with further files 
                                               # that could also contain webm video, hence we must also investigate this file further.
                
                                               # this recursive call will enable to visit all directories where a file can exist and will search for webm video
            i = i + 1



paths = "A:\Module 1"         # path which contains all the webm videos , it could contain other files , 
                              # this program can search for all directories within provided directory and search for webm videos and convert it mp4 )
                              # It will not effect your other files
                              # Change paths directory where your webm videos are stored, as i mentioned that directory could also contain other files it will ignore them which are not webm video
my_func(paths)
 
    
    
   
