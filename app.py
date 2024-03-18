import os
import subprocess

def convert_heic_to_mov(directory):
    # 指定ディレクトリのHEICファイル一覧を取得
    heic_files = [f for f in os.listdir(directory) if f.lower().endswith('.heic')]
    
    # HEICファイルが見つからなかった場合
    if not heic_files:
        print("No HEIC files found in the directory.")
        return

    # 各HEICファイルに対して変換処理
    for heic_file in heic_files:
        # 元のファイル名から拡張子を除いた名前を取得
        filename_without_ext = os.path.splitext(heic_file)[0]
        # 出力ファイル名を設定
        mov_file = f"{filename_without_ext}.mov"
        
        # ffmpegを使用してHEICをMOVに変換
        command = ['ffmpeg', '-i', os.path.join(directory, heic_file), '-vcodec', 'copy', '-acodec', 'copy', os.path.join(directory, mov_file)]
        subprocess.run(command)
        
        print(f"Converted {heic_file} to {mov_file}")

# 現在のディレクトリを指定して関数を呼び出す
convert_heic_to_mov('.')
