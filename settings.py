import os

# Путь до папки, которую нужно отсортировать
PATH = '/home/howtus/Загрузки'

# Пути до подпапок
IMAGE_PATH = os.path.join(PATH, 'Images')
VIDEO_PATH = os.path.join(PATH, 'Videos')
DOC_PATH = os.path.join(PATH, 'Documents')
MUSIC_PATH = os.path.join(PATH, 'Music')
OTHER_PATH = os.path.join(PATH, 'Others')

# Количество превьюх на экране
PREVIEW_COUNT = 16

# Списки типов расширений для разных видов файлов
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
    'pdf',
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

MUSIC_TYPES = [
    'mp3',
    'flac',
    'wav',
    'ogg',
]
