# generate.py

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Specification](#specification)
4. [Thanks](#thanks)
5. [License](#license)
6. [Contact](#contact)

## Overview  
このスクリプトは、MicrosoftのText-to-Speech（音声合成）APIであるedge_ttsを使用して、指定されたテキストファイルをMP3形式の音声ファイルに変換するPythonスクリプトです。  
.txtファイルを読み込み、指定された音声モデルを使用して音声合成を行い、MP3ファイルとして保存します。  
複数のテキストファイルを一度に処理できます。  
<br>
edge_ttsは、以下のページを参考にしてください。  
https://github.com/rany2/edge-tts  
https://pypi.org/project/edge-tts/ 

##  Installation  
動作環境は以下のとおりです。  
- Python 3.7以上
- `edge_tts` パッケージ
  
このスクリプトを動作させるためには、以下のパッケージをインストールする必要があります。
```bash
pip install edge_tts
```

## Specification

### 単一のテキストファイルを変換する
以下のコマンドを実行すると、`example.txt` が音声に変換され、`example.mp3` というファイルが生成されます。
```bash
./generate.py example.txt
```
これにより、`sample.txt` が `sample.mp3` に変換されます。

### 複数のテキストファイルを変換する
ワイルドカードを使用して複数のファイルを指定することもできます。例えば、カレントディレクトリ内のすべての `.txt` ファイルを変換する場合は、以下のコマンドを使用します。
```bash
./generate.py *.txt
```
このコマンドは、ディレクトリ内のすべての `.txt` ファイルを対応する `.mp3` ファイルに変換します。

## Thanks
https://github.com/rany2/edge-tts

## License  
© TOYO Corporation  
Licensed under the [GPL-3.0](https://github.com/synesis-toyo/generate?tab=GPL-3.0-1-ov-file)

## Contact
https://www.synesis.tech/  
[synesis-globalsales@toyo.co.jp](<mailto:synesis-globalsales@toyo.co.jp>)  
<br>
以下のページこのスクリプトのサンプル音声が掲載されています。（日本語）  
https://www.toyo.co.jp/onetech_blog/articles/detail/id=38865
