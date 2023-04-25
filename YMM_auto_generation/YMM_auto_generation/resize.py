import getpass
import glob
import os
from pathlib import Path

import cv2
import init
from PIL import Image
from tqdm import tqdm
import os


def resize(name, client):
    print("")
    print("---------------resize.py-------------------")

    # 定数
    n = 1

    # imagesというリサイズ後の画像を格納するフォルダを作成する．
    pic_dir = Path(
        f"{os.path.expanduser('~')}\\works\\" + client + "\\" + name + "\\images"
    )
    pic_dir.mkdir(exist_ok=True)

    # word -> htmlとして出来たfilesというフォルダを取得し，その中のpngファイルのみを選出．
    img_dir = glob.glob(
        f"{os.path.expanduser('~')}\\works\\{client}\\{name}\\*files"
    )
    gifs = glob.glob(img_dir[0] + "\\*.gif")
    # jpgs= glob.glob(img_dir[0] + "\\*.gif")

    for gif in gifs:
        png = Image.open(gif)
        png.save(gif.replace("gif", "png"))
        png.close()
        os.remove(gif)

    pictures = glob.glob(img_dir[0] + "\\*")

    for img in tqdm(pictures):
        # 画像読み込み
        image = cv2.imread((img), -1)

        # アスペクト比(各クライアントごとに自由に設定)
        h, w = image.shape[:2]
        aspect = w / h

        # 横長
        if 1037 / 659 >= aspect:
            nh = 659
            nw = round(nh * aspect)

        # 縦長
        else:
            nw = 1037
            nh = round(nw / aspect)

        # 上の条件分岐で得た結果からリサイズを行う
        nimg = cv2.resize(image, dsize=(nw, nh))

        # 保存
        cv2.imwrite(
            str(pic_dir)
            + "\\"
            + img.replace(
                f"{os.path.expanduser('~')}\\works\\{client}\\{name}\\{name}.files",
                "",
            ),
            nimg,
        )
        n += 1


if __name__ == "__main__":
    name, client = init.main()
    resize(name, client)
