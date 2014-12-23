## S5 (Amazon Simple Storage Service ScreenShots)

Аплоад скриншотов в Amazon S3 и красивое отображение их на странице.

Just for fun (проект выходного дня).


### Настраиваем отправку скриншотов

1. Ставим зависимости:

		brew install s3cmd terminal-notifier

2. Ставим скрипт для отправки скриншотов:

		wget -O /usr/local/bin/s5 https://raw.githubusercontent.com/dreadatour/s5/master/bin/s5
		chmox +x /usr/local/bin/s5

3. Прописываем в конфиг (/usr/local/etc/s5.conf) правильные параметры:

		AWS_S3_BUCKET_NAME='Your Amazon S3 bucket name'
		AWS_ACCESS_KEY_ID='Your Amazon S3 access key ID'
		AWS_SECRET_ACCESS_KEY='Your Amazon S3 secret access key'
		S5_URL='Your S5 installation domain name'

4. Пробуем запустить:

		/usr/local/bin/s5

	Выделяем область экрана. Скриншот должен залиться на сервер AWS S3 и должен появиться нотифай об успешно загруженном скриншоте:

	![Notify](https://raw.githubusercontent.com/dreadatour/s5/master/notify.png)


### Создаём сервис и назначаем горячие клавиши

1. Запускаем Automator.

2. Выбираем шаблон "Service":

	![Template](https://raw.githubusercontent.com/dreadatour/s5/master/choose-template.png)

3. Добавляем действие "Run Shell Script":

	![Add action](https://raw.githubusercontent.com/dreadatour/s5/master/add-action.png)

4. Создаём действие:

	![Create action](https://raw.githubusercontent.com/dreadatour/s5/master/create-action.png)

5. Сохраняем:

	![Save action](https://raw.githubusercontent.com/dreadatour/s5/master/save-action.png)

6. Назначаем сочетание клавиш:

	![Shortcut](https://raw.githubusercontent.com/dreadatour/s5/master/set-shortcut.png)

7. Готово. Нажимаем Cmd+Shift+5 - делаем скриншот, который загружается в AWS S3.


### Добавляем действие в Dropzone 3

1. Ставим ![Dropzone 3](https://aptonic.com/dropzone3/)
2. Устанавливаем действие двойным кликом по "screenshot.dzbundle".
3. Готово. Теперь можно перетаскивать любые картинки картинки в Dropzone.


### Запускаем фронтенд для отображения скриншотов

1. Клонируем репозиторий:

		git clone git@github.com:dreadatour/s5.git
        cd s5

2. Создаём virtualenv:

        mkvirtualenv s5

3. Ставим зависимости:

        pip install -r requirements.txt

4. Запускаем:

        python s5.py

5. Открываем в браузере: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
6. ...
7. Profit!
