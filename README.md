# edge-tts-generate.py

<!-- TOC -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#thanks">Thanks</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## Description  
このスクリプトは、MicrosoftのText-to-Speech（音声合成）APIであるedge_ttsを使用して、指定されたテキストファイルをMP3形式の音声ファイルに変換するPythonスクリプトです。  
.txtファイルを読み込み、指定された音声モデルを使用して音声合成を行い、MP3ファイルとして保存します。  
複数のテキストファイルを一度に処理できます。  
<br>
edge_ttsは、以下のページを参考にしてください。  
https://github.com/rany2/edge-tts  
https://pypi.org/project/edge-tts/ 

##  Installation  
動作環境は以下のとおりです。  
- Python>=3.7
- `edge_tts` パッケージ
  
このスクリプトを動作させるためには、以下のパッケージをインストールする必要があります。
```bash
pip install edge_tts
```

## Usage  

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

### 使用する音声の変更  
デフォルトの音声は、`en-US-AriaNeural` が使用されています。異なる音声を使用する場合は、`VOICE` 変数を変更します。

```python
...
VOICE = "supported voice"
...
```
<br>
なお音声は、以下のコマンドで確認できます。英語だけでなく、多様な言語がサポートされています。  

```bash
edge-tts -l
```

## Thanks
https://github.com/rany2/edge-tts

## License  
© TOYO Corporation  
Licensed under the [GPL-3.0](https://github.com/synesis-toyo/generate?tab=GPL-3.0-1-ov-file)

## Contact
https://www.toyo.co.jp/ict/products/detail/synesis.html  
[synesis-globalsales@toyo.co.jp](<mailto:synesis-globalsales@toyo.co.jp>)  
<br>
以下のブログ記事にこのスクリプトのサンプル音声が掲載されています。（日本語）  
https://www.toyo.co.jp/ict/casestudy/detail/id=42440
