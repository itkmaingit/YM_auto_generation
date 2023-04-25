import getpass
import glob
import random
import os
from enum import Enum, Flag, auto

import init

date, client = init.main()
YMMP_PATH = rf"{os.path.expanduser('~')}\works\{client}\PF\{date}.ymmp"
YMMP_PATH_AFTER = rf"{os.path.expanduser('~')}\works\{client}\PF\{date}.ymmp"
RESOURCE_PATH = rf"{os.path.expanduser('~')}\works\{client}\YukkuriMovieMaker4\const"
PROJECT_PATH = rf"{os.path.expanduser('~')}\works\{client}\{date}"

EMOTION_PATH_REIMU = (
    rf"{os.path.expanduser('~')}\works\{client}\YukkuriMovieMaker4\Characters\Reimu"
)
EMOTION_PATH_MARISA = (
    rf"{os.path.expanduser('~')}\works\{client}\YukkuriMovieMaker4\Characters\Marisa"
)


class VideoAttr(Flag):
    BACKGROUND = auto()
    END = auto()


class ImageAttr(Flag):
    MATERIAL = auto()
    BACKGROUND = auto()
    FADE = auto()


class AudioAttr(Flag):
    OPENING = auto()
    MAIN = auto()
    SE = auto()


class TextAttr(Flag):
    TITLE = auto()


class CharacterAttr(Flag):
    REIMU = auto()
    MARISA = auto()
    TWO = auto()
    TITLE = auto()
    FADE = auto()


class EmotionAttr(Flag):
    LOVE = auto()
    JOY = auto()
    QUESTION = auto()
    EXCLAMATION = auto()
    FEAR = auto()
    SADNESS = auto()
    ANGER = auto()
    SILENT = auto()


class EffectAttr(Flag):
    TRANSITION_IN = auto()
    TRANSITION_OUT = auto()


class LayerOrder(Enum):
    BACKGROUND_VIDEO = 0
    BACKGROUND_IMAGE = 1
    TACHIE_REIMU = 2
    TACHIE_MARISA = 3
    VOICE = 4
    TOGETHER_VOICE = 5
    IMAGE = 6
    SE = 7
    TITLE = 8
    BGM = 9
    FADE = 10


class ConvertToAttr:
    @staticmethod
    def int_to_EmotionAttr(num: int) -> EmotionAttr:
        if num == 1:
            return EmotionAttr.LOVE

        elif num == 2:
            return EmotionAttr.JOY

        elif num == 3:
            return EmotionAttr.QUESTION

        elif num == 4:
            return EmotionAttr.EXCLAMATION

        elif num == 5:
            return EmotionAttr.FEAR

        elif num == 6:
            return EmotionAttr.SADNESS

        elif num == 7:
            return EmotionAttr.ANGER

        elif num == 8:
            return EmotionAttr.SILENT

    @staticmethod
    def str_to_CharacterAttr(name: str) -> CharacterAttr:
        match name:
            case "霊夢":
                return CharacterAttr.REIMU

            case "魔理沙":
                return CharacterAttr.MARISA

            case "2人":
                return CharacterAttr.TWO

            case "タイトル":
                return CharacterAttr.TITLE

            case "フェード":
                return CharacterAttr.FADE


class VideoPath:
    @staticmethod
    def get_path(video: VideoAttr) -> str:
        match video:
            case VideoAttr.BACKGROUND:
                return rf"{RESOURCE_PATH}\video\background.mp4"

            case VideoAttr.END:
                return rf"{RESOURCE_PATH}\video\ED.mp4"


class ImagePath:
    @staticmethod
    def get_path(image_attr: ImageAttr, num: int = 0) -> str:
        match image_attr:
            case ImageAttr.MATERIAL:
                img = glob.glob(rf"{PROJECT_PATH}\images\image{str(num).zfill(3)}*")
                # print(img)
                return img[0]

            case ImageAttr.BACKGROUND:
                return rf"{RESOURCE_PATH}\image\background.png"

            case ImageAttr.FADE:
                return rf"{RESOURCE_PATH}\image\blackout.png"


