import os
import shutil
from pathlib import Path

from settings import (
    IMAGE_TYPES,
    VIDEO_TYPES,
    DOC_TYPES,
    MUSIC_TYPES,
    PATH,
    IMAGE_PATH,
    VIDEO_PATH,
    DOC_PATH,
    MUSIC_PATH,
    OTHER_PATH,
)


def get_file_type(file_ext):
    """
    Принимает на вход расширение файла.
    Возвращает название подпапки, в которую переместить файл.
    """
    if file_ext in IMAGE_TYPES:
        return IMAGE_PATH
    if file_ext in VIDEO_TYPES:
        return VIDEO_PATH
    if file_ext in DOC_TYPES:
        return DOC_PATH
    if file_ext in MUSIC_TYPES:
        return MUSIC_PATH
    return OTHER_PATH


def sort_files():
    """
    Берет все файлы из корня папки загрузок и распределяет их по подпапкам.
    """
    list_of_files = os.listdir(PATH)
    for file in list_of_files:
        file_name, extension = os.path.splitext(file)
        extension = extension[1:]
        if extension == '':
            continue
        file_type = get_file_type(extension)
        Path(os.path.join(PATH, file_type)).mkdir(parents=True, exist_ok=True)
        shutil.move(os.path.join(PATH, file), os.path.join(PATH, file_type, file))
