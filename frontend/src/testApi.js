export async function pingBackend() {
  const response = await fetch("/api/");
  return response.text();
}
