## Execução do projeto via docker: 🐳
Ao executar dessa maneira não precisa se preocupar em executar os outros docker, todos serão iniciados juntos.
 - utilizar a env nomeada como env-docker, antes de executar o docker execute o comando.
   ```bash
   cp .env-docker .env
   ```

- Para executar o projeto utilizando Docker Compose:
   ```bash
   docker-compose up
   ```
## Documentação: 📘
- Após o projeto estar em execução, a documentação dos endpoints pode ser acessada em:
 ```bash
 http://127.0.0.1:8000/api/v1/swagger/
 ```

## Testes: 🧪
 Para executar os testes, basta executar o comando abaixo:
 ```bash
 ./manage.py test task
 ```

# Execução do projeto sem Docker: 🛠️

## Instalação e Execução do Projeto: ⚙️

### 1. Clonar o Repositório

```bash
git clone https://github.com/LucasTaveira/todolist.git
```
### 2. Crie ambiente virtual:
  ```bash
  python -m .venv .venv
  source .venv/bin/activate
  ```

### 3. Instalação das dependencias:
  ```bash
    pip install -r requirements.txt
  ```
## Execução do Projeto: 🚀
 Após a instalação das dependências, é necessário iniciar o PostgreSQL e o Redis.

 - Inicie o PostgreSQL e o Redis a partir das respectivas pastas docker/postgres e docker/redis:
      ```bash
      cd docker/redis
      docker-compose up
  
      cd docker/postgress
      docker-compose up
      ```
  - Execute a API:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## Índice 📑
- [Documentação](#documentação)
- [Testes](#testes)
