#!/usr/bin/env python3

"""
./generate.py xxxx.txt -> xxxx.mp3
./generate.py *.txt -> xxxx.mp3, yyyy.mp3

"""

from typing import List
import edge_tts

import asyncio
import os
import sys

VOICE = "en-GB-SoniaNeural"

async def save(filename: str) -> None:
    """Main function"""
    base = os.path.splitext(filename)[0]
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(base + ".mp3")

async def main(files: List[str]):
    tasks = [save(filename) for filename in files]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    args = sys.argv
    del args[0]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(args))
    finally:
        loop.close()
