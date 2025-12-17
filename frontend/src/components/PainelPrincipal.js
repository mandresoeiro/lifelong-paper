import React from "react";
import PainelTarefas from "./PainelTarefas";

export default function PainelPrincipal() {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Meu Dashboard</h1>

      {/* Aqui você pode ter outros blocos (ex: metas, progresso, etc.) */}
      <PainelTarefas />
    </div>
  );
}
