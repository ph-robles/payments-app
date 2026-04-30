<button
  onClick={run}
  disabled={running}
  className="h-12 rounded-2xl text-base font-bold bg-blue-600 hover:bg-blue-500 px-6 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed transition"
>
  <Gauge className="w-4 h-4" />
  {running ? "Executando..." : "Iniciar Teste"}
</button>
