# Python 3.11 베이스 이미지 사용 (Alpine 버전)
FROM python:3.12-alpine

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 시스템 의존성 설치
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev mariadb-dev curl

# Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"


# Python 의존성 파일 복사
COPY ./app_tennis/pyproject.toml poetry.lock* /tmp/

# 작업 디렉토리 설정
WORKDIR /tmp

# Poetry를 사용한 Python 의존성 설치
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Django 프로젝트 파일 복사
COPY ./app_tennis /app/

# 작업 디렉토리 변경
WORKDIR /app

# 포트 공개 (Django 개발 서버)
EXPOSE 8000

# Django 개발 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
