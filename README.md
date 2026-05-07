"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Search, MapPin, X, Loader2 } from "lucide-react";

const cidadesPopulares = [
  { nome: "Rio de Janeiro", slug: "rio-de-janeiro-rj" },
  { nome: "Niterói", slug: "niteroi-rj" },
  { nome: "Nova Iguaçu", slug: "nova-iguacu-rj" },
  { nome: "Duque de Caxias", slug: "duque-de-caxias-rj" },
  { nome: "São Gonçalo", slug: "sao-goncalo-rj" },
  { nome: "Petrópolis", slug: "petropolis-rj" },
  { nome: "Volta Redonda", slug: "volta-redonda-rj" },
  { nome: "Campos dos Goytacazes", slug: "campos-dos-goytacazes-rj" },
  { nome: "Cabo Frio", slug: "cabo-frio-rj" },
  { nome: "Angra dos Reis", slug: "angra-dos-reis-rj" },
  { nome: "Teresópolis", slug: "teresopolis-rj" },
  { nome: "Macaé", slug: "macae-rj" },
];

export default function SearchInput() {
  const [valor, setValor] = useState("");
  const [sugestoes, setSugestoes] = useState<typeof cidadesPopulares>([]);
  const [focused, setFocused] = useState(false);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState("");
  const router = useRouter();

  const isCep = (v: string) => /^\d{5}-?\d{3}$/.test(v) || /^\d{8}$/.test(v);

  function handleChange(v: string) {
    setValor(v);
    setErro("");

    const soCep = v.replace(/\D/g, "");

    // Autocomplete de cidade
    if (!isCep(v) && v.length >= 2) {
      const filtradas = cidadesPopulares.filter((c) =>
        c.nome.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "")
          .includes(v.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, ""))
      );
      setSugestoes(filtradas.slice(0, 5));
    } else {
      setSugestoes([]);
    }

    // Busca automática quando CEP completo
    if (soCep.length === 8) {
      buscarCep(soCep);
    }
  }

  async function buscarCep(cep: string) {
    setLoading(true);
    setErro("");
    try {
      const res = await fetch(`/api/cep?cep=${cep}`);
      const data = await res.json();
      if (data.error) {
        setErro("CEP não encontrado. Tente o nome da cidade.");
        setLoading(false);
        return;
      }
      router.push(`/internet-em/${data.slug}`);
    } catch {
      setErro("Erro ao buscar CEP. Tente novamente.");
    }
    setLoading(false);
  }

  function irParaCidade(slug: string) {
    setValor("");
    setSugestoes([]);
    router.push(`/internet-em/${slug}`);
  }

  function handleSearch() {
    if (loading) return;
    const soCep = valor.replace(/\D/g, "");
    if (soCep.length === 8) {
      buscarCep(soCep);
    } else if (sugestoes.length > 0) {
      irParaCidade(sugestoes[0].slug);
    } else if (valor.length >= 2) {
      const slug = valor
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/\s+/g, "-")
        .replace(/[^a-z0-9-]/g, "");
      router.push(`/internet-em/${slug}`);
    }
  }

  function limpar() {
    setValor("");
    setSugestoes([]);
    setErro("");
  }

  return (
    <div className="mt-8 w-full px-6 relative" style={{ maxWidth: 520, margin: "2rem auto 0" }}>

      {/* CAIXA */}
      <div className={`flex items-center bg-white rounded-full shadow-2xl overflow-hidden transition-all duration-200 ${
        focused ? "ring-2 ring-blue-400/50" : ""
      }`}>
        <Search className="text-gray-400 w-5 h-5 ml-4 flex-shrink-0" />
        <input
          value={valor}
          onChange={(e) => handleChange(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSearch()}
          onFocus={() => setFocused(true)}
          onBlur={() => setTimeout(() => setFocused(false), 150)}
          placeholder="Digite sua cidade ou CEP..."
          className="flex-1 py-4 px-3 text-gray-800 outline-none bg-transparent text-sm placeholder-gray-400 min-w-0"
        />
        {valor.length > 0 && !loading && (
          <button onClick={limpar} className="text-gray-300 hover:text-gray-500 mr-1 flex-shrink-0">
            <X className="w-4 h-4" />
          </button>
        )}
        <button
          onClick={handleSearch}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-500 transition text-white flex items-center gap-1.5 text-sm font-semibold flex-shrink-0 h-full py-3 px-4 rounded-full m-1 disabled:opacity-70"
        >
          {loading
            ? <Loader2 className="w-4 h-4 animate-spin" />
            : <MapPin className="w-4 h-4 flex-shrink-0" />
          }
          <span className="hidden sm:inline">{loading ? "Buscando..." : "Buscar"}</span>
        </button>
      </div>

      {/* ERRO */}
      {erro && (
        <p className="text-red-400 text-xs mt-2 text-center">{erro}</p>
      )}

      {/* SUGESTÕES */}
      {sugestoes.length > 0 && focused && (
        <div className="absolute top-full left-6 right-6 mt-2 bg-white rounded-2xl shadow-2xl overflow-hidden z-50 border border-gray-100">
          {sugestoes.map((c, i) => (
            <button
              key={c.slug}
              onMouseDown={() => irParaCidade(c.slug)}
              className={`w-full text-left px-5 py-3 text-gray-700 hover:bg-blue-50 transition text-sm flex items-center gap-3 ${
                i !== sugestoes.length - 1 ? "border-b border-gray-50" : ""
              }`}
            >
              <MapPin className="w-4 h-4 text-blue-400 flex-shrink-0" />
              <span>{c.nome}</span>
              <span className="text-gray-300 text-xs ml-auto">RJ</span>
            </button>
          ))}
        </div>
      )}

      <p className="text-white/30 text-xs mt-3 text-center">
        Digite o nome da cidade ou o CEP para buscar
      </p>
    </div>
  );
}
