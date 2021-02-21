import os
import subprocess
import datetime
from functools import partial
from tkinter import *
from PIL import ImageTk, Image

from settings import VIDEO_PATH, PREVIEW_COUNT


def create_preview(video):
    """
    Создает окно выбора превью. При нажатии на превью вызывает btn_click.
    После этого уничтожает видео.
    """
    # ex. video = 'name.mp4'
    video_len = datetime.timedelta(seconds=get_video_length(os.path.join(VIDEO_PATH, video)))
    parts = video_len / (PREVIEW_COUNT + 1)
    previews = {}
    for i in range(1, PREVIEW_COUNT + 1):
        time = str(parts * i)
        image = '{}/preview_{}_{}.jpg'.format(VIDEO_PATH, video, i)
        subprocess.run(['ffmpeg', '-y', '-hide_banner', '-ss', time, '-i', '%s/%s' % (VIDEO_PATH, video), '-qmin', '1',
                        '-q:v', '1', '-qscale:v', '2', '-frames:v', '1', '-huffman', 'optimal', image])
        previews[image] = time

    root = Toplevel()
    root.title("Previews for %s" % video)

    c = r = 0
    images = []
    for p, t in previews.items():
        img = ImageTk.PhotoImage(Image.open(p).resize((320, 180), Image.BICUBIC))
        images.append(img)

        btn = Button(root, image=img, command=partial(btn_click, t, video, previews, root))
        btn.grid(column=c, row=r)

        c += 1
        if c // 4 != 0:
            r += 1
            c = 0

    root.mainloop()


def btn_click(time, video, previews, root):
    """
    Создает превью для выбранного таймкода, конвертирует превью и исходное видео в форматы ts.
    Затем склеивает .ts файлы и конвертирует в mp4. Исходный файл, превью и ts файлы удаляются.
    """
    video_name, video_ext = os.path.splitext(video)
    preview_video_path = '%s/preview_%s' % (VIDEO_PATH, video)
    preview_ts_path = '%s/mov1_%s.ts' % (VIDEO_PATH, video_name)
    video_ts_path = '%s/mov2_%s.ts' % (VIDEO_PATH, video_name)
    video_output_path = '%s/output_%s.mp4' % (VIDEO_PATH, video_name)

    # Создаю видео для превью длиной в 1 кадр
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-i', os.path.join(VIDEO_PATH, video), '-ss', time, '-t',
                    '00:00:00.01', preview_video_path])
    # Создаю .ts файл для превью
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-i', preview_video_path, '-acodec', 'copy', '-vcodec', 'copy',
                    '-vbsf', 'h264_mp4toannexb', '-f', 'mpegts', preview_ts_path])
    # Создаю .ts файл для исходного видео
    subprocess.run(['ffmpeg', '-y', '-hide_banner', '-i', os.path.join(VIDEO_PATH, video), '-acodec', 'copy',
                    '-vcodec', 'copy', '-vbsf', 'h264_mp4toannexb', '-f', 'mpegts', video_ts_path])
    # Склеиваю .ts файлы и конвертирую в .mp4
    os.system('ffmpeg -y -hide_banner -i "concat:%s|%s" -vcodec copy -acodec copy %s' % (
        preview_ts_path,
        video_ts_path,
        video_output_path
    ))
    # Удаляю все служебные файлы
    os.remove(preview_video_path)
    os.remove(preview_ts_path)
    os.remove(video_ts_path)
    os.remove(os.path.join(VIDEO_PATH, video))
    for p, t in previews.items():
        os.remove(p)

    root.destroy()


def get_video_length(filename):
    """
    Возвращает длину видео в секундах.
    """
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)
