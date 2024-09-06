# generate.py

## Table of Contents

1. [Overview](#overview)
2. [Specification](#specification)
3. [License](#license)
4. [Contact](#contact)

## Overview  
このスクリプトは、MicrosoftのText-to-Speech（音声合成）APIであるedge_ttsを使用して、指定されたテキストファイルをMP3形式の音声ファイルに変換するPythonスクリプトです。  
edge_ttsは、以下のページを参考にしてください。  
https://github.com/rany2/edge-tts  
https://pypi.org/project/edge-tts/  

特長は、.txtファイルを読み込み、指定された音声モデルを使用して音声合成を行い、MP3ファイルとして保存します。  
複数のテキストファイルを一度に処理できます。  

##  Installation  
このスクリプトを動作させるために、以下のパッケージをインストールする必要があります。
```bash
pip install edge_tts

