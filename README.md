# criando modelo de estrutura de projeto

## Instalação e Configuração

1. Clone o repositório do github:
    ```bash
    git clone https://github.com/calel95/estruturando_projeto_e_processos_do_zero.git
    ```

2. Configurar versão do `pyenv`:
    ```bash
    pyenv install 3.12.3
    pyenv local 3.12.3
    ```

3. Inicie o poetry no projeto, crie o ambiente virtual e inicie o ambiente virtual:
    ```bash
    poetry init
    poetry env use 3.12.3
    source .venv/Scripts/activate
    ```

4. Instalar as libs necessárias:
    ```bash
    poetry add pyproject.toml
    ```

