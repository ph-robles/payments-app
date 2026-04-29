"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { motion } from "framer-motion";
import { MapPin, Zap, DollarSign, Star, ArrowRight, ChevronRight, Wifi, Satellite, Phone } from "lucide-react";
import { supabase } from "@/lib/supabase";
import { use, useEffect, useState } from "react";

// ANIMAÇÃO DO MAPA
function CityAnimation({ cidade }: { cidade: string }) {
  return (
    <div className="relative w-64 h-48 mx-auto">

      {/* MAPA ESTILIZADO */}
      <div className="absolute inset-0 bg-white/5 border border-white/10 rounded-2xl overflow-hidden">
        {/* GRID */}
        {[...Array(6)].map((_, i) => (
          <div key={i} className="absolute w-full h-px bg-white/5" style={{ top: `${i * 20}%` }} />
        ))}
        {[...Array(6)].map((_, i) => (
          <div key={i} className="absolute h-full w-px bg-white/5" style={{ left: `${i * 20}%` }} />
        ))}

        {/* PONTOS DE COBERTURA */}
        {[
          { x: "30%", y: "40%", size: 40, delay: 0 },
          { x: "60%", y: "30%", size: 30, delay: 0.3 },
          { x: "50%", y: "65%", size: 35, delay: 0.6 },
          { x: "20%", y: "60%", size: 25, delay: 0.9 },
        ].map((p, i) => (
          <motion.div
            key={i}
            className="absolute rounded-full bg-blue-500/10 border border-blue-400/20"
            style={{ left: p.x, top: p.y, width: p.size, height: p.size, transform: "translate(-50%, -50%)" }}
            animate={{ scale: [1, 1.3, 1], opacity: [0.4, 0.8, 0.4] }}
            transition={{ duration: 2.5, repeat: Infinity, delay: p.delay }}
          />
        ))}

        {/* PIN PRINCIPAL */}
        <motion.div
          className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2"
          animate={{ y: [0, -6, 0] }}
          transition={{ duration: 2, repeat: Infinity }}
        >
          <div className="w-8 h-8 bg-blue-600 rounded-full border-2 border-blue-400 flex items-center justify-center shadow-lg shadow-blue-500/30">
            <MapPin className="w-4 h-4 text-white" />
          </div>
          <div className="w-2 h-2 bg-blue-600 rounded-full mx-auto -mt-1" />
        </motion.div>
      </div>

      {/* BADGE COBERTURA */}
      <motion.div
        className="absolute -top-3 -right-3 bg-green-500/20 border border-green-500/30 rounded-xl px-2 py-1"
        animate={{ opacity: [0.6, 1, 0.6] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        <span className="text-green-400 text-xs font-mono font-bold">✓ Online</span>
      </motion.div>
    </div>
  );
}

async function getProvedores(slugCidade: string) {
  const { data, error } = await supabase
    .from("provedor_cidades")
    .select(`
      provedor_id,
      cidade,
      estado,
      provedores (
        id, nome, tecnologia, velocidade_max,
        preco_min, latencia, franquia, contrato,
        instalacao, avaliacao, destaque
      )
    `)
    .eq("slug_cidade", slugCidade);

  if (error || !data) return [];
  return data.map((d: any) => d.provedores).filter(Boolean);
}

function formatarCidade(cidade: string) {
  return cidade
    .replace(/-rj|-sp|-mg|-rs|-ba|-pr|-sc|-go|-df|-es/g, "")
    .replace(/-/g, " ")
    .replace(/\b\w/g, (l) => l.toUpperCase());
}

export default function CidadePage({ params }: { params: Promise<{ cidade: string }> }) {
  const { cidade } = use(params);
  const cidadeFormatada = formatarCidade(cidade);

  const [provedores, setProvedores] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getProvedores(cidade).then((data) => {
      setProvedores(data);
      setLoading(false);
    });
  }, [cidade]);

  const velocidadeMax = provedores.length > 0 ? Math.max(...provedores.map((p) => p.velocidade_max)) : 0;
  const precoMin = provedores.length > 0 ? Math.min(...provedores.map((p) => p.preco_min)) : 0;

  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-cyan-900/10 pointer-events-none" />

          {/* PARTÍCULAS */}
          {[...Array(12)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-blue-400/20 rounded-full"
              style={{ top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%` }}
              animate={{ opacity: [0.1, 0.7, 0.1] }}
              transition={{ duration: 3 + Math.random() * 3, repeat: Infinity, delay: Math.random() * 2 }}
            />
          ))}

          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center relative z-10">

            {/* TEXTO */}
            <motion.div initial={{ opacity: 0, x: -40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.8 }}>

              {/* BREADCRUMB */}
              <div className="flex items-center gap-2 text-white/30 text-xs mb-6 flex-wrap">
                <Link href="/" className="hover:text-white transition">Início</Link>
                <ChevronRight className="w-3 h-3" />
                <span>Internet em</span>
                <ChevronRight className="w-3 h-3" />
                <span className="text-white/60">{cidadeFormatada}</span>
              </div>

              <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
                <MapPin className="w-3 h-3" />
                Comparador técnico independente
              </div>

              <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                Internet em<br />
                <span className="text-blue-400">{cidadeFormatada}</span>
              </h1>

              <p className="text-white/50 text-lg mb-8">
                {loading ? "Carregando provedores..." : provedores.length > 0
                  ? `${provedores.length} provedores disponíveis — compare e escolha o melhor.`
                  : "Cidade ainda não mapeada na nossa base."}
              </p>

              {/* STATS */}
              {!loading && provedores.length > 0 && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.3 }}
                  className="flex gap-4 flex-wrap"
                >
                  {[
                    { valor: provedores.length.toString(), label: "Provedores" },
                    { valor: `${velocidadeMax}Mb`, label: "Vel. máxima" },
                    { valor: `R$${precoMin.toFixed(0)}`, label: "A partir de" },
                  ].map((s, i) => (
                    <div key={i} className="bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-center min-w-20">
                      <div className="text-lg font-bold text-blue-400">{s.valor}</div>
                      <div className="text-white/40 text-xs mt-0.5">{s.label}</div>
                    </div>
                  ))}
                </motion.div>
              )}
            </motion.div>

            {/* ANIMAÇÃO */}
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 1, delay: 0.3 }}
            >
              <CityAnimation cidade={cidadeFormatada} />
            </motion.div>
          </div>
        </section>

        {/* PROVEDORES */}
        <section className="px-6 py-12">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Provedores disponíveis em {cidadeFormatada}
            </p>

            {loading ? (
              <div className="flex flex-col gap-4">
                {[1, 2, 3].map((i) => (
                  <div key={i} className="bg-white/5 border border-white/10 rounded-2xl p-6 animate-pulse">
                    <div className="h-5 bg-white/10 rounded w-1/3 mb-3" />
                    <div className="h-3 bg-white/5 rounded w-1/4" />
                  </div>
                ))}
              </div>
            ) : provedores.length === 0 ? (
              <div className="bg-white/5 border border-white/10 rounded-2xl p-12 text-center">
                <Wifi className="text-white/20 w-12 h-12 mx-auto mb-4" />
                <h3 className="font-bold text-lg mb-2">Cidade não mapeada ainda</h3>
                <p className="text-white/40 text-sm max-w-sm mx-auto mb-6">
                  Ainda não temos dados para essa cidade. Estamos expandindo nossa cobertura.
                </p>
                <Link href="/" className="inline-block bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm">
                  Buscar outra cidade
                </Link>
              </div>
            ) : (
              <div className="flex flex-col gap-4">
                {provedores.map((p: any, i: number) => (
                  <motion.div
                    key={p.id}
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.08 }}
                    className={`rounded-2xl border p-6 transition-all ${
                      i === 0
                        ? "bg-blue-500/5 border-blue-500/30"
                        : "bg-white/5 border-white/10 hover:border-blue-500/20"
                    }`}
                  >
                    <div className="flex flex-col md:flex-row md:items-center gap-4">

                      {/* RANKING */}
                      <div className="text-4xl font-bold text-white/5 w-10 flex-shrink-0 hidden md:block">
                        {String(i + 1).padStart(2, "0")}
                      </div>

                      {/* INFO */}
                      <div className="flex-1">
                        <div className="flex items-center gap-3 mb-2 flex-wrap">
                          <h3 className="font-bold text-lg">{p.nome}</h3>
                          {p.destaque && (
                            <span className="bg-blue-500/10 text-blue-400 text-xs px-2 py-0.5 rounded-full border border-blue-500/20">
                              {p.destaque}
                            </span>
                          )}
                          {i === 0 && (
                            <span className="bg-yellow-500/10 text-yellow-400 text-xs px-2 py-0.5 rounded-full border border-yellow-500/20">
                              ⭐ Melhor opção
                            </span>
                          )}
                        </div>

                        <div className="flex flex-wrap gap-4 text-sm text-white/50">
                          <span className="flex items-center gap-1">
                            {p.tecnologia === "Satélite"
                              ? <Satellite className="w-3 h-3 text-blue-400" />
                              : <Zap className="w-3 h-3 text-blue-400" />
                            }
                            {p.tecnologia}
                          </span>
                          <span className="flex items-center gap-1">
                            <Zap className="w-3 h-3 text-blue-400" />
                            {p.velocidade_max} Mbps
                          </span>
                          {p.avaliacao > 0 && (
                            <span className="flex items-center gap-1">
                              <Star className="w-3 h-3 text-yellow-400" />
                              {p.avaliacao}
                            </span>
                          )}
                        </div>
                      </div>

                      {/* PREÇO + CTA */}
                      <div className="flex items-center gap-4">
                        <div className="text-right">
                          <div className="font-bold text-xl flex items-center gap-1">
                            <DollarSign className="w-4 h-4 text-blue-400" />
                            R$ {p.preco_min.toFixed(2)}
                          </div>
                          <div className="text-white/30 text-xs">por mês</div>
                        </div>
                        <motion.button
                          whileTap={{ scale: 0.95 }}
                          className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-5 py-3 rounded-xl text-sm flex items-center gap-2"
                        >
                          <Phone className="w-4 h-4" />
                          Contratar
                        </motion.button>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </div>
        </section>

        {/* CTA */}
        <section className="px-6 pb-8">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-cyan-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
            <Wifi className="text-blue-400 w-10 h-10 mx-auto mb-4" />
            <h3 className="font-bold text-xl mb-2">Quer comparar outras cidades?</h3>
            <p className="text-white/50 text-sm mb-6">
              Busque qualquer cidade do Rio de Janeiro e veja todos os provedores disponíveis.
            </p>
            <Link href="/" className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm">
              Buscar outra cidade <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
