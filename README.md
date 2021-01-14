# Shikibu
  
音声の書き起こしツールです。
  
Audio Transcriber Tool
  
## 環境設定 Environment Setup

[Azure Speech to Text](https://azure.microsoft.com/ja-jp/services/cognitive-services/speech-to-text/)のインスタンスを作成しkeyをAZURE_SPEECH_KEYとして環境変数に設定します
  
Prepare [Azure Speech to Text](https://azure.microsoft.com/ja-jp/services/cognitive-services/speech-to-text/) instance and set its key into environmental variable AZURE_SPEECH_KEY
  
## 前処理 pre-process
  
事前にwavファイルに変換してください
  
Change file format into .wav

ex.
  
ffmpeg -i input.mp4 -ar 16000 output.wav
  
## 実行 Execution

wavファイルをdistディレクトリに配置

place wav file into dist directory 
  
dist/runShikubu.bat にwavファイルをドラッグアンドドロップ
  
Drag & drop .wav file onto dist/runShikubu.bat
  