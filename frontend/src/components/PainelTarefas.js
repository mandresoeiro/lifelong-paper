import { useEffect, useState } from "react";
import { listarTarefas, criarTarefa } from "../services/tasksApi";

export default function PainelTarefas() {
  const [tarefas, setTarefas] = useState([]);
  const [titulo, setTitulo] = useState("");

  // Carregar tarefas quando o componente for montado
  useEffect(() => {
    listarTarefas().then(setTarefas);
  }, []);

  const adicionarTarefa = async () => {
    if (!titulo.trim()) return;
    const nova = await criarTarefa(titulo, "");
    setTarefas([nova, ...tarefas]);
    setTitulo("");
  };

  return (
    <div className="bg-white p-4 rounded-xl shadow mt-6">
      <h2 className="text-lg font-semibold mb-4">📋 Minhas Tarefas</h2>

      <div className="flex gap-2 mb-3">
        <input
          type="text"
          placeholder="Nova tarefa..."
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          className="border border-gray-300 rounded px-3 py-2 w-full"
        />
        <button
          onClick={adicionarTarefa}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          Adicionar
        </button>
      </div>

      {tarefas.length === 0 ? (
        <p className="text-gray-500 text-sm">Nenhuma tarefa cadastrada ainda.</p>
      ) : (
        <ul className="space-y-2">
          {tarefas.map((t) => (
            <li
              key={t.id}
              className="border rounded p-2 flex justify-between items-center hover:bg-gray-50 transition"
            >
              <span>{t.titulo}</span>
              {t.concluido ? (
                <span className="text-green-600 text-sm font-semibold">✔ Concluída</span>
              ) : (
                <span className="text-gray-400 text-sm">Em aberto</span>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
