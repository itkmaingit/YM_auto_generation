import getpass
import glob
import re
import os
import init
from tqdm import tqdm


def txt_extract(name, client):
    print("")
    print("---------------htm_clean.py-------------------")

    p1 = re.compile(r"<span.*?>")
    p2 = re.compile(r"</span>")
    p3 = re.compile(r">[^<>]+<")
    p4 = re.compile(r"img")
    p5 = re.compile(r"\d&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ")
    filename = glob.glob(
        f"{os.path.expanduser('~')}\\works\\{client}\\{name}\\*.htm"
    )

    with open(filename[0], "r", encoding="cp932") as f:
        with open(
            f"{os.path.expanduser('~')}\\works\\"
            + client
            + "\\"
            + name
            + "\\image.txt",
            "w",
            encoding="utf-8",
        ) as wf:
            for text in tqdm(f.readlines()):
                text = p1.sub("", text)
                text = p2.sub("", text)
                if text:

                    if p3.search(text):
                        text = p3.search(text).group()

                        if text.replace(" ", "") != ">&nbsp;<":
                            text = text.lstrip(">")
                            text = text.rstrip("<")
                            text = text.replace("「", "『")
                            text = text.replace("」", "』")
                            text = p5.sub("", text)
                            text = text.replace("&nbsp;", "")
                            text.replace(" ", "")
                            text.replace("　", "")
                            wf.write(text)

                    elif p4.search(text):
                        wf.write("\n")
                else:
                    break


if __name__ == "__main__":
    name, client = init.main()
    txt_extract(name, client)
