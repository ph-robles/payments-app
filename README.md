"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { motion } from "framer-motion";
import { BookOpen, Clock, ChevronRight, ArrowRight, Zap } from "lucide-react";

const artigos = [
  {
    slug: "melhor-internet-petropolis-rj-2026",
    titulo: "Melhor internet em Petrópolis RJ 2026",
    descricao: "Compare os melhores provedores disponíveis em Petrópolis. Fibra, satélite e rádio analisados por um técnico de campo.",
    tempo: "5 min",
    tag: "Cidade",
    tagColor: "blue",
    emoji: "🏙️",
  },
  {
    slug: "starlink-vale-a-pena-rio-de-janeiro",
    titulo: "Starlink vale a pena no Rio de Janeiro?",
    descricao: "Análise técnica completa do Starlink no RJ. Velocidade real, latência, cobertura e comparativo com fibra óptica.",
    tempo: "7 min",
    tag: "Satélite",
    tagColor: "purple",
    emoji: "🛰️",
  },
  {
    slug: "internet-rural-interior-rj",
    titulo: "Internet rural no interior do RJ: qual escolher em 2026",
    descricao: "Guia completo para escolher internet no interior fluminense. Starlink, 4G rural e satélite comparados por técnico de campo.",
    tempo: "6 min",
    tag: "Rural",
    tagColor: "green",
    emoji: "🌿",
  },
  {
    slug: "claro-vs-vivo-fibra-rj",
    titulo: "Claro vs Vivo Fibra: qual é melhor no RJ em 2026",
    descricao: "Comparativo técnico entre Claro Fibra e Vivo Fibra no Rio de Janeiro. Velocidade, estabilidade, preço e suporte.",
    tempo: "5 min",
    tag: "Comparativo",
    tagColor: "orange",
    emoji: "⚡",
  },
  {
    slug: "como-testar-velocidade-real-internet",
    titulo: "Como testar a velocidade real da sua internet",
    descricao: "Guia técnico para medir a velocidade real. Saiba se seu provedor está entregando o que prometeu e como reclamar.",
    tempo: "4 min",
    tag: "Dica técnica",
    tagColor: "cyan",
    emoji: "📡",
  },
];

const tagColors: Record<string, string> = {
  blue: "bg-blue-500/10 text-blue-400 border-blue-500/20",
  purple: "bg-purple-500/10 text-purple-400 border-purple-500/20",
  green: "bg-green-500/10 text-green-400 border-green-500/20",
  orange: "bg-orange-500/10 text-orange-400 border-orange-500/20",
  cyan: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20",
};

// ANIMAÇÃO DE LIVRO/ARTIGOS
function GuiasAnimation() {
  return (
    <div className="relative w-64 h-48 mx-auto">
      {[...Array(4)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute left-1/2 bg-white/5 border border-white/10 rounded-xl"
          style={{ width: 180 - i * 15, height: 50 }}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0, top: i * 28 }}
          transition={{ delay: i * 0.15, duration: 0.6 }}
        >
          <div className="flex items-center gap-3 px-4 h-full">
            <motion.div
              className="w-6 h-6 rounded-lg bg-blue-500/20 border border-blue-500/30 flex-shrink-0"
              animate={{ opacity: [0.5, 1, 0.5] }}
              transition={{ duration: 2, repeat: Infinity, delay: i * 0.3 }}
            />
            <div className="flex flex-col gap-1 flex-1">
              <div className="h-2 bg-white/10 rounded-full w-full" />
              <div className="h-1.5 bg-white/5 rounded-full w-3/4" />
            </div>
          </div>
        </motion.div>
      ))}

      {/* PULSO */}
      <motion.div
        className="absolute -bottom-4 left-1/2 -translate-x-1/2 w-32 h-1 bg-blue-400/20 rounded-full"
        animate={{ scaleX: [0.5, 1, 0.5], opacity: [0.3, 0.8, 0.3] }}
        transition={{ duration: 2, repeat: Infinity }}
      />
    </div>
  );
}

