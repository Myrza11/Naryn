# Используем нужную версию Python (3.12)
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Обновляем pip до последней версии
RUN python -m pip install --upgrade pip

# Устанавливаем необходимые зависимости для PyQt5 и PyQtWebEngine
RUN apt-get update && apt-get install -y qtbase5-dev qtwebengine5-dev sip-dev && rm -rf /var/lib/apt/lists/*

# Копируем файлы с зависимостями
COPY clean_requirements.txt .
COPY clean_requirements2.txt .
COPY clean_requirements3.txt .
COPY clean_requirements4.txt .
COPY clean_requirements5.txt .
COPY clean_requirements6.txt .
COPY clean_requirements8.txt .

# Устанавливаем зависимости из файлов с увеличением таймаута
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements6.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements2.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements3.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements4.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements5.txt
RUN pip install --no-cache-dir --timeout=600 -r clean_requirements8.txt

# Используем зеркало PyPI для ускоренной загрузки пакетов
RUN pip install --no-cache-dir -r clean_requirements6.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements2.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements3.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements4.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements5.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r clean_requirements8.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Копируем остальные файлы проекта
COPY . .

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запуск приложения (если используется Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
