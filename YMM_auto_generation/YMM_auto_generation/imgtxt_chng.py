# import re
import os
import getpass

import init
from tqdm import tqdm


def main(name, client):
    print("")
    print("---------------imgtxt_chng.py----------------")

    # p1 = re.compile(r"\d:.*?$")
    # p2 = re.compile(r"^\d:.*$")

    with open(
        f"{os.path.expanduser('~')}\\works\\"
        + client
        + "\\"
        + name
        + "\\image.txt",
        "r",
        encoding="utf-8",
    ) as f:
        lst = f.readlines()
        with open(
            f"{os.path.expanduser('~')}\\works\\"
            + client
            + "\\"
            + name
            + "\\re_image.txt",
            "w",
            encoding="utf-8",
        ) as wf:
            for i, text in enumerate(tqdm(lst)):
                # print(text)
                if text == "\n":
                    text = lst[judge(lst, i)]
                if text[1] != ":":
                    append_text = text
                else:
                    if text[0] == "4":
                        append_text = "楔楔楔むら"
                    else:
                        append_text = text[2:]

                wf.write(
                    append_text.replace(" ", "")
                    .replace("　", "")
                    .replace("&#12316;", "〜")
                    .replace("&amp;", "&")
                    .replace("&#8194;", "")
                    .replace("&quot;", '"')
                    .replace("&#8203;", "")
                    .replace("&#8226;", "•")
                )


def judge(lst, i):
    k = i
    while lst[k] == "\n":
        k += 1
    return k


if __name__ == "__main__":
    name, client = init.main()
    main(name, client)
