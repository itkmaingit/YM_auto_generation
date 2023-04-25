import copy
import getpass
import json
import os
import item
import openpyxl
import useful_functions
from output_dic import output_dic

import data


def main():
    """
    1.ymmpからVoiceItemのListを作成，re_image.txtから画像を挿入する時点の最初の文字列と，その行番号の
    辞書型を格納したListを作成
    2.1,2で作成したListを使って，VoiceItem以外を格納したItemListを作成
    3.タイトル，BGM，FADE，キャラクターの立ち絵，背景，エンディングなどを入れていく

    layer構成
    0 background video
    1 background image
    2 tachie reimu
    3 tachie marisa
    4 voices
    5 two voices
    6 material image
    7 SE
    8 title text
    9 BGM
    10 fade
    """
    json_file: str = open(data.YMMP_PATH, "r", encoding="utf-8_sig")
    before_ymmp_dic = json.load(json_file)
    emotion_sheet = openpyxl.load_workbook(
        rf"{os.path.expanduser('~')}\works\{data.client}\{data.date}\daihon_completed.xlsx"
    )["Sheet"]
    voice_item_list = []
    other_item_list = []  # voice_item以外を格納
    all_item_list = []
    image_timing_list = []
    fade_timing = []  # FADEのタイミングのindexを格納するリスト，imageの作成の際にFADEが間にないかを確認する
    pre_text: str = ""
    cur_text: str = ""
    pre_frame: int = 0
    cur_frame: int = 0
    last_frame: int = 0
    length: int = 0
    pre_title_text: str = ""
    cur_title_text: str = ""

    # 画像を挿入する時点の最初の8文字程度の文字列を含むリストを作成
    with open(
        rf"{os.path.expanduser('~')}\works\{data.client}\{data.date}\re_image.txt",
        "r",
        encoding="utf-8",
    ) as re_image_txt:
        for row, text in enumerate(re_image_txt.readlines()):
            pre_text = cur_text
            cur_text = text
            # 一番最初の行か，同じ場所に画像が複数枚入る時はパス
            if row == 0 or cur_text == pre_text:
                continue

            colon_order = text.find(":")
            if text:
                if colon_order == -1 or colon_order > 10:
                    image_timing_list.append(
                        {
                            "text": useful_functions.remove_new_line(text[:8]),
                            "row": row,
                        }
                    )
                else:
                    image_timing_list.append(
                        {
                            "text": useful_functions.remove_new_line(
                                text[: colon_order - 1]
                            ),
                            "row": row,
                        }
                    )

    # VoiceItemを全て格納したリストを作成
    for index, voice_item in enumerate(before_ymmp_dic["Timeline"]["Items"]):
        voice_item_list.append(
            item.VoiceItem(
                serif=voice_item["Serif"],
                emotion=data.ConvertToAttr.int_to_EmotionAttr(
                    int(emotion_sheet[f"C{str(index+1)}"].value)
                ),
                frame=voice_item["Frame"],
                length=voice_item["Length"],
                layer=data.LayerOrder.VOICE.value,
                voice_length=voice_item["VoiceLength"],
                hatsuon=voice_item["Hatsuon"],
                chara_attr=data.ConvertToAttr.str_to_CharacterAttr(
                    voice_item["CharacterName"]
                ),
            )
        )
        if (
            data.ConvertToAttr.str_to_CharacterAttr(voice_item["CharacterName"])
            == data.CharacterAttr.FADE
        ):
            fade_timing.append(index)

        if index == len(before_ymmp_dic["Timeline"]["Items"]) - 1:
            last_frame = voice_item["Frame"] + voice_item["Length"] + 55

    # 毎ループでImageItemとAudioItemをitem_listに格納していく．
    # pre_frameがItemのframe,cur_frame-pre_frameの長さがlengthになることに注意
    # (どこまで画像ファイルを伸ばせばいいかわからない)
    # 最初と最後だけ挙動が異なる点にも注意
    # FADE周りの処理は正直諦めてべた書き，読む人は苦労するだろうけどごめんなさい．
    # 新しいvoice_list_for_image_timingを作って，合致するものがあった時，それ以前のvoice_itemを削除している．
    # fadeにぶち当たった時は不自然にならないようにlengthを55増やしている
    # Titleのテキスト前で切るか，それともTitleのテキストに画像が割り振られているかで挙動を変えている．
    voice_item_list_for_image_timing = copy.deepcopy(voice_item_list)
    is_first = True

    for image_timing, is_last in useful_functions.last_one(image_timing_list):
        # print(f'{image_timing["row"]}::{image_timing["text"]}')
        for index, voice_item in enumerate(voice_item_list_for_image_timing):
            # print(
            #     f'{image_timing["row"]}::{image_timing["text"]}-----{useful_functions.remove_new_line(voice_item.serif)}'
            # )
            if (
                image_timing["text"]
                in useful_functions.remove_new_line(voice_item.serif)
                # ----------------------------------------------------------------
                or useful_functions.remove_new_line(voice_item.serif)
                in image_timing["text"]
                # ----------------------------------------------------------------
                or voice_item.chara_attr
                in [
                    data.CharacterAttr.FADE,
                    data.CharacterAttr.TITLE,
                ]
            ):
                # print("\n----------------------------\n")
                # print(
                #     f"{image_timing}['row']---{image_timing['text']}::{useful_functions.remove_new_line(voice_item.serif)}"
                # )
                if voice_item.chara_attr == data.CharacterAttr.TITLE and image_timing[
                    "text"
                ] in useful_functions.remove_new_line(voice_item.serif):
                    pre_frame = cur_frame
                    cur_frame = voice_item.frame
                    length = voice_item.frame - pre_frame

                elif voice_item.chara_attr == data.CharacterAttr.FADE:
                    pre_frame = cur_frame
                    cur_frame = voice_item.frame + voice_item.length
                    length = voice_item.frame - pre_frame + 55

                elif voice_item.chara_attr == data.CharacterAttr.TITLE:
                    pre_frame = cur_frame
                    cur_frame = voice_item.frame + voice_item.length
                    length = voice_item.frame - pre_frame

                else:
                    pre_frame = cur_frame
                    cur_frame = voice_item.frame
                    length = voice_item.frame - pre_frame

                del voice_item_list_for_image_timing[: index + 1]

                if is_first:
                    is_first = False
                    break

                if is_last:
                    other_item_list.append(
                        item.ImageItem(
                            frame=cur_frame,
                            length=last_frame - cur_frame,
                            layer=data.LayerOrder.IMAGE.value,
                            image_attr=data.ImageAttr.MATERIAL,
                            num=image_timing["row"],
                        )
                    )
                    other_item_list.append(
                        item.AudioItem(
                            frame=cur_frame,
                            length=last_frame - cur_frame,
                            layer=data.LayerOrder.SE.value,
                            audio_attr=data.AudioAttr.SE,
                        )
                    )

                    # 最初以外全ての場合行う(最後でも行う)
                if length <= 0:
                    continue
                other_item_list.append(
                    item.ImageItem(
                        frame=pre_frame,
                        length=length,
                        layer=data.LayerOrder.IMAGE.value,
                        image_attr=data.ImageAttr.MATERIAL,
                        num=image_timing["row"] - 1,
                    )
                )
                other_item_list.append(
                    item.AudioItem(
                        frame=pre_frame,
                        length=length,
                        layer=data.LayerOrder.SE.value,
                        audio_attr=data.AudioAttr.SE,
                    )
                )

                break

    # タイトルを挿入
    # attrがTITLEのテキストを，TITLEあるいはFADEの手前まで挿入
    # FADEまで挿入したら，もうTITLEは存在しないことと同義なのでbreak
    # TITLEのframe<->TITLEのframe,.....,TITLEのframe<->FADEのframe
    pre_frame = 0
    cur_frame = 0
    length = 0
    is_first = True
    pre_attr = None
    cur_attr = None
    # chara_attrがTITLEかFADEの要素だけを抽出したリストを新たに作成
    title_and_fade_list = [
        voice_item
        for voice_item in copy.deepcopy(voice_item_list)
        if voice_item.chara_attr
        in [
            data.CharacterAttr.TITLE,
            data.CharacterAttr.FADE,
        ]
    ]

    for index, voice_item in enumerate(title_and_fade_list):
        pre_attr = cur_attr
        cur_attr = voice_item.chara_attr

        pre_title_text = cur_title_text
        cur_title_text = useful_functions.remove_new_line(voice_item.serif)
        pre_frame = cur_frame
        cur_frame = voice_item.frame
        length = cur_frame - pre_frame
        if pre_attr == data.CharacterAttr.TITLE:
            other_item_list.append(
                item.TextItem(
                    text=pre_title_text,
                    frame=pre_frame,
                    length=length,
                    layer=data.LayerOrder.TITLE.value,
                    text_attr=data.TextAttr.TITLE,
                )
            )

        if index == len(title_and_fade_list) - 1:
            if cur_attr == data.CharacterAttr.TITLE:
                other_item_list.append(
                    item.TextItem(
                        text=cur_title_text,
                        frame=cur_frame,
                        length=last_frame - cur_frame,
                        layer=data.LayerOrder.TITLE.value,
                        text_attr=data.TextAttr.TITLE,
                    )
                )

    # BGMを挿入
    # テキストの時とそこまで変わらないが，途中FADEを挟む部分は挿入しないことに注意
    # 最初(0)<->FADE1_frame,FADE1_frame+length<->FADE2_frame,FADE2_frame+length<->last_frame
    pre_frame = 0
    cur_frame = 0
    length = 0
    fade_list = [
        voice_item
        for voice_item in voice_item_list
        if voice_item.chara_attr == data.CharacterAttr.FADE
    ]

    other_item_list.append(
        item.AudioItem(
            frame=0,
            length=fade_list[0].frame,
            layer=data.LayerOrder.BGM.value,
            audio_attr=data.AudioAttr.OPENING,
        )
    )
    if len(fade_list) == 2:
        other_item_list.append(
            item.AudioItem(
                frame=fade_list[0].frame + fade_list[0].length,
                length=fade_list[1].frame - (fade_list[0].frame + fade_list[0].length),
                layer=data.LayerOrder.BGM.value,
                audio_attr=data.AudioAttr.MAIN,
            )
        )
        other_item_list.append(
            item.AudioItem(
                frame=fade_list[1].frame + fade_list[1].length,
                length=last_frame - (fade_list[1].frame + fade_list[1].length),
                layer=data.LayerOrder.BGM.value,
                audio_attr=data.AudioAttr.MAIN,
            )
        )
    elif len(fade_list) == 1:
        other_item_list.append(
            item.AudioItem(
                frame=fade_list[0].frame + fade_list[0].length,
                length=last_frame - (fade_list[0].frame + fade_list[0].length),
                layer=data.LayerOrder.BGM.value,
                audio_attr=data.AudioAttr.MAIN,
            )
        )

    # 背景動画，背景画像，立ち絵を挿入
    # 最初(0)<->last_frame
    other_item_list.append(
        item.VideoItem(
            frame=0,
            length=last_frame,
            layer=data.LayerOrder.BACKGROUND_VIDEO.value,
            video_attr=data.VideoAttr.BACKGROUND,
        )
    )
    other_item_list.append(
        item.ImageItem(
            frame=0,
            length=last_frame,
            layer=data.LayerOrder.BACKGROUND_IMAGE.value,
            image_attr=data.ImageAttr.BACKGROUND,
        )
    )
    other_item_list.append(
        item.TachieItem(
            frame=0,
            length=last_frame,
            layer=data.LayerOrder.TACHIE_REIMU.value,
            chara_attr=data.CharacterAttr.REIMU,
        )
    )
    other_item_list.append(
        item.TachieItem(
            frame=0,
            length=last_frame,
            layer=data.LayerOrder.TACHIE_MARISA.value,
            chara_attr=data.CharacterAttr.MARISA,
        )
    )

    # FADEのvoice_itemをフェード画像に変換,frameはfade_voice_frame+15,length80
    # voice_itemは削除する
    # fade_listは流用
    for fade_voice_item in fade_list:
        other_item_list.append(
            item.ImageItem(
                frame=fade_voice_item.frame + 15,
                length=80,
                layer=data.LayerOrder.FADE.value,
                image_attr=data.ImageAttr.FADE,
            )
        )
        voice_item_list.remove(fade_voice_item)

    # エンディングを挿入
    # last_frame-40にlength80のblackout_image
    # last_frameにlength877のend_video
    other_item_list.append(
        item.ImageItem(
            frame=last_frame - 40,
            length=80,
            layer=data.LayerOrder.FADE.value,
            image_attr=data.ImageAttr.FADE,
        )
    )
    other_item_list.append(
        item.VideoItem(
            frame=last_frame,
            length=877,
            layer=data.LayerOrder.BACKGROUND_VIDEO.value,
            video_attr=data.VideoAttr.END,
        )
    )
    # next_frame = 0
    for voice_item in voice_item_list:
        for voice_item in copy.deepcopy(voice_item.get_dict()):
            all_item_list.append(voice_item)

    for other_item in other_item_list:
        for other_item in copy.deepcopy(other_item.get_dict()):
            all_item_list.append(other_item)

    sorted_list = sorted(all_item_list, key=data.get_frame)
    after_ymmp_dic = output_dic(sorted_list)

    with open(data.YMMP_PATH_AFTER, "w", encoding="utf-8") as f:
        json.dump(after_ymmp_dic, f)


if __name__ == "__main__":
    main()
