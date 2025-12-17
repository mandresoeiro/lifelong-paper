export async function getPapers() {
  const response = await fetch("/api/papers/");
  if (!response.ok) throw new Error("Erro ao buscar papers");
  return response.json();
}
