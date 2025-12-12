# Lifelong Paper

Sistema de gerenciamento de artigos acadêmicos desenvolvido com Django.

## Estrutura do Projeto

- **accounts**: Gerenciamento de contas de usuário
- **profiles**: Perfis de usuário
- **papers**: Gerenciamento de artigos
- **visual**: Interface visual
- **core**: Configurações principais do Django

## Configuração

1. Crie um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:
```bash
pip install django
```

3. Execute as migrações:
```bash
python manage.py migrate
```

4. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Estrutura de Settings

O projeto usa configurações modulares:
- `core/settings/base.py`: Configurações comuns
- `core/settings/dev.py`: Configurações de desenvolvimento
- `core/settings/prod.py`: Configurações de produção
