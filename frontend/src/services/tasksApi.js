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
