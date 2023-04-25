import correct_check
import docx_xlsx
import emotion
import htm_clean
import imgtxt_chng
import init
import kaigyou
import resize
import separate
import txt
import xlsm_txt

name, client = init.main()
API_key = "dad10cd5b97f39fb"
API_Endpoint = "https://ai-api.userlocal.jp/text-emotion/basic-emotions"


def main():
    htm_clean.txt_extract(name, client)
    imgtxt_chng.main(name, client)
    resize.resize(name, client)
    docx_xlsx.main(name, client)
    separate.separate(name, client)
    kaigyou.kaigyou(name, client)
    txt.excel(name, client)
    xlsm_txt.extract(name, client)
    correct_check.main(name, client)
    emotion.emotion(name, client)


if __name__ == "__main__":
    main()
