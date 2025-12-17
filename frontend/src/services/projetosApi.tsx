// frontend/src/services/projetosApi.tsx

export async function listarProjetos() {
  const res = await fetch('/api/projetos/');
  return res.json();
}

export async function criarProjeto(data) {
  // data: { nome, descricao, tecnologias, status, link, progresso }
  const res = await fetch('/api/projetos/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function obterProjeto(id) {
  const res = await fetch(`/api/projetos/${id}/`);
  return res.json();
}

export async function atualizarProjeto(id, data) {
  const res = await fetch(`/api/projetos/${id}/`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function deletarProjeto(id) {
  const res = await fetch(`/api/projetos/${id}/`, { method: 'DELETE' });
  return res.ok;
}

export default {
  listarProjetos,
  criarProjeto,
  obterProjeto,
  atualizarProjeto,
  deletarProjeto,
};
