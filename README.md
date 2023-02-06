# Projeto Scielo
Esse repositório contém as aplicaçoes do Projeto Scielo
## Como rodar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.10
* Instale o docker e o docker-compose 
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Crie o usuário 
* Rode os containers
* Rode a aplicação

```
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
docker-compose up -d
python manage.py runserver
```


## Endpoints

| Método     | Url                  | Descrição                                     |
|------------|----------------------|-----------------------------------------------|
| POST       | api/v1/articles      | Recebe xml no formato JATS Version 1.3.       |
| POST       | api/v1/token         | Recebe usuário e senha e retorna tokens JWT.  |
| POST       | api/v1/token/refresh | Recebe resfresh token e retorna access Token. |
