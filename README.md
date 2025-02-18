Case Técnico: Recursos Cognitivos

===================================

## Descrição do Projeto

Este projeto consiste em uma aplicação web desenvolvida como parte de um case técnico para a empresa Recursos Cognitivos. A aplicação permite o gerenciamento de informações relacionadas a uma instituição de ensino, possibilitando o cadastro e a consulta de dados de alunos, cursos e matrículas.

## Status do Projeto

🚧 Projeto em desenvolvimento 🚧

## Funcionalidades

- Cadastro de Alunos: Permite adicionar novos alunos com informações pessoais.
- Cadastro de Cursos: Possibilita a criação de novos cursos com detalhes específicos.
- Gerenciamento de Matrículas: Facilita a associação de alunos a cursos.
- Consulta de Informações: Interfaces para visualizar listas de alunos, cursos e matrículas.

## Tecnologias Utilizadas

- Linguagem: Python
- Framework Web: Flask
- Banco de Dados: MySQL
- Front-end: HTML5, CSS3, JavaScript

## Requisitos para Execução

Antes de iniciar, certifique-se de ter instalado:
- Python 3.x ([Download](https://www.python.org/))
- MySQL Server ([Download](https://www.mysql.com/))
- Git ([Download](https://git-scm.com/))

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/matheusbnas/case_tecnico_RecursosCognitivos.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd case_tecnico_RecursosCognitivos
   ```

3. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

6. Configure o banco de dados MySQL:
   - Crie um banco de dados chamado `escola_manager`.
   - Atualize o arquivo `config.py` com suas credenciais do MySQL.
   - Execute as migrações do banco de dados:
     ```bash
     flask db upgrade
     ```

7. Inicie a aplicação:
   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Estrutura do Projeto

- `escola_manager/`: Diretório principal contendo os módulos da aplicação.
- `run.py`: Script para iniciar a aplicação.
- `requirements.txt`: Lista de dependências do projeto.
- `config.py`: Arquivo de configuração da aplicação.
- `setup.py`: Script para instalação do pacote.

## Contribuição

Se desejar contribuir com este projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça as alterações e commit:
   ```bash
   git commit -m 'Adicionando nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request explicando suas mudanças.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

