import os

from settings import (
    VIDEO_PATH,
)


def convert_webm_to_mp4():
    """
    Конвентирует все webm видео в mp4.
    """
    if not os.path.exists(VIDEO_PATH):
        return

    list_of_videos = os.listdir(VIDEO_PATH)
    for video in list_of_videos:
        video_name, video_extension = os.path.splitext(video)
        if video_extension[1:] != 'webm':
            continue
        os.system(
            'ffmpeg -i "{path}/{video}" -q:v 1 -hide_banner "{path}/{video_name}.mp4"'.format(
                path=VIDEO_PATH,
                video=video,
                video_name=video_name
            )
        )
        os.remove(os.path.join(VIDEO_PATH, video))
