# Sistemas Distribuidos - 2024-2 - CIT2021

Este es el repositorio del curso de Sistemas Distribuidos, en el cual encontraran los códigos y ejemplos que iremos mostrando en ayudantía. Estos ejemplos podran usarlo como una guía para sus tareas. Además, pueden utilizar este README.md como guía para ordenar sus entregas.

### Stack

<p align='left'>
    <a href='https://docs.docker.com/' target='_blank'>
        <img src='https://img.shields.io/badge/docker-0F3486?style=for-the-badge&logo=docker&link=https%3A%2F%2Fdocs.docker.com%2F' height='30'>
    </a>
    <a href='https://www.postgresql.org/docs/' target='_blank'>
        <img src='https://img.shields.io/badge/Postgresql-6395BF?style=for-the-badge&logo=postgresql&logoColor=%23ffffff&link=https%3A%2F%2Fwww.postgresql.org%2Fdocs%2F' height='30'>
    </a>
</p>

### Video tutorial

<a href = 'https://youtu.be/XfqOB4hvxlY?si=68QiGEbrPYHiSGHf&t=8'
target='_blank'>
<img src='https://img.shields.io/badge/Video-0F0F0F?style=for-the-badge&logo=youtube&logoColor=%23FF0000'>
</a>

### How to run docker_demo

1. Clone this repository

```bash
git clone https://github.com/cesarmunozr/SD-2024-2.git
```

2. Run the docker compose

```bash
docker compose up
```

-d to run in detached mode

```bash
docker compose up -d
```

3. Access the container

```bash
docker exec -it pgdb /bin/bash
```

4. Access the database

```bash
psql -U postgres
```

5. To bring down the container

```bash
docker compose down
```

-v to remove the volumes

```bash
docker compose down -v
```
