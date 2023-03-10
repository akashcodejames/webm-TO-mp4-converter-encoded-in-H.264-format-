import os
import sys

path = "A:/Module 10"
print("tim")
dir_list1 = os.listdir(path)
hmm = 0
while True:
    try:
        while hmm < len(dir_list1):
            dir_list = os.listdir(path + "/" + dir_list1[hmm])
            i = 0
            while i < len(dir_list):
                if "webm" in dir_list[i]:
                    list_1 = dir_list[i].split("webm")
                    a = list_1[0] + "mp4"
                    print(a)
                    try:
                        os.system(f'cmd /c "ffmpeg -i "{path + "/" + dir_list1[hmm] + "/" + dir_list[i]}" -c:v copy "{ path + "/" + dir_list1[hmm] + "/" + a}" "')
                    except:
                        sys.exit(0)
                    os.remove(path + "/" + dir_list1[hmm] + "/" + dir_list[i])
                    i = i + 1
                else:
                    print("ok")
                    i = i + 1
            hmm = hmm + 1
            if hmm == len(dir_list1):
                hmm = "abc" + 1
    except:
        if hmm == len(dir_list1):
            break
        else:
            hmm = hmm + 1

# prints all files
print(len(dir_list))

# os.system('cmd /k "ffmpeg -i "A:/Module 8/1 - Deep LearningNeural Networks/1.1 - History of Neural networks and Deep '
#           'Learning..webm" getsomeen.mp4 "')
