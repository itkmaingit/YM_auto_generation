import getpass
import os
import init


def main(name, client):
    """
    re_image.txtとdaihon.txtを比較して、おかしな文章がないかを確認するための関数
    """
    filepath = f"{os.path.expanduser('~')}\\works\\{client}\\{name}"
    global j
    j = 0
    with open(f"{filepath}\\re_image.txt", "r", encoding="utf-8") as imf:
        with open(f"{filepath}\\daihon.txt", "r", encoding="utf-8") as dai:
            imt = imf.readlines()
            dat = dai.readlines()

            for i, line in enumerate(imt):
                flag = line.find(":")
                if flag == -1 or flag > 10:
                    text = line[:8].rstrip("\n")
                else:
                    text = line[:flag].rstrip("\n")
                checker = dai_check(dat, text)
                if not checker:
                    print(f"re_image.txtの{i+1}行目がおかしい！確認して！")
                    print(f"++\n{line}++")


def dai_check(dat, text):
    global j
    flag = False
    for n, txt in enumerate(dat[j:]):
        t = txt.lstrip("霊夢「").lstrip("魔理沙「").lstrip("タイトル「").rstrip("\n").rstrip("」")
        if t in text:
            flag = True
            j = n
            break
        elif text in t:
            flag = True
            j = n
            break
    return flag


if __name__ == "__main__":
    name, client = init.main()
    main(name, client)
