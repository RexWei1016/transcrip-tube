# YouTube 影片轉錄工具

這是一個用於下載 YouTube 影片音訊並進行語音轉錄的 Python 工具。該工具使用 Whisper 模型進行語音識別，並能夠保持原始時間戳記。

## 功能特點

- 從 YouTube 下載音訊
- 音訊分段處理
- 使用 Whisper 進行語音轉錄
- 保持原始時間戳記
- 支援中文轉錄
- 可打包成獨立執行檔 (.exe)

## 系統需求

- Python 3.x
- FFmpeg
- Whisper 模型

## 安裝步驟

1. 克隆此專案：
```bash
git clone [repository_url]
cd youtube_transcriber
```

2. 安裝所需套件：
```bash
pip install -r requirements.txt
```

3. 確保 FFmpeg 已安裝並在系統 PATH 中，或將 FFmpeg 執行檔放在 `tool/` 目錄下。

## 使用方式

### 方法一：直接執行 Python 程式

1. 執行主程式：
```bash
python main.py
```

2. 輸入 YouTube 影片網址
3. 等待程式處理完成

### 方法二：使用打包後的執行檔 (.exe)

1. 安裝打包工具：
```bash
pip install pyinstaller
```

2. 執行打包命令：
```bash
pyinstaller --onefile --add-data "tool/*;tool/" main.py
```

3. 打包完成後，執行檔將位於 `dist` 目錄中
4. 直接雙擊 `main.exe` 即可執行

注意：打包後的執行檔會包含所有必要的依賴項，但檔案大小會較大。

## 專案結構

```
youtube_transcriber/
├── main.py              # 主程式
├── config.py            # 設定檔
├── tool/                # 工具目錄（包含 FFmpeg）
├── utils/               # 工具函數
├── downloader/          # 下載相關模組
├── audio_processing/    # 音訊處理模組
└── transcription/       # 轉錄相關模組
```

## 配置參數說明

在 `config.py` 中可以調整以下參數：

- `OUTPUT_AUDIO_FILE`: 輸出音訊檔案的名稱（不含副檔名）
- `SAMPLED_AUDIO_FILE`: 抽樣處理後的音訊檔案名稱
- `SEGMENT_LEN_MS`: 音訊分段長度（毫秒），預設為 5000ms（5秒）
- `SAMPLE_PORTION`: 音訊抽樣比例，預設為 0.25（25%）

## 處理流程

1. 下載 YouTube 影片音訊
2. 切割音訊成多個片段
3. 對片段進行抽樣處理
4. 使用 Whisper 進行語音轉錄
5. 回推原始時間戳記

## 注意事項

- 請確保有足夠的網路頻寬下載影片
- 轉錄過程可能需要較長時間，取決於音訊長度
- 建議使用 GPU 加速轉錄過程
- 打包成 .exe 時，請確保 `tool` 目錄中的 FFmpeg 執行檔已包含在內
- 打包後的執行檔首次執行可能需要較長時間載入

## 授權

[請在此處添加授權資訊]

## 貢獻

歡迎提交 Pull Request 或提出 Issue。 