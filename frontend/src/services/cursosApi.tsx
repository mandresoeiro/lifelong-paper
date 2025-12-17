// frontend/src/services/cursosApi.tsx

export async function listarCursos() {
  const res = await fetch('/cursos/');
  // Note: currently cursos endpoints return HTML pages; if a JSON API exists, change to /api/cursos/
  try {
    return res.json();
  } catch (e) {
    // fallback: return status and text
    const text = await res.text();
    return { status: res.status, text };
  }
}

export async function criarCurso(data) {
  const form = new FormData();
  Object.keys(data).forEach((k) => form.append(k, data[k]));
  const res = await fetch('/cursos/novo/', {
    method: 'POST',
    body: form,
  });
  return { ok: res.ok, status: res.status };
}

export default { listarCursos, criarCurso };
