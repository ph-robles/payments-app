"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { motion } from "framer-motion";
import { Satellite, CheckCircle, XCircle, ArrowRight, Globe, Zap, Shield, Signal } from "lucide-react";

// ANIMAÇÃO ORBITAL
function OrbitalAnimation() {
  return (
    <div className="relative w-64 h-64 mx-auto">

      {/* TERRA */}
      <div className="absolute bottom-4 left-1/2 -translate-x-1/2 w-32 h-32 rounded-full bg-gradient-to-br from-blue-600/60 to-blue-900/80 border border-blue-500/30 overflow-hidden">
        <div className="absolute top-4 left-4 w-10 h-6 rounded-full bg-green-700/50" />
        <div className="absolute top-8 left-12 w-14 h-7 rounded-full bg-green-700/40" />
        <div className="absolute top-3 right-4 w-6 h-4 rounded-full bg-green-700/50" />
        {/* ATMOSFERA */}
        <div className="absolute inset-0 rounded-full bg-blue-400/10 border border-blue-400/20" />
      </div>

      {/* ÓRBITA */}
      <motion.div
        className="absolute top-8 left-1/2 -translate-x-1/2 w-48 h-48 rounded-full border border-blue-400/20"
        style={{ borderStyle: "dashed" }}
      />

      {/* SATÉLITE 1 */}
      <motion.div
        className="absolute"
        style={{ top: "10%", left: "50%" }}
        animate={{ rotate: 360 }}
        transition={{ duration: 6, repeat: Infinity, ease: "linear" }}
        transformOrigin="0 100px"
      >
        <div className="relative -translate-x-1/2">
          <div className="w-6 h-4 bg-blue-500/80 rounded-sm border border-blue-400/50 relative">
            <div className="absolute -left-4 top-1/2 -translate-y-1/2 w-3 h-1.5 bg-blue-300/60" />
            <div className="absolute -right-4 top-1/2 -translate-y-1/2 w-3 h-1.5 bg-blue-300/60" />
          </div>
        </div>
      </motion.div>

      {/* SATÉLITE 2 */}
      <motion.div
        className="absolute"
        style={{ top: "10%", left: "50%" }}
        animate={{ rotate: -360 }}
        transition={{ duration: 9, repeat: Infinity, ease: "linear" }}
        transformOrigin="0 80px"
      >
        <div className="relative -translate-x-1/2">
          <div className="w-5 h-3 bg-cyan-500/70 rounded-sm border border-cyan-400/40 relative">
            <div className="absolute -left-3 top-1/2 -translate-y-1/2 w-2.5 h-1 bg-cyan-300/50" />
            <div className="absolute -right-3 top-1/2 -translate-y-1/2 w-2.5 h-1 bg-cyan-300/50" />
          </div>
        </div>
      </motion.div>

      {/* ONDAS DE SINAL */}
      {[1, 2, 3].map((i) => (
        <motion.div
          key={i}
          className="absolute bottom-16 left-1/2 -translate-x-1/2 rounded-full border border-blue-400/15"
          animate={{ width: [10, 80], height: [10, 80], opacity: [0.8, 0] }}
          transition={{ duration: 2, repeat: Infinity, delay: i * 0.6 }}
        />
      ))}

      {/* VELOCIDADE */}
      <motion.div
        className="absolute top-2 right-2 bg-blue-500/20 border border-blue-500/30 rounded-lg px-2 py-1"
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        <span className="text-blue-400 text-xs font-mono font-bold">200Mbps</span>
      </motion.div>

      {/* LATÊNCIA */}
      <motion.div
        className="absolute top-2 left-2 bg-green-500/20 border border-green-500/30 rounded-lg px-2 py-1"
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 2, repeat: Infinity, delay: 1 }}
      >
        <span className="text-green-400 text-xs font-mono font-bold">25ms</span>
      </motion.div>

    </div>
  );
}

export const metadata = {
  title: "Starlink no Brasil 2026",
  description: "Tudo sobre o Starlink no Brasil. Preço, velocidade, instalação e comparativo com fibra óptica.",
};

