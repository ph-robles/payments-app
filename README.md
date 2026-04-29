"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { motion } from "framer-motion";
import { Zap, CheckCircle, XCircle, ArrowRight, Globe, Signal, Shield, Wifi } from "lucide-react";

// ANIMAÇÃO DE FIBRA
function FiberAnimation() {
  return (
    <div className="relative w-64 h-64 mx-auto">

      {/* LINHAS DE FIBRA */}
      {[...Array(6)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute left-0 right-0"
          style={{ top: `${15 + i * 12}%` }}
        >
          <motion.div
            className="h-0.5 rounded-full"
            style={{
              background: `linear-gradient(to right, transparent, ${
                ["#3b82f6", "#06b6d4", "#8b5cf6", "#3b82f6", "#06b6d4", "#8b5cf6"][i]
              }, transparent)`,
            }}
            animate={{ scaleX: [0, 1, 0], x: ["-100%", "0%", "100%"] }}
            transition={{ duration: 2 + i * 0.3, repeat: Infinity, delay: i * 0.4, ease: "easeInOut" }}
          />
        </motion.div>
      ))}

      {/* CAIXA DE ODF */}
      <motion.div
        className="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-20 bg-gray-800/80 border border-gray-600/40 rounded-lg flex flex-col items-center justify-center gap-1"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        {[...Array(5)].map((_, i) => (
          <motion.div
            key={i}
            className="w-6 h-1 rounded-full bg-blue-500/60"
            animate={{ opacity: [0.3, 1, 0.3] }}
            transition={{ duration: 1.5, repeat: Infinity, delay: i * 0.2 }}
          />
        ))}
      </motion.div>

      {/* ROTEADOR */}
      <motion.div
        className="absolute right-4 top-1/2 -translate-y-1/2 w-14 h-10 bg-gray-800/80 border border-gray-600/40 rounded-lg flex items-center justify-center"
        animate={{ boxShadow: ["0 0 0px #3b82f6", "0 0 15px #3b82f620", "0 0 0px #3b82f6"] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        <Wifi className="text-blue-400 w-6 h-6" />
      </motion.div>

      {/* PULSOS DE LUZ */}
      {[0, 1, 2].map((i) => (
        <motion.div
          key={i}
          className="absolute top-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-blue-400"
          animate={{ x: [20, 200], opacity: [0, 1, 0] }}
          transition={{ duration: 1.5, repeat: Infinity, delay: i * 0.5, ease: "linear" }}
        />
      ))}

      {/* VELOCIDADE */}
      <motion.div
        className="absolute top-2 right-2 bg-blue-500/20 border border-blue-500/30 rounded-lg px-2 py-1"
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        <span className="text-blue-400 text-xs font-mono font-bold">600Mbps</span>
      </motion.div>

      {/* LATÊNCIA */}
      <motion.div
        className="absolute top-2 left-2 bg-green-500/20 border border-green-500/30 rounded-lg px-2 py-1"
        animate={{ opacity: [0.5, 1, 0.5] }}
        transition={{ duration: 2, repeat: Infinity, delay: 1 }}
      >
        <span className="text-green-400 text-xs font-mono font-bold">5ms</span>
      </motion.div>

    </div>
  );
}

export default function FibraOpticaPage() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

          {/* PARTÍCULAS */}
          {[...Array(20)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-blue-400/20 rounded-full"
              style={{ top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%` }}
              animate={{ opacity: [0.1, 0.8, 0.1], scale: [1, 1.5, 1] }}
              transition={{ duration: 3 + Math.random() * 3, repeat: Infinity, delay: Math.random() * 2 }}
            />
          ))}

          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center relative z-10">
            <motion.div initial={{ opacity: 0, x: -40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.8 }}>
              <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
                <Zap className="w-3 h-3" />
                Guia técnico independente · 2026
              </div>
              <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                Fibra Óptica:<br />
                <span className="text-blue-400">a melhor internet</span><br />
                disponível
              </h1>
              <p className="text-white/50 text-lg mb-8 leading-relaxed">
                Entenda como funciona a fibra óptica, por que é superior ao cabo coaxial
                e como escolher o melhor plano na sua cidade.
              </p>
              <div className="flex flex-wrap gap-3">
                <a href="#provedores" className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm flex items-center gap-2">
                  Ver provedores <ArrowRight className="w-4 h-4" />
                </a>
                <Link href="/comparar" className="bg-white/5 hover:bg-white/10 transition border border-white/10 text-white px-6 py-3 rounded-xl text-sm">
                  Comparar planos
                </Link>
              </div>
            </motion.div>

            <motion.div initial={{ opacity: 0, scale: 0.8 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1, delay: 0.3 }}>
              <FiberAnimation />
            </motion.div>
          </div>
        </section>

        {/* STATS */}
        <section className="px-6 py-10 border-b border-white/10">
          <div className="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { icon: <Signal className="w-5 h-5 text-blue-400" />, valor: "1Gbps", label: "Velocidade máxima" },
              { icon: <Zap className="w-5 h-5 text-blue-400" />, valor: "5ms", label: "Latência média" },
              { icon: <Globe className="w-5 h-5 text-blue-400" />, valor: "99%", label: "Estabilidade" },
              { icon: <Shield className="w-5 h-5 text-blue-400" />, valor: "R$90", label: "A partir de" },
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

        {/* COMO FUNCIONA */}
        <section className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">Como funciona</p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {[
                { num: "01", titulo: "Luz no cabo", texto: "A fibra óptica transmite dados através de pulsos de luz em fios de vidro ultrafinos — muito mais rápido que sinais elétricos." },
                { num: "02", titulo: "Zero interferência", texto: "Diferente do cabo coaxial, a fibra não sofre interferência eletromagnética. Isso garante estabilidade mesmo em dias de chuva." },
                { num: "03", titulo: "Velocidade simétrica", texto: "Upload e download na mesma velocidade. Perfeito para videochamadas, live streaming e home office." },
              ].map((item, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.15 }}
                  className="bg-white/5 border border-white/10 rounded-2xl p-6"
                >
                  <div className="text-4xl font-bold text-blue-400/20 mb-3">{item.num}</div>
                  <h3 className="font-bold mb-2">{item.titulo}</h3>
                  <p className="text-white/50 text-sm leading-relaxed">{item.texto}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* PROVEDORES */}
        <section id="provedores" className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Principais provedores de fibra no RJ
            </p>
            <div className="flex flex-col gap-4">
              {[
                { nome: "Claro Fibra", velocidade: "até 600 Mbps", preco: "a partir de R$99,90", cobertura: "Maior cobertura do RJ", pros: ["Rede ampla", "Instalação grátis"], contras: ["Fidelidade 12 meses"] },
                { nome: "Vivo Fibra", velocidade: "até 500 Mbps", preco: "a partir de R$109,99", cobertura: "Capital e região", pros: ["Melhor estabilidade", "App completo"], contras: ["Cobertura menor"] },
                { nome: "TIM Live", velocidade: "até 400 Mbps", preco: "a partir de R$89,99", cobertura: "Capitais e cidades grandes", pros: ["Preço mais baixo"], contras: ["Cobertura limitada"] },
              ].map((p, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.1 }}
                  className="bg-white/5 border border-white/10 hover:border-blue-500/30 rounded-2xl p-6 transition-all"
                >
                  <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2 flex-wrap">
                        <h3 className="font-bold text-lg">{p.nome}</h3>
                        <span className="text-xs bg-blue-500/10 border border-blue-500/20 text-blue-400 px-2 py-0.5 rounded-full">
                          {p.cobertura}
                        </span>
                      </div>
                      <div className="flex gap-4 text-sm text-white/50 mb-3">
                        <span className="flex items-center gap-1"><Zap className="w-3 h-3 text-blue-400" />{p.velocidade}</span>
                        <span>{p.preco}</span>
                      </div>
                      <div className="flex flex-wrap gap-3">
                        {p.pros.map((pro, j) => (
                          <span key={j} className="flex items-center gap-1 text-xs text-green-400">
                            <CheckCircle className="w-3 h-3" />{pro}
                          </span>
                        ))}
                        {p.contras.map((contra, j) => (
                          <span key={j} className="flex items-center gap-1 text-xs text-red-400">
                            <XCircle className="w-3 h-3" />{contra}
                          </span>
                        ))}
                      </div>
                    </div>
                    <button className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm flex items-center gap-2 flex-shrink-0 w-fit">
                      Contratar <ArrowRight className="w-4 h-4" />
                    </button>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* FIBRA VS CABO */}
        <section className="px-6 py-12 border-b border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">Fibra vs cabo coaxial</p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-blue-500/5 border border-blue-500/20 rounded-2xl p-6">
                <h3 className="font-bold text-lg mb-4 text-blue-400">⚡ Fibra Óptica</h3>
                <ul className="flex flex-col gap-3">
                  {["Velocidade até 1 Gbps", "Latência de 5ms", "Estável em chuva", "Upload = Download", "Não degrada com distância"].map((item, i) => (
                    <li key={i} className="flex items-center gap-2 text-white/70 text-sm">
                      <CheckCircle className="w-4 h-4 text-green-400 flex-shrink-0" />{item}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
                <h3 className="font-bold text-lg mb-4 text-white/50">📺 Cabo Coaxial</h3>
                <ul className="flex flex-col gap-3">
                  {["Velocidade até 300 Mbps", "Latência de 15–30ms", "Instável em tempestades", "Upload menor que download", "Degrada com distância"].map((item, i) => (
                    <li key={i} className="flex items-center gap-2 text-white/40 text-sm">
                      <XCircle className="w-4 h-4 text-red-400/60 flex-shrink-0" />{item}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="px-6 py-8">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-purple-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
            <Zap className="text-blue-400 w-10 h-10 mx-auto mb-4" />
            <h3 className="font-bold text-xl mb-2">Tem fibra óptica na sua cidade?</h3>
            <p className="text-white/50 text-sm mb-6">Busque agora e veja todos os provedores disponíveis no seu endereço.</p>
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
