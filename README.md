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
