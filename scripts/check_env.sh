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
