# Url Shortener

## Instalar as dependências do projeto

### instalar o pyenv
https://github.com/pyenv/pyenv#installation

### dependências para compilar e instalar o python
`sudo apt-get update; sudo apt-get install make gcc build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`

### instalar a versão 3.10.0 do python
`pyenv install 3.10.0`

### configurar versão 3.10.0 na sessão do terminal aberto
`pyenv shell 3.10.0`

### instalar depêdencias do projeto
`pip install --upgrade pip setuptools wheel poetry`

### criar o ambiente virtual através poetry
`poetry env use 3.10.0`

### ativar o ambiente virtual através poetry
`source $(poetry env info --path)/bin/activate`

### rodar o comando pra instalar as depedencias da aplicação
`make install-deps`

## Arquivo .env

Faça um cópia do arquivo .env.local removendo o sufixo .local

## Configurar Application Default Credentials

### instalar o gcloud cli
https://cloud.google.com/sdk/docs/install-sdk

### configurar o cli para o projeto de nonprod
`gcloud config set project snmxgfihomh7g4qogpyop2qtu0dief`

### fazer o login no gcloud via cli para criar um Application Default Credentials na sua máquina
`gcloud auth application-default login`

## Gerar um token para fazer requisições nos endpoints de reenvio de mensagens da dead letter
`gcloud auth print-identity-token`