class AudioPath:
    @staticmethod
    def get_path(audio_attr: AudioAttr) -> str:
        match audio_attr:
            case AudioAttr.OPENING:
                return rf"{RESOURCE_PATH}\audio\opening.mp3"
            case AudioAttr.MAIN:
                return rf"{RESOURCE_PATH}\audio\main.mp3"
            case AudioAttr.SE:
                p = random.randint(1, 6)
                return rf"{RESOURCE_PATH}\audio\SE{p}.mp3"


class ItemDic:
    video = {
        "$type": "YukkuriMovieMaker.Project.Items.VideoItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "FilePath": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\固定アイテム\\ED.mp4",  # 変更
        "AudioTrackIndex": 0,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLooped": True,  # 変更
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 150.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [],
        "Group": 0,
        "Frame": 6127,  # 変更
        "Layer": 8,  # 変更
        "Length": 877,  # 変更
        "IsLocked": False,
        "IsHidden": False,
    }

    image = {
        "$type": "YukkuriMovieMaker.Project.Items.ImageItem, YukkuriMovieMaker",
        "FilePath": rf"{RESOURCE_PATH}\image\blackout.png",  # 変更
        "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},  # 変更
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [
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
        ],
        "Group": 0,
        "Frame": 6087,
        "Layer": 9,
        "Length": 80,
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": False,
        "IsHidden": False,
    }

    audio = {
        "$type": "YukkuriMovieMaker.Project.Items.AudioItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "FilePath": rf"{RESOURCE_PATH}\BGM_Start.mp3",  # 変更
        "AudioTrackIndex": 0,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "FadeIn": 0.0,
        "FadeOut": 1.0,
        "IsLooped": True,  # 変更
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "Group": 0,
        "Frame": 0,  # 変更
        "Layer": 14,  # 変更
        "Length": 2385,  # 変更
        "IsLocked": False,
        "IsHidden": False,
    }

    text = {
        "$type": "YukkuriMovieMaker.Project.Items.TextItem, YukkuriMovieMaker",
        "Text": "",  # 変更
        "Decorations": [],
        "Font": "UD デジタル 教科書体 NP-B",
        "FontSize": {"From": 70.0, "To": 1.0, "AnimationType": "なし", "Span": 0.0},
        "LineHeight2": {
            "From": 100.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "LetterSpacing2": {
            "From": -2.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "DisplayInterval": 0.0,
        "BasePoint": "LeftTop",
        "FontColor": "#FFFFFFFF",
        "Style": "Border",
        "StyleColor": "#FF000000",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "X": {"From": -932.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": -500.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [],
        "Group": 0,
        "Frame": 2385,
        "Layer": 7,
        "Length": 55,
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": True,
        "IsHidden": False,
    }

    voice_reimu = {
        "$type": "YukkuriMovieMaker.Project.Items.VoiceItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "CharacterName": "霊夢",
        "Serif": "こんばんわ\r\n、ゆっくり霊夢です。",  # ymmpから取得
        "Decorations": [],
        "Hatsuon": "こんばんわ、ゆっくり/れーむで_ス。",  # ymmpから取得
        "Pronounce": None,
        "VoiceLength": "00:00:01.8695000",  # ymmpから取得
        "VoiceCache": None,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "VoiceParameter": {
            "$type": "YukkuriMovieMaker.Voice.VoiceParameter, YukkuriMovieMaker",
            "Speed": 110,
        },
        "ContentOffset": "00:00:00",
        "VoiceFadeIn": 0.0,
        "VoiceFadeOut": 0.0,
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "JimakuVisibility": "UseCharacterSetting",
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "X": {"From": 380.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "JimakuFadeIn": 0.0,
        "JimakuFadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "Font": "けいふぉんと",
        "FontSize": {"From": 80.0, "To": 1.0, "AnimationType": "なし", "Span": 0.0},
        "LineHeight2": {
            "From": 125.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "LetterSpacing2": {
            "From": 0.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "DisplayInterval": 0.0,
        "BasePoint": "CenterCenter",
        "FontColor": "#FFFFFFFF",
        "Style": "Border",
        "StyleColor": "#FFFF0000",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "JimakuVideoEffects": [],
        "TachieFaceParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.FaceParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "EyeAnimation": "Default",
            "MouthAnimation": "Default",
            "Eyebrow": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\眉\\06.png",  # 変更
            "Eye": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\目\\@0疑問0.png",  # 変更
            "Mouth": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\口\\@0疑問07.png",  # 変更
            "Hair": None,
            "Complexion": None,
            "Body": None,
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "TachieFaceEffects": [],
        "Group": 0,
        "Frame": 0,  # 変更
        "Layer": 7,  # 変更
        "Length": 136,  # 変更
        "IsLocked": False,
        "IsHidden": False,
    }

    voice_marisa = {
        "$type": "YukkuriMovieMaker.Project.Items.VoiceItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "CharacterName": "魔理沙",
        "Serif": "魔理沙だぜ。",  # ymmpから取得
        "Decorations": [],
        "Hatsuon": "まりさだぜ。",  # ymmpから取得
        "Pronounce": None,
        "VoiceLength": "00:00:00.7317500",  # ymmpから取得
        "VoiceCache": None,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "VoiceParameter": {
            "$type": "YukkuriMovieMaker.Voice.VoiceParameter, YukkuriMovieMaker",
            "Speed": 110,
        },
        "ContentOffset": "00:00:00",
        "VoiceFadeIn": 0.0,
        "VoiceFadeOut": 0.0,
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "JimakuVisibility": "UseCharacterSetting",
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "X": {"From": 380.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "JimakuFadeIn": 0.0,
        "JimakuFadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "Font": "けいふぉんと",
        "FontSize": {"From": 80.0, "To": 1.0, "AnimationType": "なし", "Span": 0.0},
        "LineHeight2": {
            "From": 125.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "LetterSpacing2": {
            "From": 0.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "DisplayInterval": 0.0,
        "BasePoint": "CenterCenter",
        "FontColor": "#FFFFFFFF",
        "Style": "Border",
        "StyleColor": "#FF0000FF",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "JimakuVideoEffects": [],
        "TachieFaceParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.FaceParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "EyeAnimation": "Default",
            "MouthAnimation": "Default",
            "Eyebrow": None,  # 変更
            "Eye": None,  # 変更
            "Mouth": None,  # 変更
            "Hair": None,
            "Complexion": None,
            "Body": None,
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "TachieFaceEffects": [],
        "Group": 0,
        "Frame": 136,  # 変更
        "Layer": 7,  # 変更
        "Length": 68,  # 変更
        "IsLocked": False,
        "IsHidden": False,
    }

    tachie_marisa = {
        "$type": "YukkuriMovieMaker.Project.Items.TachieItem, YukkuriMovieMaker",
        "CharacterName": "魔理沙",
        "TachieItemParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.ItemParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "IsHiddenWhenNoSpeech": False,
            "Eyebrow": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\眉\\00.png",
            "Eye": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\目\\00.png",
            "Mouth": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\口\\00.png",
            "Hair": None,
            "Complexion": None,
            "Body": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\体\\00.png",
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "X": {"From": 750.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": -10.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 150.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [
            {
                "$type": "YukkuriMovieMaker.Project.Effects.RepeatMoveEffect, YukkuriMovieMaker",
                "Label": "反復移動 X0px, Y40px, 2.00秒",
                "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
                "Y": {"From": 40.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
                "Span": {
                    "From": 2.0,
                    "To": 0.0,
                    "AnimationType": "なし",
                    "Span": 0.0,
                },
                "EasingType": "Sine",
                "EasingMode": "InOut",
                "IsCentering": True,
                "IsEnabled": True,
            }
        ],
        "Group": 0,
        "Frame": 0,
        "Layer": 7,
        "Length": 56908,
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": False,
        "IsHidden": False,
    }

    tachie_reimu = {
        "$type": "YukkuriMovieMaker.Project.Items.TachieItem, YukkuriMovieMaker",
        "CharacterName": "霊夢",
        "TachieItemParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.ItemParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "IsHiddenWhenNoSpeech": False,
            "Eyebrow": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\眉\\00.png",
            "Eye": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\目\\00.png",
            "Mouth": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\口\\00.png",
            "Hair": None,
            "Complexion": None,
            "Body": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\体\\00.png",
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "X": {"From": -750.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": -10.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 150.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": True,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [
            {
                "$type": "YukkuriMovieMaker.Project.Effects.RepeatMoveEffect, YukkuriMovieMaker",
                "Label": "反復移動 X0px, Y40px, 2.00秒",
                "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
                "Y": {"From": 40.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
                "Span": {
                    "From": 2.0,
                    "To": 0.0,
                    "AnimationType": "なし",
                    "Span": 0.0,
                },
                "EasingType": "Sine",
                "EasingMode": "InOut",
                "IsCentering": True,
                "IsEnabled": True,
            }
        ],
        "Group": 0,
        "Frame": 0,
        "Layer": 6,
        "Length": 56908,
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": False,
        "IsHidden": False,
    }
    two_voice_reimu = {
        "$type": "YukkuriMovieMaker.Project.Items.VoiceItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "CharacterName": "霊夢",
        "Serif": "ご視聴ありがとうございました",
        "Decorations": [
            {
                "Start": 0,
                "Length": 14,
                "IsBold": False,
                "IsItalic": False,
                "Scale": 1.0,
                "Font": None,
                "Foreground": None,
                "IsLineBreak": False,
                "HasDecoration": False,
            }
        ],
        "Hatsuon": "ご_シちょー/ありがとー/ございま_シた",
        "Pronounce": None,
        "VoiceLength": "00:00:01.6902500",
        "VoiceCache": None,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "VoiceParameter": {
            "$type": "YukkuriMovieMaker.Voice.VoiceParameter, YukkuriMovieMaker",
            "Speed": 110,
        },
        "ContentOffset": "00:00:00",
        "VoiceFadeIn": 0.0,
        "VoiceFadeOut": 0.0,
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "JimakuVisibility": "Custom",
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "X": {"From": 320.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "JimakuFadeIn": 0.0,
        "JimakuFadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "Font": "けいふぉんと",
        "FontSize": {"From": 80.0, "To": 1.0, "AnimationType": "なし", "Span": 0.0},
        "LineHeight2": {
            "From": 125.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "LetterSpacing2": {
            "From": 0.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "DisplayInterval": 0.0,
        "BasePoint": "CenterCenter",
        "FontColor": "#FFFFFFFF",
        "Style": "Border",
        "StyleColor": "#FFFF0000",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "JimakuVideoEffects": [],
        "TachieFaceParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.FaceParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "EyeAnimation": "Default",
            "MouthAnimation": "Default",
            "Eyebrow": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\眉\\02.png",
            "Eye": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\目\\27.png",
            "Mouth": f"{os.path.expanduser('~')}\\\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Reimu\\口\\@4喜び05.png",
            "Hair": None,
            "Complexion": None,
            "Body": None,
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "TachieFaceEffects": [],
        "Group": 0,
        "Frame": 0,
        "Layer": 4,
        "Length": 119,
        "IsLocked": False,
        "IsHidden": False,
    }
    two_voice_marisa = {
        "$type": "YukkuriMovieMaker.Project.Items.VoiceItem, YukkuriMovieMaker",
        "IsWaveformEnabled": False,
        "CharacterName": "魔理沙",
        "Serif": "ご視聴ありがとうございました",
        "Decorations": [
            {
                "Start": 0,
                "Length": 14,
                "IsBold": False,
                "IsItalic": False,
                "Scale": 1.0,
                "Font": None,
                "Foreground": None,
                "IsLineBreak": False,
                "HasDecoration": False,
            }
        ],
        "Hatsuon": "ご_シちょー/ありがとー/ございま_シた",
        "Pronounce": None,
        "VoiceLength": "00:00:01.6902500",
        "VoiceCache": None,
        "Volume": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Pan": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "PlaybackRate": 100.0,
        "VoiceParameter": {
            "$type": "YukkuriMovieMaker.Voice.VoiceParameter, YukkuriMovieMaker",
            "Speed": 110,
        },
        "ContentOffset": "00:00:00",
        "VoiceFadeIn": 0.0,
        "VoiceFadeOut": 0.0,
        "EchoIsEnabled": False,
        "EchoInterval": 0.1,
        "EchoAttenuation": 40.0,
        "JimakuVisibility": "Custom",
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "X": {"From": 440.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "JimakuFadeIn": 0.0,
        "JimakuFadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": False,
        "IsClippingWithObjectAbove": False,
        "Font": "けいふぉんと",
        "FontSize": {"From": 80.0, "To": 1.0, "AnimationType": "なし", "Span": 0.0},
        "LineHeight2": {
            "From": 125.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "LetterSpacing2": {
            "From": 0.0,
            "To": 0.0,
            "AnimationType": "なし",
            "Span": 0.0,
        },
        "DisplayInterval": 0.0,
        "BasePoint": "CenterCenter",
        "FontColor": "#FFFFFFFF",
        "Style": "Border",
        "StyleColor": "#FF0000FF",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "JimakuVideoEffects": [],
        "TachieFaceParameter": {
            "$type": "YukkuriMovieMaker.Plugin.Tachie.AnimationTachie.FaceParameter, YukkuriMovieMaker.Plugin.Tachie.AnimationTachie",
            "EyeAnimation": "Default",
            "MouthAnimation": "Default",
            "Eyebrow": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\眉\\02.png",
            "Eye": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\目\\27.png",
            "Mouth": f"{os.path.expanduser('~')}\\works\\sumiwataturo\\YukkuriMovieMaker4\\Characters\\Marisa\\口\\@4喜び05.png",
            "Hair": None,
            "Complexion": None,
            "Body": None,
            "Back1": None,
            "Back2": None,
            "Back3": None,
            "Etc1": None,
            "Etc2": None,
            "Etc3": None,
        },
        "TachieFaceEffects": [],
        "Group": 0,
        "Frame": 0,
        "Layer": 5,
        "Length": 119,
        "IsLocked": False,
        "IsHidden": False,
    }

    mosaic_transition_in = {
        "$type": "YukkuriMovieMaker.Project.Items.FrameBufferItem, YukkuriMovieMaker",
        "ClearBackground": True,
        "IsAlphaEnabled": False,
        "IsFrameOutImageRenderingEnabled": False,
        "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": True,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [
            {
                "$type": "YukkuriMovieMaker.Project.Effects.InOutMosaicEffect, YukkuriMovieMaker",
                "Label": "モザイクをかけながら退場",
                "Value": 80.0,
                "IsInEffect": False,
                "IsOutEffect": True,
                "EffectTimeSeconds": 1.0,
                "EasingType": "Linear",
                "EasingMode": "Out",
                "IsEnabled": True,
            }
        ],
        "Group": 0,
        "Frame": 0,  # 変更
        "Layer": 0,  # 変更
        "Length": 45,  # 変更
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": False,
        "IsHidden": False,
    }

    mosaic_transition_out = {
        "$type": "YukkuriMovieMaker.Project.Items.FrameBufferItem, YukkuriMovieMaker",
        "ClearBackground": True,
        "IsAlphaEnabled": False,
        "IsFrameOutImageRenderingEnabled": False,
        "X": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Y": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Opacity": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Zoom": {"From": 100.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "Rotation": {"From": 0.0, "To": 0.0, "AnimationType": "なし", "Span": 0.0},
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsAlwaysOnTop": True,
        "IsClippingWithObjectAbove": False,
        "VideoEffects": [
            {
                "$type": "YukkuriMovieMaker.Project.Effects.InOutMosaicEffect, YukkuriMovieMaker",
                "Label": "モザイクを解除しながら登場",
                "Value": 80.0,
                "IsInEffect": True,
                "IsOutEffect": False,
                "EffectTimeSeconds": 1.0,
                "EasingType": "Linear",
                "EasingMode": "Out",
                "IsEnabled": True,
            },
        ],
        "Group": 0,
        "Frame": 45,  # 変更
        "Layer": 0,  # 変更
        "Length": 45,  # 変更
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "IsLocked": False,
        "IsHidden": False,
    }


class EmotionDic:
    @staticmethod
    def get_emotion(chara_attr: CharacterAttr, emotion: EmotionAttr) -> dict:
        match chara_attr:
            case CharacterAttr.REIMU:
                match emotion:
                    case EmotionAttr.LOVE:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\02.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\27.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@4喜び05.png",
                        }

                    case EmotionAttr.JOY:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\07.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@3楽しい10.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@3楽しい14.png",
                        }

                    case EmotionAttr.QUESTION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@0疑問0.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@0疑問07.png",
                        }

                    case EmotionAttr.EXCLAMATION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\01.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\05.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\00.png",
                        }
                    case EmotionAttr.FEAR:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@2恐怖06.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@2恐怖04.png",
                        }

                    case EmotionAttr.SADNESS:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@5泣く17.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@5泣く02.png",
                        }

                    case EmotionAttr.ANGER:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\00.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\16.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@2恐怖04.png",
                        }
                    case EmotionAttr.SILENT:
                        dic = {
                            "Eyebrow": None,
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\29.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\04.png",
                        }

            case CharacterAttr.MARISA:
                match emotion:
                    case EmotionAttr.LOVE:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\02.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\27.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@4喜び05.png",
                        }

                    case EmotionAttr.JOY:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\07.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\@3楽しい10.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@3楽しい14.png",
                        }

                    case EmotionAttr.QUESTION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\@0疑問0.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@0疑問07.png",
                        }

                    case EmotionAttr.EXCLAMATION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\01.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\05.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\00.png",
                        }
                    case EmotionAttr.FEAR:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\@2恐怖06.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@2恐怖04.png",
                        }

                    case EmotionAttr.SADNESS:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\04.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\@5泣く17.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@5泣く13.png",
                        }

                    case EmotionAttr.ANGER:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_MARISA}\眉\00.png",
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\16.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@2恐怖04.png",
                        }
                    case EmotionAttr.SILENT:
                        dic = {
                            "Eyebrow": None,
                            "Eye": rf"{EMOTION_PATH_MARISA}\目\29.png",
                            "Mouth": rf"{EMOTION_PATH_MARISA}\口\@2恐怖04.png",
                        }

            case CharacterAttr.TWO:
                dic = {
                    "Eyebrow": None,
                    "Eye": None,
                    "Mouth": None,
                }

            case CharacterAttr.TITLE:
                match emotion:
                    case EmotionAttr.LOVE:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\02.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\27.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@4喜び05.png",
                        }

                    case EmotionAttr.JOY:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\07.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@3楽しい10.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@3楽しい14.png",
                        }

                    case EmotionAttr.QUESTION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@0疑問0.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@0疑問07.png",
                        }

                    case EmotionAttr.EXCLAMATION:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\01.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\05.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\00.png",
                        }
                    case EmotionAttr.FEAR:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@2恐怖06.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@2恐怖04.png",
                        }

                    case EmotionAttr.SADNESS:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\06.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\@5泣く17.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@5泣く02.png",
                        }

                    case EmotionAttr.ANGER:
                        dic = {
                            "Eyebrow": rf"{EMOTION_PATH_REIMU}\眉\00.png",
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\16.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\@2恐怖04.png",
                        }
                    case EmotionAttr.SILENT:
                        dic = {
                            "Eyebrow": None,
                            "Eye": rf"{EMOTION_PATH_REIMU}\目\29.png",
                            "Mouth": rf"{EMOTION_PATH_REIMU}\口\04.png",
                        }

            case CharacterAttr.FADE:
                dic = {
                    "Eyebrow": None,
                    "Eye": None,
                    "Mouth": None,
                }

        return dic


def get_frame(item):
    return item["Frame"]
