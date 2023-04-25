from abc import ABCMeta, abstractmethod

import data


class BaseItem(metaclass=ABCMeta):
    """
    Itemの抽象クラス、get_dictでItemのdictの実体を作る関数を持つ

    Itemを扱う側は、コンストラクタをわたし、
    get_dictするだけで良いというブラックボックス化を行うために、常にlist[dict**]を返すというプログラムにする"""

    @abstractmethod
    def get_dict(self):
        pass


class VoiceItem(BaseItem):
    def __init__(
        self,
        serif: str,
        emotion: data.EmotionAttr,
        frame: int,
        length: int,
        layer: int,
        voice_length: float,
        hatsuon: str,
        chara_attr: data.CharacterAttr,
    ):
        self.serif = serif
        self.emotion = emotion
        self.frame = frame
        self.length = length
        self.layer = layer
        self.voice_length = voice_length
        self.hatsuon = hatsuon
        self.chara_attr = chara_attr

    def get_dict(self):
        dic_list = []
        if self.chara_attr == data.CharacterAttr.TWO:
            dic_list.append(data.ItemDic.two_voice_reimu)
            dic_list.append(data.ItemDic.two_voice_marisa)
            dic_list[0]["Layer"] = data.LayerOrder.VOICE.value
            dic_list[1]["Layer"] = data.LayerOrder.TOGETHER_VOICE.value
            dic_list[0]["Length"] = self.length + 55
            dic_list[1]["Length"] = self.length + 55

        else:
            match self.chara_attr:
                case data.CharacterAttr.REIMU:
                    dic_list.append(data.ItemDic.voice_reimu)

                case data.CharacterAttr.MARISA:
                    dic_list.append(data.ItemDic.voice_marisa)

                case data.CharacterAttr.TITLE:
                    dic_list.append(data.ItemDic.voice_reimu)

            dic_list[0]["Layer"] = self.layer
            dic_list[0]["Length"] = self.length

        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["VoiceLength"] = self.voice_length
            dic_list[index]["Hatsuon"] = self.hatsuon
            dic_list[index]["Serif"] = self.serif
            if self.chara_attr == data.CharacterAttr.TWO:
                pass
            else:
                dic_list[index]["TachieFaceParameter"][
                    "Eyebrow"
                ] = data.EmotionDic.get_emotion(self.chara_attr, self.emotion)[
                    "Eyebrow"
                ]
                dic_list[index]["TachieFaceParameter"][
                    "Eye"
                ] = data.EmotionDic.get_emotion(self.chara_attr, self.emotion)["Eye"]
                dic_list[index]["TachieFaceParameter"][
                    "Mouth"
                ] = data.EmotionDic.get_emotion(self.chara_attr, self.emotion)["Mouth"]

        return dic_list


class TextItem(BaseItem):
    def __init__(
        self, text: str, frame: int, length: int, layer: int, text_attr: data.TextAttr
    ):
        self.text = text
        self.frame = frame
        self.length = length
        self.layer = layer
        self.text_attr = text_attr

    def get_dict(self):
        dic_list = []
        dic_list.append(data.ItemDic.text)
        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer

            dic_list[index]["Text"] = self.text

        match self.text_attr:
            case data.TextAttr.TITLE:
                pass

        return dic_list


class VideoItem(BaseItem):
    def __init__(
        self,
        frame: int,
        length: int,
        layer: int,
        video_attr: data.VideoAttr,
    ):
        self.frame = frame
        self.length = length
        self.layer = layer
        self.path = data.VideoPath.get_path(video_attr)
        self.video_attr = video_attr

    def get_dict(self):
        dic_list = []
        dic_list.append(data.ItemDic.video)
        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer
            dic_list[index]["FilePath"] = self.path

            match self.video_attr:
                case data.VideoAttr.BACKGROUND:
                    dic_list[index]["IsLooped"] = True

                case data.VideoAttr.END:
                    dic_list[index]["IsLooped"] = False

        return dic_list


class AudioItem(BaseItem):
    def __init__(
        self,
        frame: int,
        length: int,
        layer: int,
        audio_attr: data.AudioAttr,
    ):
        self.frame = frame
        self.length = length
        self.layer = layer
        self.path = data.AudioPath.get_path(audio_attr)
        self.audio_attr = audio_attr

    def get_dict(self):
        dic_list = []
        dic_list.append(data.ItemDic.audio)
        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer
            dic_list[index]["FilePath"] = self.path

            match self.audio_attr:
                case data.AudioAttr.OPENING:
                    dic_list[index]["IsLooped"] = True
                    pass

                case data.AudioAttr.MAIN:
                    dic_list[index]["IsLooped"] = True
                    pass

                case data.AudioAttr.SE:
                    dic_list[index]["IsLooped"] = False
                    pass

        return dic_list


class ImageItem(BaseItem):
    def __init__(
        self,
        frame: int,
        length: int,
        layer: int,
        image_attr: data.ImageAttr,
        num: int = 0,
    ):
        self.frame = frame
        self.length = length
        self.layer = layer
        self.path = data.ImagePath.get_path(image_attr, num)
        self.image_attr = image_attr

    def get_dict(self):
        dic_list = []
        dic_list.append(data.ItemDic.image)
        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer
            dic_list[index]["FilePath"] = self.path

            match self.image_attr:
                case data.ImageAttr.MATERIAL:
                    dic_list[index]["Y"]["From"] = -160.0
                    dic_list[index]["VideoEffects"] = []
                    pass

                case data.ImageAttr.BACKGROUND:
                    dic_list[index]["Y"]["From"] = 0
                    dic_list[index]["VideoEffects"] = []
                    pass
                case data.ImageAttr.FADE:
                    dic_list[index]["Y"]["From"] = 0
                    dic_list[index]["VideoEffects"] = [
                        {
                            "$type": "YukkuriMovieMaker.Project.Effects.InOutFadeEffect, YukkuriMovieMaker",
                            "Label": "フェードイン・アウト",
                            "Value": 0.0,
                            "IsInEffect": True,
                            "IsOutEffect": True,
                            "EffectTimeSeconds": 0.5,
                            "EasingType": "Sine",
                            "EasingMode": "Out",
                            "IsEnabled": True,
                        }
                    ]
                    pass

        return dic_list


class TachieItem(BaseItem):
    def __init__(
        self, frame: int, length: int, layer: int, chara_attr: data.CharacterAttr
    ):
        self.frame = frame
        self.length = length
        self.layer = layer
        self.chara_attr = chara_attr

    def get_dict(self):
        dic_list = []
        match self.chara_attr:
            case data.CharacterAttr.REIMU:
                dic_list.append(data.ItemDic.tachie_reimu)

            case data.CharacterAttr.MARISA:
                dic_list.append(data.ItemDic.tachie_marisa)

        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer

        return dic_list


class EffectItem(BaseItem):
    def __init__(
        self, frame: int, length: int, layer: int, effect_attr: data.EffectAttr
    ):
        self.frame = frame
        self.length = length
        self.layer = layer
        self.effect_attr = effect_attr

    def get_dict(self):
        dic_list = []
        match self.effect_attr:
            case data.EffectAttr.TRANSITION_IN:
                dic_list.append(data.ItemDic.mosaic_transition_in)

            case data.EffectAttr.TRANSITION_OUT:
                dic_list.append(data.ItemDic.mosaic_transition_out)

        for index in range(len(dic_list)):
            dic_list[index]["Frame"] = self.frame
            dic_list[index]["Length"] = self.length
            dic_list[index]["Layer"] = self.layer

        return dic_list
