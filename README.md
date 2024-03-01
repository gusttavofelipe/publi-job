<!-- # PubliJob Site -->

# Informações do projeto
O site foi desenvolvido ultilizando `Django`, para armazenar os arquivos, `Postgres` por meio do `Docker`,  framework CSS `Bootstrap4` . Ultilizando as bibliotecas: `crispy_forms` e `widget_tweaks` para incrementar o front

## Execução
Este projeto ultiliza a versão **3.12** do Python, use [pyenv](https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875) para instalar a respectiva versão

#### Após a instalação execute:
```shell
pyenv virtualenv 3.12 publijob
```
Para criar o ambiente virtual

```shell
pyenv activate publijob
```
Para atvar o ambiente virtual

## Instalar dependencias
#### Certifique-se de que seu ambiente virtual esteja ativado e execute:
```shell
make dependencies
```

## Banco de dados
Crie um arquivo .env e insira as credenciais de local.env

#### Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/ubuntu/) e [docker-compose](https://docs.docker.com/compose/install/linux/) instalados e execute:
```shell
docker-compose up -d
```
## Site
#### Após as etapas anteriores serem bem sucedidas execute:
```shell
make migrate
```
Para executar as migrações no banco de dados

```shell
make runserver
```
Para subir o site. <br>
Para ver, acesse: http://127.0.0.1:8000/
