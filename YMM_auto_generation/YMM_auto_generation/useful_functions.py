def remove_new_line(text: str) -> str:
    return text.replace("\r", "").replace("\n", "")


def last_one(iterable):
    """与えられたイテレータブルオブジェクトの
    最後の一つの要素の時にTrue、それ以外の時にFalseを返す

    ex.
    for i, is_last in last_one(range(5)):
        print(i, is_last)

    # 0, False
    # 1, False
    # 2, False
    # 3, False
    # 4, True
    """
    # イテレータを取得して最初の値を取得する
    it = iter(iterable)
    last = next(it)
    # 2番目の値から開始して反復子を使い果たすまで実行
    for val in it:
        # 一つ前の値を返す
        yield last, False
        last = val  # 値の更新
    # 最後の一つ
    yield last, True
