# 🍷 Festival Cave | Sistema de leilão - Backend

## Sobre o projeto

Este repositório contém o código-fonte do **back-end** para o sistema de leilão em tempo real do **FESTIVAL CAVE**, um evento de vinhos realizado em Natal com o patrocínio do Governo do Rio Grande do Norte.

O sistema foi projetado para leiloar uma obra de arte única, pintada ao vivo por um artista durante o evento. A plataforma permite que os participantes deem lances de forma interativa e dinâmica, acompanhando o progresso do leilão em tempo real.

## Tecnologias Utilizadas

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black">

## Endpoints da Aplicação

### Autenticação
| Rota | Descrição | Autenticação |
| --- | --- | --- |
| <kbd>GET /auth/validate_auth</kbd> | Valida se o usuário está autenticado com sucesso. | HTTP Basic Auth |

### Lances (Bids)
| Rota | Descrição |
| --- | --- |
| <kbd>POST /bids</kbd> | Cria um novo lance. |
| <kbd>GET /bids</kbd> | Retorna a lista de todos os lances. |
| <kbd>GET /bids/highest</kbd> | Retorna o maior lance registrado. |
| <kbd>DELETE /bids/{bid_value}</kbd> | Deleta um lance com base no seu valor. |
| <kbd>DELETE /bids</kbd> | Deleta **todos** os lances. |

### Relatórios (Reports)
| Rota | Descrição |
| --- | --- |
| <kbd>POST /reports</kbd> | Gera e retorna um relatório de lances. O formato (`excel`, `csv`, `json`) deve ser especificado no corpo da requisição. |

## Executando o projeto

### Pré-requisitos

- Python 3.12+
- Pip 24.0+

### Passos:

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/Erm2k8/CAVE-2025-BACKEND.git](https://github.com/Erm2k8/CAVE-2025-BACKEND.git)
    ```

2.  Acesse o diretório do projeto:
    ```bash
    cd CAVE-2025-BACKEND
    ```

3.  Crie e ative um ambiente virtual:
    ```bash
    # Crie o ambiente
    python -m venv .venv

    # Ative o ambiente
    # Windows
    .venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate
    ```

4.  Instale as dependências:
    ```bash
    pip install -r src/requirements.txt
    ```

5.  Configure as variáveis de ambiente:
    - Renomeie o arquivo `.env.example` para `.env`.
    - Preencha as variáveis de ambiente no arquivo `.env` com suas credenciais do Firebase e de administrador.

6.  Execute a aplicação:
    ```bash
    cd src
    uvicorn main:app --reload
    ```

A aplicação estará disponível em `http://127.0.0.1:8000`. A documentação interativa da API pode ser acessada em `http://127.0.0.1:8000/docs`.

## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Erm2k8">
        <img src="https://avatars.githubusercontent.com/u/144192401?v=4" width="115"><br>
        <sub>Ermesson Andrade</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/leonardonadson">
        <img src="https://avatars.githubusercontent.com/u/72714982?v=4" width="115"><br>
        <sub>Leonardo Nadson</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lucas-albuq">
        <img src="https://avatars.githubusercontent.com/u/108223448?v=4" width="115"><br>
        <sub>Lucas Albuquerque</sub>
      </a>
    </td>
  </tr>
</table>
