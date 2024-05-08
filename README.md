```markdown
# Docker를 이용한 Django 개발 환경 명령어 모음

Docker 개발 환경에서 유용하게 사용할 수 있는 명령어들

## 서비스 시작하기

- 모든 서비스 시작하기
  ```bash
  docker-compose up
  ```
  `-d` 플래그를 추가하면 백그라운드에서 서비스를 시작할 수 있음 (dev 모드)

## 컨테이너 내에서 명령어 실행하기

- 마이그레이션 생성 및 적용하기
  ```bash
  docker-compose run <서비스 이름> sh -c "python manage.py makemigrations"
  docker-compose run <서비스 이름> sh -c "python manage.py migrate"
  ```
- Django 슈퍼유저 생성하기
  ```bash
  docker-compose run <서비스 이름> sh -c "python manage.py createsuperuser"
  ```
- 테스트 실행하기
  ```bash
  docker-compose run <서비스 이름> sh -c "python manage.py test"
  ```

## 서비스 재시작 및 중지하기

- 개별 서비스 재시작하기
  ```bash
  docker-compose restart <서비스 이름>
  ```
- 모든 서비스 중지하기
  ```bash
  docker-compose down
  ```
  `--volumes` 또는 `-v` 플래그를 사용하면 볼륨도 함께 제거됨

## 로그 보기

- 서비스 로그 보기
  ```bash
  docker-compose logs <서비스 이름>
  ```
  `-f` 플래그를 사용하면 실시간 로그를 볼 수 있음

## 컨테이너 접속하기

- 셸 접속하기
  ```bash
  docker-compose exec <서비스 이름> sh
  ```
  또는
  ```bash
  docker-compose exec <서비스 이름> bash
  ```
  실행 중인 컨테이너 내부에 있는 셸에 접속가능! 이를 통해 컨테이너 내에서 직접 명령어를 실행할 수 있음

이 명령어들을 적절히 활용하여 개발 환경을 관리하고 필요한 Django 관리 명령어를 실행해 개발을 계속 진행할 수 있다..!
```