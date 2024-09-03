# Sistema de Adoção de Animais

Este repostório contém o codigo fonte do **Sistema de Adoção de Animais**, um projeto desenvolvido com Django como parte do Trabalho de Conclusão de Curso (TCC) em Análise e Desenvolvimento de Sistemas. O objetivo deste sistema é facilitar a adoção de animais de estimação, conectando abrigos e adotantes em uma plataforma intuitova e eficiente.

# Funcionalidades Principais:

- **Cadastro de Animais:** Permite que abrigos registrem animais disponíveis para adoção, incluindo informações como nome, espécie, raça, idade, porte e fotos.

- **Gerenciamento de Adotantes:** Sistema para cadastro e gerenciamento dos adotantes, com informações de contato e histórico de adoções.

- **Processo de Adoção:** Funcionalidade para registrar adoções, vinculando animais e adotantes, gerando um histórico das adoções reaizadas.

- **Interface administrativa:** Utilização do Django Admin para facilitar a gestão de dados como animais, adotantes e abrigos.

- **Autenticação e Autorização:** Módulo de autenticação para garantir que apenas usuários autorizados possam acessar determinadas funcionalidades.

- **Uploads de Imagens:** Suporte para upload de imagens dos animais, com armazenamento e exibição nas páginas de detalhes.

# Tecnologias Utilizadas:

- **Django:** Framework web utilizado para o desenvolvimento back-end.

- **SQLite:** Banco de dados utilizado para armazenamento das informações (configurável para outros bancos de dados com PostgreSQL).

- **JavaScript:** Funcionalidades dinâmicas e interativas na interface do usuário.

# Como Executar o Projeto:

1. Clone o repositório:
git clone https://github.com/seu-usuario/sistema-adocao-animais.git

2. Navegue até o diretório do projeto:
cd sistema-adocao-animais

3. Crie a ative o ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

4. Instale as dependências:
pip install -r requirements.txt

5. Aplique as migrações para criar o banco de dados:
python manage.py migrate

6. Crie um superusuário para acessar o admin:
python manage.py createsuperuser

7. Inicie o servidor de desenvolvimento:
python manage.py runserver

8. Acesse a aplicação em http://localhost:8000/

# Licença:

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes

# Autor

* **Jadson Silva** - https://www.linkedin.com/in/jadson-jose-silva/ | https://github.com/Jadson-Jose/AdoteSE
