## 🚗 Sistema de Gestão de Veículos (Car Management System)

Este é um sistema de gerenciamento de veículos robusto e escalável construído com **Python** e o framework **Django**. A aplicação oferece uma API RESTful completa para gerenciar carros, fabricantes, usuários, grupos e permissões, utilizando autenticação moderna e filtragem avançada.

---

## 🛠️ Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias principais:

* **Python 3.12.3** Linguagem de programação principal.
* **Django:** Framework web de alto nível para desenvolvimento rápido e design pragmático.
* **Django REST Framework (DRF):** Toolkit poderoso para a construção de Web APIs.
* **djangorestframework-simplejwt:** Implementação de autenticação baseada em **JSON Web Tokens (JWT)** para segurança e statelessness.
* **django-rql:** Implementa a linguagem de consulta **Resource Query Language (RQL)** para filtragem, classificação e paginação avançadas via URL.

---

## ✨ Funcionalidades Principais

* **Gerenciamento de CRUD:** Suporte completo para criar, ler, atualizar e deletar (**C**reate, **R**ead, **U**pdate, **D**elete) **Carros** e **Fabricantes**.
* **Autenticação Segura:** Autenticação de usuário via **JWT** (access e refresh tokens).
* **Gerenciamento de Acesso:** Administração de **Usuários**, **Grupos** e **Permissões** (integrado com o sistema de permissões nativo do Django).
* **API RESTful:** Endpoints bem definidos para interagir com os recursos do sistema.
* **Filtragem Avançada (RQL):** Capacidade de realizar consultas complexas, filtragem (ex: `?query=eq(ano,2022)&query=ge(preco,30000)`), ordenação e seleção de campos diretamente pela URL, através do `django-rql`.

---

## 🚀 Primeiros Passos

### Pré-requisitos

* Python 3.x
* pip (gerenciador de pacotes Python)

### Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/GuiOliver27/cars-api.git)
    cd cars-api
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # ou
    # venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

    > **Nota:** Certifique-se de que `requirements.txt` contém: `django`, `djangorestframework`, `djangorestframework-simplejwt`, `django-rql`, etc.

4.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acessar o Admin/DRF Browsable API):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

O sistema estará disponível em `http://127.0.0.1:8000/`.

