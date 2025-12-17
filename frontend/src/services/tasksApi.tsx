// frontend/src/services/tasksApi.js

export async function listarTarefas() {
  const res = await fetch("/api/tarefas/");
  return res.json();
}

export async function criarTarefa(titulo, descricao) {
  const res = await fetch("/api/tarefas/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titulo, descricao }),
  });
  return res.json();
}

export async function obterTarefa(id) {
  const res = await fetch(`/api/tarefas/${id}/`);
  return res.json();
}

export async function atualizarTarefa(id, data) {
  const res = await fetch(`/api/tarefas/${id}/`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function deletarTarefa(id) {
  const res = await fetch(`/api/tarefas/${id}/`, {
    method: "DELETE",
  });
  return res.ok;
}
