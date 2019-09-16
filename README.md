# Text Handler Web APP

Esse APP tem o objetivo de receber um texto, analisá-lo e encontrar a frequência de cada palavra neste texto. Pra isso o projeto foi feito em duas frentes, sendo elas uma classe e o REST.

A classe manipula os textos e retorna a resposta. Essa classe virou a app/api_v1/text_handler/text_handler.py::TextHandler e pode ser utilizada em várias API's.

O aplicativo API Rest foi criado utilizando o framework Flask. Sua função é: receber as requisições, chamar a biblioteca passando os dados e desenvolver a resposta.

![Exemplo](doc/imgs/example.gif)

## Estrutura
A estrutura do projeto é ilustrado na imagem a seguir.

![Estrutura](doc/imgs/folder_structure.png)

## Instação

O projeto precisa que o pipenv e docker estejam instalados.

### Como instalar as bibliotecas python requeridas

Caminhe até a pasta backend
```bash
cd backend/
```

Digite o comando a seguir:

```bash
pipenv install
```

### Como instalar o Postgres

O projeto utiliza o banco de dados postgres. A ferramenta *docker* foi utilizada para fornecer o banco.

Caminhe até a pasta backend
```bash
cd backend/
```

Digite o comando a seguir:

```bash
docker-compose up
```

### Inicializando o banco de dados

As tabelas do banco de dados precisam ser criada. Siga os passos:

1. Caminhe até o direito do backend
```bash
cd backend/
```

2. Inicie o pipenv
```bash
pipenv shell
```

3. Digite o seguinte comando
```bash
FLASK_APP=run.py FLASK_ENV=development flask db upgrade
```

## Projeto

O projeto foi escrito na linguaguem python 3.7. Durante o desenvolvimento foi utilizado a técnica de *test driven development (tdd)*.

### TextHandler (backend/app/text_handler/text_handler.py)

O *TextHandler* é uma classe que recebe como paramêtro uma lista de string, que representa os textos, e processa a lista através de um dos 4 métodos.

Para realizar o processamento do texto, a biblioteca *nltk* foi utilizada.

Um dos requisitos do projeto é a remoção das stop-words. Para resolver isso,utilizei uma lista de palavras encontradas no link: [gist stop-words](https://gist.github.com/alopes/5358189).

#### Métodos e suas funções:

1. sw_vocabulary

Cria uma lista de palavras únicas presentes nos textos seguindo algumas condições como: a não presença de stop-words; palavras que começam com número e todas as letras devem ser minúsculas.

Ex: Texto => Bernardo Gomes Abreu

["Bernardo", "Gomes", "Abreu"]

2. sw_frequency_distribution

Com a lista de palavras criada no sw_vocabulary, esse método checa a frequência que cada palavra da lista aparece em cada texto.

3. ng_vocabulary

Cria uma lista de elementos formados por duas palavras em sequência presentes nos textos, seguindo algumas condições como: a não presença de stop-words; palavras que começam com número e todas as letras devem ser minúsculas.

Ex: Texto => Bernardo Gomes Abreu

[["Bernardo", "Gomes"], ["Gomes", "Abreu"]]

4. ng_frequency_distribution

Com a lista de palavras criadas no ng_vocabulary, esse método checa a frequência que cada palavra da lista aparece em cada texto


### REST API

O APP  *Rest API* foi feito utilizando *Flask Framework* e Flask-RESTPlus como base do projeto e foram utilizadas as bibliotecas: Marshmallow, para realizar a deserialização e serialização dos dados trafegados; Flask-Migrate, para realizar o versionamento do banco de dados; e a Flask-SQLAlchemy, para controlar os acessos ao banco de dados.

As regras abaixo foram seguidas no desenvolvimento:

1. Todo dado que entra ou sai do sistema deve passar por um schema criado pela biblioteca Marshmallow.
2. Toda entrada ou saída do sistema deverá ser feito em json.

### Testes

O projeto conta com cerca de 80 testes que foram criados durante o desenvolvimento.

![Estrutura](doc/imgs/tests_count.png)

Utilizando a biblioteca coverage conseguimos mensurar que os testes passaram pelo menos uma vez por cada linha.

![COVERAGE_REPORT](doc/imgs/coverage_report.png)



#### Como executar os testes
Para executar os testes digite o comando abaixo:

```bash
pytest
```

### Documentação API
A documentação da API está no endpoint /api/v1.

![SWAGGER](doc/imgs/swagger.png)

### Link Heroku
[text-bernardo](https://text-bernardo.herokuapp.com/)


## Licença
[MIT](https://choosealicense.com/licenses/mit/)

