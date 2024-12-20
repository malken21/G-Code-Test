import os


def is_utf8(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False


# 現在のディレクトリを取得
current_directory = os.getcwd()

# ディレクトリ内のファイルをループ
for filename in os.listdir(current_directory):
    if filename.endswith(".ncc"):
        # ファイルパスを生成
        file_path = os.path.join(current_directory, filename)

        # ファイルが UTF-8 の場合はスキップ
        if is_utf8(file_path):
            print(f"Skipping {filename} (already UTF-8)")
            continue

        # ファイルを Shift_JIS で読み込み
        with open(file_path, "r", encoding="shift_jis") as file:
            content = file.read()

        # ファイルを UTF-8 で書き込み
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Converted {filename} to UTF-8")
