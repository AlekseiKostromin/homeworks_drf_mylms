# Docker 27.2
# ������ ������-��������

���� ������ ������ ��� ������-�������� � �������������� Django � ������ ����������.

## ������ ������� � ������� Docker Compose

��� ������� ������� � ������� Docker Compose ��������� ��������� ����:

1. ���������� Docker � Docker Compose, ���� ��� ��� �� ����������� �� ����� ����������.

2. ����������� ����������� � ��������:
    ```
    git clone https://github.com/AlekseiKostromin/homeworks_drf_mylms
    ```
3. ��������� � ���������� � ��������:
    ```
    cd my_lms_project
    ```
4. �������� ���� `.env` � ����� ������� � ������� � ��� ���������� ���������:
    ```
    ������ ���������� ��������� ����� � ����� .env_sample
    ```
5. �������� � ��������� ���������� Docker:
    ```
    docker-compose up --build
    ```
8. �������� ������� � ��������� �� ������ `http://localhost:8000` ��� ������� �  �������.

9. ��� ������������� ��������� �������� ���� ������ � �������� ����������� �����:
    ```
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py collectstatic
    ```
10. ������! ������ ������-�������� ������ ������� � ������� Docker Compose.

# drf 26.2

# drf 26.1

# drf 25.2

# drf 25.1

# drf 24.2

# drf 24.1



