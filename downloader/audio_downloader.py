import os
import yt_dlp
from config import OUTPUT_AUDIO_FILE

def download_audio(youtube_url: str) -> str:
    if os.path.exists(OUTPUT_AUDIO_FILE):
        os.remove(OUTPUT_AUDIO_FILE)
        print(f"🧹 已刪除舊檔案：{OUTPUT_AUDIO_FILE}")

    # 動態推算 ffmpeg 路徑（根目錄的 /tool 資料夾）
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ffmpeg_dir = os.path.join(project_root, "tool")

    ffmpeg_exe = os.path.join(ffmpeg_dir, "ffmpeg.exe")
    ffprobe_exe = os.path.join(ffmpeg_dir, "ffprobe.exe")

    # 安全檢查
    if not (os.path.exists(ffmpeg_exe) and os.path.exists(ffprobe_exe)):
        raise FileNotFoundError("❌ 找不到 ffmpeg.exe 或 ffprobe.exe，請確認已放入 tool 資料夾")

    print("🔧 使用內建 ffmpeg 路徑：", ffmpeg_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': OUTPUT_AUDIO_FILE,
        'ffmpeg_location': ffmpeg_dir,  # yt-dlp 會自動從這裡找 ffmpeg & ffprobe
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    print("🎧 開始下載音訊（使用專案內 tool/ffmpeg）...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    final_file = OUTPUT_AUDIO_FILE + ".mp3"
    print("✅ 音訊下載完成：", final_file)
    return final_file
