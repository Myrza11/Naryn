# Используем Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для PyQt5 и необходимые пакеты для PyQtWebEngine
RUN apt-get update && apt-get install -y qtbase5-dev qtwebengine5-dev sip-dev && rm -rf /var/lib/apt/lists/*

# Копируем очищенные списки зависимостей
COPY clean_requirements.txt .
COPY clean_requirements2.txt .
COPY clean_requirements3.txt .
COPY clean_requirements4.txt .
COPY clean_requirements5.txt .
COPY clean_requirements6.txt .
COPY clean_requirements8.txt .

# Устанавливаем зависимости из всех файлов по очереди
RUN pip install --no-cache-dir -r clean_requirements6.txt

RUN pip install --no-cache-dir -r clean_requirements.txt
RUN pip install --no-cache-dir -r clean_requirements2.txt
RUN pip install --no-cache-dir -r clean_requirements3.txt
RUN pip install --no-cache-dir -r clean_requirements4.txt
RUN pip install --no-cache-dir -r clean_requirements5.txt
RUN pip install --no-cache-dir -r clean_requirements8.txt


# Копируем остальные файлы проекта
COPY . .

# Открываем порт
EXPOSE 8000

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
