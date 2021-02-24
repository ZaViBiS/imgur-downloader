# installation
pip install -r requirements.txt

# using
```console
py main.py
How many photos do I need to download:
1000
```

```console
proxy:True
OS:Windows
thread:100



successfully downloaded |░                               | 12/1000
```
# requirements

* requests
* pysocks
* colorama
* progress
* Pillow


# customization
```python3
# --- Можно настраевать --- #
max_thread = 100 # количествор потоков работы
proxy_onner = True # True - использовать proxy ( Нужен файл со списком proxy ) | False - Не использовать


# --- Переменные --- #
there_is = False
proxy_http = []
proxy_socks = []

```