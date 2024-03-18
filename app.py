import os
import subprocess

def convert_heic_to_mov(input_dir, output_dir, finished_dir):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # finishedディレクトリが存在しない場合は作成
    if not os.path.exists(finished_dir):
        os.makedirs(finished_dir)

    # inputディレクトリのHEICファイル一覧を取得
    heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic')]
    
    # HEICファイルが見つからなかった場合
    if not heic_files:
        print("No HEIC files found in the input directory.")
        return

    # 各HEICファイルに対して変換処理
    for heic_file in heic_files:
        # 元のファイル名から拡張子を除いた名前を取得
        filename_without_ext = os.path.splitext(heic_file)[0]
        # 出力ファイル名を設定
        mov_file = f"{filename_without_ext}.mov"
        
        # ffmpegを使用してHEICをMOVに変換
        command = ['ffmpeg', '-i', os.path.join(input_dir, heic_file), '-vcodec', 'copy', '-acodec', 'copy', os.path.join(output_dir, mov_file)]
        subprocess.run(command)
        
        print(f"Converted {heic_file} to {mov_file}")

        # 変換が完了したファイルをfinishedディレクトリに移動
        os.rename(os.path.join(input_dir, heic_file), os.path.join(finished_dir, heic_file))

# スクリプトが置かれているディレクトリを基点にinput、output、finishedフォルダを指定
base_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(base_dir, 'input')
output_dir = os.path.join(base_dir, 'output')
finished_dir = os.path.join(base_dir, 'finished')

convert_heic_to_mov(input_dir, output_dir, finished_dir)
