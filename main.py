from downloader.audio_downloader import download_audio
from audio_processing.segmenter import split_audio
from audio_processing.sampler import sample_segments
from transcription.whisper_transcriber import transcribe_with_original_time
import os
import sys

# 設定 tool/ 路徑進 PATH，讓 whisper 可以呼叫 ffmpeg
tool_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "tool"))
os.environ["PATH"] = f"{tool_dir};{os.environ['PATH']}"

def main():
    youtube_url = input("請輸入 YouTube 影片網址：")

    # [1] 下載音訊
    audio_path = download_audio(youtube_url)
    print("[1] 音訊下載完成")

    # [2] 切割音訊
    segments, duration_ms = split_audio(audio_path)

    # [3] 抽樣 + 匯出 mp3 + 建立對應表
    sampled_path, segment_offset_map = sample_segments(segments, duration_ms)

    # [4] Whisper 轉錄 + 回推原始時間
    print("[2] 開始 Whisper 轉錄...")
    transcribe_with_original_time(sampled_path, segment_offset_map)

if __name__ == "__main__":
    main()