export default function GuiasPage() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

          {/* PARTÍCULAS */}
          {[...Array(15)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-blue-400/20 rounded-full"
              style={{ top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%` }}
              animate={{ opacity: [0.1, 0.7, 0.1] }}
              transition={{ duration: 3 + Math.random() * 3, repeat: Infinity, delay: Math.random() * 2 }}
            />
          ))}

          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center relative z-10">
            <motion.div initial={{ opacity: 0, x: -40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.8 }}>
              <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
                <BookOpen className="w-3 h-3" />
                Conteúdo técnico independente
              </div>
              <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                Guias<br />
                <span className="text-blue-400">Técnicos</span>
              </h1>
              <p className="text-white/50 text-lg mb-8 leading-relaxed">
                Análises e comparativos feitos por técnico de telecom
                com experiência real em campo. Sem papo de vendedor.
              </p>
              <div className="flex flex-wrap gap-3">
                <a href="#artigos" className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm flex items-center gap-2">
                  Ver guias <ArrowRight className="w-4 h-4" />
                </a>
                <Link href="/comparar" className="bg-white/5 hover:bg-white/10 transition border border-white/10 text-white px-6 py-3 rounded-xl text-sm">
                  Comparar planos
                </Link>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 1, delay: 0.3 }}
            >
              <GuiasAnimation />
            </motion.div>
          </div>
        </section>

        {/* STATS */}
        <section className="px-6 py-10 border-b border-white/10">
          <div className="max-w-6xl mx-auto grid grid-cols-3 gap-4">
            {[
              { valor: "5", label: "Guias publicados" },
              { valor: "100%", label: "Gratuito" },
              { valor: "Campo", label: "Experiência real" },
            ].map((s, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                className="bg-white/5 border border-white/10 rounded-2xl p-4 text-center"
              >
                <div className="text-xl font-bold text-blue-400">{s.valor}</div>
                <div className="text-white/40 text-xs mt-1">{s.label}</div>
              </motion.div>
            ))}
          </div>
        </section>

        {/* LISTA DE ARTIGOS */}
        <section id="artigos" className="px-6 py-12">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Todos os guias
            </p>
            <div className="flex flex-col gap-4">
              {artigos.map((artigo, i) => (
                <motion.div
                  key={artigo.slug}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.08 }}
                >
                  <Link
                    href={`/guias/${artigo.slug}`}
                    className="group bg-white/5 hover:bg-blue-500/5 border border-white/10 hover:border-blue-500/30 rounded-2xl p-6 transition-all flex flex-col md:flex-row md:items-center gap-4"
                  >
                    {/* EMOJI */}
                    <div className="text-4xl flex-shrink-0 hidden md:block">{artigo.emoji}</div>

                    {/* CONTEÚDO */}
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2 flex-wrap">
                        <span className={`text-xs px-2 py-0.5 rounded-full border ${tagColors[artigo.tagColor]}`}>
                          {artigo.tag}
                        </span>
                        <span className="flex items-center gap-1 text-white/30 text-xs">
                          <Clock className="w-3 h-3" />
                          {artigo.tempo} de leitura
                        </span>
                      </div>
                      <h2 className="font-bold text-lg text-white mb-1 group-hover:text-blue-400 transition">
                        {artigo.titulo}
                      </h2>
                      <p className="text-white/50 text-sm leading-relaxed">
                        {artigo.descricao}
                      </p>
                    </div>

                    {/* SETA */}
                    <ChevronRight className="w-5 h-5 text-white/20 group-hover:text-blue-400 transition flex-shrink-0 hidden md:block" />
                  </Link>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="px-6 pb-8">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-purple-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
            <Zap className="text-blue-400 w-10 h-10 mx-auto mb-4" />
            <h3 className="font-bold text-xl mb-2">Quer comparar provedores na sua cidade?</h3>
            <p className="text-white/50 text-sm mb-6">
              Use nossa ferramenta gratuita para ver todas as opções disponíveis no seu endereço.
            </p>
            <Link href="/" className="inline-block bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm">
              Buscar internet na minha cidade
            </Link>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
