'''
default (1, 1)
generating_strings - это функция для генирации случайной строки.
generating_strings(количества символов в строке, 1 - уквы + цифры / 2 - только буквы)
пример:
print(generating_strings(5))
>>>K4ef3
'''
local_how = 0


def generating_strings(size=1, what=1):
    import string
    from random import choice
    if what == 1:
        return ''.join(choice(string.ascii_letters + string.digits) for _ in range(size))
    else:
        return ''.join(choice(string.ascii_letters) for _ in range(size))


def potok(how, bar_finish):
    from random import randint
    from PIL import Image
    import requests
    from os import abort
    from io import BytesIO
    import cfg

    global local_how

    cfg.proxy_http = [line.rstrip() for line in cfg.proxy_http]
    cfg.proxy_socks = [line.rstrip() for line in cfg.proxy_socks]


    format_list = ['.jpg', '.png', '.gif', '.jpeg']
    check = True

    if local_how >= how:
        check = False
        abort()

    while check == True:
        try:
            if cfg.proxy_onner == True:
                if randint(1, 2) == 1:
                    cfg.proxy = {
                        'http': cfg.proxy_http[randint(0, len(cfg.proxy_http) - 1)]}
                else:
                    proxy = {'http': 'socks4://' +
                             cfg.proxy_socks[randint(0, len(cfg.proxy_socks) - 1)]}
            else:
                proxy = None

            string = generating_strings(6, 1)
            num_of_list = randint(0, 3)
            url = 'http://i.imgur.com/' + string + format_list[num_of_list]
            img = requests.get(url, proxies=proxy, timeout=5).content

            if (161, 81) != Image.open(BytesIO(img)).size:
                '''
                if check == False:
                    print(Style.BRIGHT + Fore.YELLOW + string + '.png' +
                          Fore.RESET + ' successfully found and saved ' + proxy)
                '''
                local_how += 1
                bar_finish.next()
                f = open('output/' + string + format_list[num_of_list], 'wb')
                f.write(img)
                f.close()
                
                # del f
                # del check
                # del img
                # del url
                # del string
                # del num_of_list
                # del proxy

                # break

        except:
            pass


def what_is_my_platform(ret=None):
    from sys import platform

    if platform == 'linux' or platform == 'linux2':
        if ret == 'clear':
            return 'clear'
        else:
            return 'Linux'


    elif platform == 'win32':
        if ret == 'clear':
            return 'cls'
        else:
            return 'Windows'
        
    elif platform == 'darwin':
        if ret == 'clear':
            return None
        else:
            return 'MacOS'