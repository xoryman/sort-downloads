#!/bin/python3

import os
from functools import partial
from tkinter import Tk, Button, messagebox

from convert import convert_webm_to_mp4
from preview import create_preview
from settings import VIDEO_PATH
from sort import sort_files


def main():
    """
    Входная функция программы.
    Выводит интерфейс для создания превью.
    """
    root = Tk()
    root.title("DPM by xoryman")

    videos = os.listdir(VIDEO_PATH)
    r = 0
    btns = []
    for video in videos:
        video_name, video_ext = os.path.splitext(video)
        if video_ext[1:] != 'mp4' or 'output' in video_name:
            continue
        btn = Button(root, text=video_name[:30], command=partial(create_preview, video))
        btn.grid(row=r, column=0)
        btns.append(btn)
        r += 1

    if not btns:
        messagebox.showerror('Ошибка', 'Видеозаписей не найдено.')
        root.destroy()

    root.mainloop()


if __name__ == '__main__':
    sort_files()
    convert_webm_to_mp4()
    main()
