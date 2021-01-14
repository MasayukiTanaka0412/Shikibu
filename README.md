# Shikibu
  
音声の書き起こしツールです。
  
Audio Transcriber Tool
  
## 環境設定

[Azure Speech to Text](https://azure.microsoft.com/ja-jp/services/cognitive-services/speech-to-text/)のインスタンスを作成しkeyをAZURE_SPEECH_KEYとして環境変数に設定します
  
Prepare [Azure Speech to Text](https://azure.microsoft.com/ja-jp/services/cognitive-services/speech-to-text/) instance and set its key into environmental variable AZURE_SPEECH_KEY
  
## 前処理 pre-process
  
事前にwavファイルに変換してください
  
Change file format into .wav

ex.
  
ffmpeg -i input.mp4 -ar 8000 output.wav