import os
import shutil

path = '/home/howtus/Загрузки'
list_of_files = os.listdir(path)

IMAGE_TYPES = [
    'png',
    'jpeg',
    'jpg',
    'bmp',
    'tiff',
    'gif',
    'ico',
    'svg',
    'webp',
]

VIDEO_TYPES = [
    'avi',
    'mp4',
    'mkv',
    'flv',
    'mpeg',
    'mov',
    '3gp',
    'wmw',
    'webm',
]

DOC_TYPES = [
    'docx',
    'doc',
    'pptx',
    'ppt',
    'xls',
    'xlsx',
    'odt',
    'ods',
    'odp',
    'txt',
    'rtf',
]


def get_file_type(file_ext):
    if file_ext in IMAGE_TYPES:
        return 'Images'
    if file_ext in VIDEO_TYPES:
        return 'Videos'
    if file_ext in DOC_TYPES:
        return 'Documents'
    return 'Others'


def convert_webm_to_mp4():
    webm_path = path + '/Videos'

    if not os.path.exists(webm_path):
        print("No Videos directory!")
        return

    list_of_webm = os.listdir(webm_path)

    for webm in list_of_webm:
        webm_name, webm_ext = os.path.splitext(webm)
        print(webm)
        if not webm_ext[1:] == 'webm':
            continue

        os.system(f'ffmpeg -i {webm_path}/"{webm}" -q:v 1 -hide_banner {webm_path}/"{webm_name}".mp4')
        os.remove(webm_path + '/' + webm)


# Проходим по списку всех файлов в каталоге
for file in list_of_files:
    # Получаем имя файла и его расширение
    name, ext = os.path.splitext(file)
    # Убираем точку из расширения
    ext = ext[1:]
    # Пропускаем папки
    if ext == '':
        continue
    # Проверяем к какому типу файлов относится данный
    file_type = get_file_type(ext)
    # Создаем каталог если его не существует
    if not os.path.exists(path + '/' + file_type):
        os.makedirs(path + '/' + file_type)
    # Перемещаем туда файл
    shutil.move(path + '/' + file, path + '/' + file_type + '/' + file)


if input("Convert all .webm videos to .mp4? [y/n] ") == 'y':
    convert_webm_to_mp4()
