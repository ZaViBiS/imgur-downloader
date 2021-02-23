import sys

sys.path.append('source')  # Добовление дериктории импорта

from progress.bar import *
from colorama import *
import cfg
import lib
import threading
import time
import os



# --- Начала замера скорости выполнения --- #
start = time.time()

init() # инициализация colorama'ы

# --- Сколько нужно фото --- #
print('How many photos do I need to download:' + Style.BRIGHT + Fore.CYAN) # Жилаемое количество скачаных файлов
how = int(input())
print(Fore.RESET)

# --- Полоска готовности --- #
bar_finish = ShadyBar(Style.BRIGHT + Fore.YELLOW + 'successfully downloaded', max=how)

# --- Если proxy включены читает их из файлаов --- #
if cfg.proxy_onner == True:
    for x in open('source/http.txt'):
        cfg.proxy_http.append(x)

    for x in open('source/socks.txt'):
        cfg.proxy_socks.append(x)

    cfg.proxy_http = [line.rstrip() for line in cfg.proxy_http]
    cfg.proxy_socks = [line.rstrip() for line in cfg.proxy_socks]
# --- ^ = + = ^ --- #

# --- Проверка на наличеи выходной дериктории --- #
for x in os.listdir():
    if x == 'output':
        cfg.there_is = True


# --- Создание выходной дериктории ( Если её нет ) --- #
if cfg.there_is != True:
    os.mkdir('output')

# --- Очистка экрана --- #
os.system(lib.what_is_my_platform('clear'))


# --- Вывод информации --- #
print(
'''proxy:{0}
OS:{1}
thread:{2}'''.format(cfg.proxy_onner, lib.what_is_my_platform(), cfg.max_thread))

# --- Запуск потоков --- #
for x in range(cfg.max_thread):
    threading.Thread(target=lib.potok, args=(how, bar_finish, )).start()
    if lib.local_how >= how:
        break

print('\n\n')

# Количество секунд затраченое на выполнение
while len(threading.enumerate()) != 1:
    time.sleep(0.1)

    if lib.local_how >= how:
        break


# --- Вывод затраченого времени --- #
print(Fore.RESET + '\n\n[Finished in ' + Style.BRIGHT + Fore.YELLOW + str(round(time.time() - start, 2)) + Fore.RESET + 's]')


os.abort() # Завиршение
