## ScrSt (ScreenShots)

Аплоад скриншотов в Amazon S3 и красивое отображение их на странице.


### Зачем это всё?

1. На данный момент времени (июнь 2015) предлагаемый скрипт - единственный способ обмениться скриншотами, сделанными на макбуках с ретиной, с нормальным отображением полученных изображений как на обычных экранах, так и на ретине.

2. Кроме того, здесь нет никакой рекламы, а в браузере не отображается ничего, кроме сделанного скриншота - никаких лишних панелей на полэкрана, никакой бесполезной информации.

3. Ещё скрипт умеет Open Graph и полученный скриншот нормально отображается, например, в Facebook или Slack. Имеется возможность задать любое название полученному скриншоту.

4. Just for fun (проект выходного дня).


### Минусы, подводные камни

1. Нет аннотаций скриншотов с помощью стрелок, подписей и прочей графики. Пока нет.

2. Нужен аккаунт в Amazon S3 и хостинг для запуска фронтенда для отображения скриншотов.

3. Всё. Остальное - сплошной профит!


### Установка

1. Ставим скрипт:

		brew install dreadatour/formulas/scrst

2. Настраиваем:

		➜ /usr/local/bin/scrst --setup
		Amazon S3 configuration
		-----------------------
		Access key ID: BURD4JFDIW19HU2CGHN6
		Secret access key: Edj3LXlBnyStd0A6LVEwQzeCAwyDjzDCkiWVyTgr
		Bucket name: scrst

		ScrSt configuration
		-------------------
		Enter URL for uploaded screenshots: http://scr.st/
		Use long names for taken screenshots (true/false): false
		Keep file extension un result URL (true/false): false

	При необходимости настройки можно изменить в файле `/usr/local/etc/scrst.cfg`.

	По идее, всё уже работает, но если нужна интеграция с OS X (горячие кнопки) и Dropzone - читаем дальше.

3. Скачиваем и распаковываем архив с программой: https://github.com/dreadatour/scrst/archive/master.zip

4. Устанавливаем системные сервисы для запуска скрипта с помощью горячих клавиш. Для этого открываем в `Finder` папку `services` из скачанного архива и на каждом из сервисов делаем двойной клик и нажимаем <kbd>Установить</kbd> в появившемся окне:

	![Install service](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/service-install.png)

	После установки всех сервисов переходим в настройки клавиатуры и настраиваем горячие кнопки для вызова скрипта:

	![Setup shortcuts](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/setup-shortcuts.png)

5. Для того, чтобы добавить действие по загрузке файла через [Dropzone 3](https://aptonic.com/dropzone3/) нужно сделать двойной клик на `screenshot.dzbundle` в скачанной папке:

	![Setup dropzone action](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/dropzone.png)


### Использование

0. Параметры командной строки скрипта для загрузки скриншотов:

		➜ /usr/local/bin/scrst --help
		usage: scrst [-h] [-c CONFIG] [-s] [-a] [-t TITLE] [-r] [-q] [-v] [image_file]

		Screenshot uploader

		positional arguments:
		  image_file

		optional arguments:
		  -h, --help            show this help message and exit
		  -c CONFIG, --config CONFIG
		                        config file, default: /usr/local/etc/scrst.cfg
		  -s, --setup           run interactive setup
		  -a, --ask-title       ask user for screenshot title before upload
		  -t TITLE, --title TITLE
		                        screenshot title
		  -r, --rename-last-screenshot
		                        rename last uploaded screenshot
		  -q, --quiet           do not show OS X notify
		  -v, --verbose         verbose output

1. Пробуем запустить без параметров:

		/usr/local/bin/scrst

	Или нажимаем сочетание клавиш <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>5</kbd>.

	Выделяем область экрана. Скриншот загрузится на сервер AWS S3, ссылка на него будет скопирована в буфер обмена и появится нотифай об успешно загруженном файле:

	![Notify](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/notify.png)

	Если кликнуть по нотифаю - в браузере откроется страница с загруженным скриншотом.

	В консоли будет выведена информация о загруженном скриншоте:

		➜ /usr/local/bin/scrst
		Screenshot uploaded: http://scr.st/yfcmt1

2. Для того, чтобы задать название загруженному файлу, добавляем параметр `--ask-title`:

		/usr/local/bin/scrst --ask-title

	Или нажимаем сочетание клавиш <kbd>Cmd</kbd>+<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>5</kbd>.

	Выделяем область экрана. Появится окно с предложением ввести название для снятого скриншота:

	![Enter title](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/title-enter.png)

	После нажатия на кнопку <kbd>OK</kbd> будет показан нотифай об успешно загруженном файле:

	![Notify with title](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/notify-title.png)

3. Для того, чтобы переименовать последний загруженный скриншот, добавляем параметр `--rename-last-screenshot`:

		/usr/local/bin/scrst --rename-last-screenshot

	Или нажимаем сочетание клавиш <kbd>Cmd</kbd>+<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>5</kbd>.

	Появится окно с предложением изменить название последнего загруженного скриншота:

	![Edit title](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/title-edit.png)

	После нажатия на кнопку <kbd>OK</kbd> будет показан нотифай об успешно изменённом названии:

	![Notify with title edited](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/notify-title-edit.png)

4. Для загрузки существующего файла без уведомлений о загрузке с указанием названия, добавляем параметры `--quiet` и `--title` и указываем имя файла, который нужно загрузить:

		➜ /usr/local/bin/scrst --quiet --title "Киска" ~/Desktop/image.png
		File uploaded: http://scr.st/GdrN36

5. Если установлен Dropzone и действие для него, можно просто перетащить любую картинку на иконку "Scr.st" в окне Dropzone:

	![Dropzone window](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/dropzone-window.png)

	И она автоматичеки будет загружена.


### Запускаем фронтенд для отображения скриншотов

1. Клонируем репозиторий:

		git clone git@github.com:dreadatour/scrst.git
        cd scrst/frontend

2. Создаём virtualenv:

        mkvirtualenv scrst

3. Ставим зависимости:

        pip install -r requirements.txt

4. Создаём и редактируем конфиг (задаём название bucket в Amazon S3):

		cp config.py-dist config.py
		vim config.py

5. Запускаем:

        python app.py

6. Открываем в браузере: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
7. Открываем закачанный скриншот, например: [http://127.0.0.1:5000/LUzCJo](http://127.0.0.1:5000/LUzCJo) (где `LUzCJo.png` - название файла, сгенерированного скриптом scrst).
8. ...
9. Profit!

	![Browser window](https://raw.githubusercontent.com/dreadatour/scrst/master/screenshots/browser.png)
