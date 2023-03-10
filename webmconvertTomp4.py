import os
import sys

def my_func(path):
    try:
        dir_list = os.listdir(path)
    except:
        return
    i = 0
    while i < len(dir_list):
        if "webm" in dir_list[i]:
            list_1 = dir_list[i].split("webm")
            a = list_1[0] + "mp4"
            print(a)
            try:
                os.system(
                    f'cmd /c "ffmpeg -i "{path + "/" + dir_list[i]}" -c:v copy "{path + "/" + a}" "')
            except:
                sys.exit(0)
            os.remove(path + "/" + dir_list[i])
            i = i + 1
        else:
            my_func(path + "/" + dir_list[i]) # this recursive call will enable to visit all directories where a file can exist and will search for webm video
            i = i + 1



paths = "A:\Module 1"         # path which contains all the webm videos , it could contain other files , 
                              # this program can search for all directories within provided directory and search for webm videos and convert it mp4 )
                              # It will not effect your other files
my_func(paths)
 
    
    
   