export default function StarlinkPage() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-cyan-900/10 pointer-events-none" />

          {/* ESTRELAS */}
          {[...Array(25)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-0.5 h-0.5 bg-white rounded-full"
              style={{ top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%` }}
              animate={{ opacity: [0.1, 0.9, 0.1] }}
              transition={{ duration: 2 + Math.random() * 3, repeat: Infinity, delay: Math.random() * 2 }}
            />
          ))}

          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center relative z-10">
            <motion.div initial={{ opacity: 0, x: -40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.8 }}>
              <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
                <Satellite className="w-3 h-3" />
                Guia técnico independente · 2026
              </div>
              <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                Starlink no Brasil:<br />
                <span className="text-blue-400">vale a pena</span><br />
                em 2026?
              </h1>
              <p className="text-white/50 text-lg mb-8 leading-relaxed">
                Análise técnica completa do serviço de internet via satélite da SpaceX.
                Preço real, velocidade real e para quem realmente vale.
              </p>
              <div className="flex flex-wrap gap-3">
                <a href="#planos" className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm flex items-center gap-2">
                  Ver planos <ArrowRight className="w-4 h-4" />
                </a>
                <Link href="/internet-rural" className="bg-white/5 hover:bg-white/10 transition border border-white/10 text-white px-6 py-3 rounded-xl text-sm">
                  Internet Rural
                </Link>
              </div>
            </motion.div>

            <motion.div initial={{ opacity: 0, scale: 0.8 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1, delay: 0.3 }}>
              <OrbitalAnimation />
            </motion.div>
          </div>
        </section>

        {/* STATS */}
        <section className="px-6 py-10 border-b border-white/10">
          <div className="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { icon: <Signal className="w-5 h-5 text-blue-400" />, valor: "200Mbps", label: "Velocidade máxima" },
              { icon: <Zap className="w-5 h-5 text-blue-400" />, valor: "25ms", label: "Latência média" },
              { icon: <Globe className="w-5 h-5 text-blue-400" />, valor: "100%", label: "Cobertura no BR" },
              { icon: <Shield className="w-5 h-5 text-blue-400" />, valor: "Sem", label: "Fidelidade" },
            ].map((s, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                className="bg-white/5 border border-white/10 rounded-2xl p-4 text-center"
              >
                <div className="flex justify-center mb-2">{s.icon}</div>
                <div className="text-xl font-bold text-blue-400">{s.valor}</div>
                <div className="text-white/40 text-xs mt-1">{s.label}</div>
              </motion.div>
            ))}
          </div>
        </section>

        {/* PLANOS */}
        <section id="planos" className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">Planos disponíveis no Brasil</p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {[
                { nome: "Residencial", preco: "R$ 236/mês", kit: "R$ 1.680", velocidade: "25–200 Mbps", destaque: false },
                { nome: "Residencial+", preco: "R$ 350/mês", kit: "R$ 1.680", velocidade: "40–220 Mbps", destaque: true },
                { nome: "Portátil", preco: "R$ 236/mês", kit: "R$ 999", velocidade: "5–50 Mbps", destaque: false },
              ].map((p, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className={`rounded-2xl border p-6 text-center ${
                    p.destaque
                      ? "bg-blue-500/10 border-blue-500/30"
                      : "bg-white/5 border-white/10"
                  }`}
                >
                  {p.destaque && (
                    <span className="bg-blue-500/20 text-blue-400 text-xs px-2 py-0.5 rounded-full border border-blue-500/30 mb-3 inline-block">
                      Mais popular
                    </span>
                  )}
                  <h3 className="font-bold text-lg mb-4">{p.nome}</h3>
                  <div className="text-3xl font-bold text-blue-400 mb-1">{p.preco}</div>
                  <div className="text-white/40 text-sm mb-4">Kit: {p.kit}</div>
                  <div className="text-white/60 text-sm mb-6">{p.velocidade}</div>
                  <button className="w-full bg-blue-600 hover:bg-blue-500 transition text-white font-bold py-3 rounded-xl text-sm">
                    Contratar
                  </button>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* PROS E CONTRAS */}
        <section className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-6">
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              className="bg-green-500/5 border border-green-500/20 rounded-2xl p-6"
            >
              <h3 className="font-bold text-lg mb-4 text-green-400">✅ Pontos positivos</h3>
              <ul className="flex flex-col gap-3">
                {[
                  "Funciona em qualquer lugar do Brasil",
                  "Baixa latência comparado a satélites convencionais",
                  "Sem fidelidade — cancele quando quiser",
                  "Velocidade real de 100–200 Mbps",
                  "Ideal para home office em área rural",
                  "Instalação simples — você mesmo pode instalar",
                ].map((item, i) => (
                  <li key={i} className="flex items-center gap-2 text-white/70 text-sm">
                    <CheckCircle className="w-4 h-4 text-green-400 flex-shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              className="bg-red-500/5 border border-red-500/20 rounded-2xl p-6"
            >
              <h3 className="font-bold text-lg mb-4 text-red-400">❌ Pontos negativos</h3>
              <ul className="flex flex-col gap-3">
                {[
                  "Mensalidade cara — R$236/mês mínimo",
                  "Kit inicial de R$999 a R$1.680",
                  "Sinal cai em chuvas fortes (2–5 min)",
                  "Upload mais lento que fibra óptica",
                  "Não indicado para gaming competitivo",
                  "Precisa de área aberta — sem obstáculos",
                ].map((item, i) => (
                  <li key={i} className="flex items-center gap-2 text-white/70 text-sm">
                    <XCircle className="w-4 h-4 text-red-400 flex-shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
            </motion.div>
          </div>
        </section>

        {/* PARA QUEM VALE */}
        <section className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">Para quem vale a pena</p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {[
                { emoji: "🏡", titulo: "Zona rural e interior", texto: "Sem dúvida a melhor opção. Se não tem fibra no seu endereço, Starlink é a escolha certa." },
                { emoji: "🏔️", titulo: "Chácaras e sítios", texto: "Perfeito para propriedades rurais que precisam de internet estável para trabalho ou lazer." },
                { emoji: "💼", titulo: "Home office crítico", texto: "Para quem trabalha remotamente em área rural e não pode depender de 4G instável." },
                { emoji: "🚗", titulo: "Uso portátil", texto: "O plano portátil permite usar em trânsito — ótimo para quem viaja entre propriedades." },
              ].map((item, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className="bg-white/5 border border-white/10 rounded-2xl p-5 flex gap-4"
                >
                  <span className="text-3xl flex-shrink-0">{item.emoji}</span>
                  <div>
                    <h3 className="font-bold mb-1">{item.titulo}</h3>
                    <p className="text-white/50 text-sm">{item.texto}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="px-6 py-8">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-cyan-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
            <Satellite className="text-blue-400 w-10 h-10 mx-auto mb-4" />
            <h3 className="font-bold text-xl mb-2">Compare internet na sua cidade</h3>
            <p className="text-white/50 text-sm mb-6">Veja se o Starlink é realmente a melhor opção para o seu endereço.</p>
            <Link href="/" className="inline-block bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm">
              Buscar provedores
            </Link>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
