import glob

import cv2
import pyperclip

files = glob.glob("D:\\work_movies\\sumiwataturo\\*")
times = [[]]
alltimes = [[] for i in range(len(files))]
tanka = []
money = 0
minutes = 0
seconds = 0
time1 = 0
time2 = 0
alltime1 = 0
alltime2 = 0
text1 = ""
text2 = ""

print(f"動画ファイル名を入力してください．")
v = input()
cap = cv2.VideoCapture(f"D:\\work_movies\\sumiwataturo\\{v}.mp4")
print("")
second = cap.get(cv2.CAP_PROP_FRAME_COUNT) // 60
times[0].append(int(second // 60))
times[0].append(int(second % 60))
text1 += f"{times[0][0]}:{times[0][1]}"
time1 += times[0][0]
time2 += times[0][1]

minutes = time1 + time2 // 60
seconds = time2 % 60


for i, mov in enumerate(files):
    cap = cv2.VideoCapture(mov)
    second = cap.get(cv2.CAP_PROP_FRAME_COUNT) // 60
    alltimes[i].append(int(second // 60))
    alltimes[i].append(int(second % 60))
    alltime1 += alltimes[i][0]
    alltime2 += alltimes[i][1]

allminutes = alltime1 + alltime2 // 60
allseconds = alltime2 % 60

print(f"今回の報酬は{str(int((minutes*250+seconds*25/6)*0.858))}円です。お疲れさまでした。\n")

print(
    f"動画をアップロードいたしました。\n{len(files)}件目 {str(minutes)}:{str(seconds).zfill(2)} ({str(allminutes)}:{str(allseconds).zfill(2)})\n≪{pyperclip.paste()}≫\nとなります。"
)

input()
pyperclip.copy(
    f"動画をアップロードいたしました。\n{len(files)}件目 {str(minutes)}:{str(seconds).zfill(2)} ({str(allminutes)}:{str(allseconds).zfill(2)})\n≪{pyperclip.paste()}≫\nとなります。"
)
