import pickle
import os


def main():
    if os.path.isfile("client.pickle"):
        print("フォルダ名を入力してください。")
        name = input()
        with open("client.pickle", "rb") as f:
            client = pickle.load(f)

    else:
        print("初期設定を行います。クライアント様の名前を記入してください。")
        with open("client.pickle", "wb") as f:
            client = input()
            pickle.dump(client, f)
            print("初期設定が完了しました。")
        print("")
        print("引き続き、今から編集するフォルダ名を入力してください。")
        name = input()

    return name, client
