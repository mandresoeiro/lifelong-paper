# 🟢 Script padrão — check_env.sh

Este documento descreve o **script padrão de verificação de ambiente Django**, usado para garantir que o projeto está rodando no **Python correto**, com **Django instalado** e **ambiente saudável**.

---

## 🎯 Objetivo do script

O script `check_env.sh` verifica automaticamente:

- ✅ Qual Python está sendo usado (`which python`)
- ✅ Versão do Python (`python -V`)
- ✅ Se o Django está instalado no ambiente ativo
- ✅ Se o projeto passa no `manage.py check`
- ⚠️ Alerta se você **não estiver dentro da venv**

---

## 📁 Estrutura recomendada

```text
lifelong-paper/
├── scripts/
│   └── check_env.sh
├── manage.py
├── static/
├── templates/
└── ...
```

---

## 📄 Código do script

Crie o arquivo:

```bash
nano scripts/check_env.sh
```

Cole **exatamente** o conteúdo abaixo:

```bash
#!/usr/bin/env bash

echo "────────────────────────────────────"
echo "🔍 Django Environment Check"
echo "────────────────────────────────────"

echo
echo "📌 Python path:"
which python || { echo "❌ Python não encontrado"; exit 1; }

echo
echo "📌 Python version:"
python -V || { echo "❌ Python não funciona"; exit 1; }

echo
echo "📌 Django version:"
python -m django --version || {
  echo "❌ Django NÃO está instalado neste ambiente"
  echo "👉 Ative a venv ou instale o Django"
  exit 1
}

echo
echo "📌 Django system check:"
python manage.py check || {
  echo "❌ Django encontrou problemas"
  exit 1
}

echo
echo "✅ Ambiente Django OK"
echo "────────────────────────────────────"
```

---

## 🔐 Permissão de execução

```bash
chmod +x scripts/check_env.sh
```

---

## ▶️ Como executar

### Com venv ativada:

```bash
./scripts/check_env.sh
```

### Com Poetry (recomendado):

```bash
poetry run ./scripts/check_env.sh
```

---

## 🧪 Exemplo de saída (ambiente OK)

```text
🔍 Django Environment Check

📌 Python path:
/home/marcio/dev/myprojects/lifelong-paper/.venv/bin/python

📌 Python version:
Python 3.12.1

📌 Django version:
5.0.1

📌 Django system check:
System check identified no issues (0 silenced).

✅ Ambiente Django OK
```

---

## ❌ Exemplo de saída (ambiente quebrado)

```text
📌 Django version:
❌ Django NÃO está instalado neste ambiente
👉 Ative a venv ou instale o Django
```

---

## 🧠 Boas práticas recomendadas

- Sempre rodar Django com **Poetry ou venv ativada**
- Usar este script **antes de rodar o servidor**
- Evitar misturar `pip install` com Poetry
- Nunca confiar em `python` sem verificar `which python`

---

## 🔹 Alias no terminal (zsh)

Adicione no `~/.zshrc`:

```bash
alias djcheck="./scripts/check_env.sh"
```

Depois recarregue:

```bash
source ~/.zshrc
```

Agora basta rodar:

```bash
djcheck
```

---

## 🔹 Próximas evoluções (opcional)

- `make check`
- `make run`
- Script de setup automático
- Integração com CI (GitHub Actions)

---

📌 **Este arquivo pode ser usado no MkDocs, Obsidian ou como documentação do projeto.**
