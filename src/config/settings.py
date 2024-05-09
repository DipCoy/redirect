import os

from redirect.storages.dummy import DictStorage

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

storage = DictStorage(default_destination='https://google.com')
storage.set('ya', 'https://ya.ru')
