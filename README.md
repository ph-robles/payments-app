"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/footer";
import { useState } from "react";
import { motion } from "framer-motion";
import { Zap, Satellite, Star, CheckCircle, XCircle, ArrowRight, BarChart2 } from "lucide-react";


const planos = [
    {
        id: "claro",
        nome: "Claro Fibra",
        tipo: "Fibra Óptica",
        velocidade: 600,
        latencia: "5ms",
        preco: 99.90,
        avaliacao: 4.2,
        franquia: "Ilimitado",
        contrato: "12 meses",
        instalacao: "Grátis",
        pros: ["Maior cobertura urbana", "Velocidade estável", "Instalação grátis"],
        contras: ["Fidelidade obrigatória", "Suporte lento"],
    },
    {
        id: "vivo",
        nome: "Vivo Fibra",
        tipo: "Fibra Óptica",
        velocidade: 500,
        latencia: "5ms",
        preco: 109.99,
        avaliacao: 4.4,
        franquia: "Ilimitado",
        contrato: "12 meses",
        instalacao: "Grátis",
        pros: ["Melhor avaliação de usuários", "App completo", "Boa estabilidade"],
        contras: ["Preço mais alto", "Cobertura menor que Claro"],
    },
    {
        id: "tim",
        nome: "TIM Live",
        tipo: "Fibra Óptica",
        velocidade: 400,
        latencia: "8ms",
        preco: 89.99,
        avaliacao: 3.9,
        franquia: "Ilimitado",
        contrato: "12 meses",
        instalacao: "Grátis",
        pros: ["Preço mais baixo", "Sem taxa de adesão"],
        contras: ["Cobertura limitada", "Suporte fraco"],
    },
    {
        id: "starlink",
        nome: "Starlink",
        tipo: "Satélite",
        velocidade: 150,
        latencia: "25ms",
        preco: 236,
        avaliacao: 4.6,
        franquia: "Ilimitado",
        contrato: "Sem fidelidade",
        instalacao: "Kit R$ 999",
        pros: ["Funciona em qualquer lugar", "Sem fidelidade", "Melhor para rural"],
        contras: ["Mensalidade cara", "Kit inicial caro"],
    },
];

// ANIMAÇÃO DE BARRAS
function BarAnimation() {
    const bars = [
        { label: "Claro", valor: 600, max: 600, cor: "bg-red-400" },
        { label: "Vivo", valor: 500, max: 600, cor: "bg-purple-400" },
        { label: "TIM", valor: 400, max: 600, cor: "bg-blue-400" },
        { label: "Starlink", valor: 150, max: 600, cor: "bg-cyan-400" },
    ];

    return (
        <div className="w-full max-w-sm mx-auto space-y-3">
            {bars.map((b, i) => (
                <motion.div
                    key={i}
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: i * 0.15 }}
                    className="flex items-center gap-3"
                >
                    <span className="text-white/40 text-xs w-14 text-right flex-shrink-0">{b.label}</span>
                    <div className="flex-1 h-6 bg-white/5 rounded-full overflow-hidden border border-white/10">
                        <motion.div
                            className={`h-full ${b.cor} rounded-full flex items-center justify-end pr-2`}
                            initial={{ width: 0 }}
                            animate={{ width: `${(b.valor / b.max) * 100}%` }}
                            transition={{ duration: 1.2, delay: i * 0.15, ease: "easeOut" }}
                        >
                            <span className="text-black text-xs font-bold">{b.valor}M</span>
                        </motion.div>
                    </div>
                </motion.div>
            ))}
            <p className="text-white/20 text-xs text-center mt-4">Velocidade máxima (Mbps)</p>
        </div>
    );
}

export default function CompararPage() {
    const [selecionados, setSelecionados] = useState<string[]>(["claro", "starlink"]);

    const toggle = (id: string) => {
        if (selecionados.includes(id)) {
            if (selecionados.length > 2) setSelecionados(selecionados.filter((s) => s !== id));
        } else {
            if (selecionados.length < 3) setSelecionados([...selecionados, id]);
        }
    };

    const comparados = planos.filter((p) => selecionados.includes(p.id));

    return (
        <>
            <Navbar />
            <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

                {/* HERO */}
                <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">

                    {/* FUNDO GRADIENTE */}
                    <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

                    {/* PARTÍCULAS */}
                    {[...Array(15)].map((_, i) => (
                        <motion.div
                            key={i}
                            className="absolute w-1 h-1 bg-blue-400/30 rounded-full"
                            style={{
                                top: `${Math.random() * 100}%`,
                                left: `${Math.random() * 100}%`,
                            }}
                            animate={{ opacity: [0.1, 0.6, 0.1], scale: [1, 1.5, 1] }}
                            transition={{
                                duration: 3 + Math.random() * 3,
                                repeat: Infinity,
                                delay: Math.random() * 2,
                            }}
                        />
                    ))}

                    <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 items-center relative z-10">

                        {/* TEXTO */}
                        <motion.div
                            initial={{ opacity: 0, x: -40 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.8 }}
                        >
                            <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
                                <BarChart2 className="w-3 h-3" />
                                Comparador técnico independente · 2026
                            </div>

                            <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                                Compare planos<br />
                                <span className="text-blue-400">lado a lado</span>
                            </h1>

                            <p className="text-white/50 text-lg mb-8 leading-relaxed">
                                Selecione até 3 provedores e veja velocidade,
                                preço, latência e contrato lado a lado.
                                Dados técnicos reais, sem enrolação.
                            </p>

                            <div className="flex flex-wrap gap-3">
                                <a href="#comparativo" className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm flex items-center gap-2">
                                    Comparar agora <ArrowRight className="w-4 h-4" />
                                </a>
                            </div>
                        </motion.div>

                        {/* ANIMAÇÃO DE BARRAS */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.9 }}
                            animate={{ opacity: 1, scale: 1 }}
                            transition={{ duration: 1, delay: 0.3 }}
                            className="bg-white/5 border border-white/10 rounded-2xl p-8"
                        >
                            <p className="text-white/30 text-xs font-mono uppercase tracking-widest mb-6 text-center">
                                Velocidade máxima por provedor
                            </p>
                            <BarAnimation />
                        </motion.div>
                    </div>
                </section>

                {/* SELETOR */}
                <section id="comparativo" className="px-6 py-8 border-b border-white/10">
                    <div className="max-w-4xl mx-auto">
                        <p className="text-white/40 text-xs uppercase tracking-widest font-mono mb-4">
                            Selecione os planos ({selecionados.length}/3)
                        </p>
                        <div className="flex flex-wrap gap-3">
                            {planos.map((p) => (
                                <motion.button
                                    key={p.id}
                                    onClick={() => toggle(p.id)}
                                    whileTap={{ scale: 0.95 }}
                                    className={`px-4 py-2 rounded-full border text-sm font-medium transition-all ${selecionados.includes(p.id)
                                            ? "bg-blue-600 text-white border-blue-600"
                                            : "bg-white/5 text-white/60 border-white/10 hover:border-white/30"
                                        }`}
                                >
                                    {p.nome}
                                </motion.button>
                            ))}
                        </div>
                    </div>
                </section>

                {/* TABELA */}
                <section className="px-6 py-12">
                    <div className="max-w-4xl mx-auto overflow-x-auto">

                        {/* CABEÇALHO */}
                        <div className="grid gap-4 mb-4" style={{ gridTemplateColumns: `160px repeat(${comparados.length}, 1fr)` }}>
                            <div />
                            {comparados.map((p) => (
                                <motion.div
                                    key={p.id}
                                    initial={{ opacity: 0, y: -10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    className="bg-white/5 border border-white/10 rounded-2xl p-5 text-center"
                                >
                                    {p.tipo === "Satélite"
                                        ? <Satellite className="text-blue-400 w-8 h-8 mx-auto mb-2" />
                                        : <Zap className="text-blue-400 w-8 h-8 mx-auto mb-2" />
                                    }
                                    <div className="font-bold">{p.nome}</div>
                                    <div className="text-white/40 text-xs mt-1">{p.tipo}</div>
                                    <div className="flex items-center justify-center gap-1 mt-2">
                                        <Star className="w-3 h-3 text-yellow-400" />
                                        <span className="text-sm text-yellow-400">{p.avaliacao}</span>
                                    </div>
                                </motion.div>
                            ))}
                        </div>

                        {/* LINHAS */}
                        {[
                            { label: "Velocidade", render: (p: typeof planos[0]) => `${p.velocidade} Mbps` },
                            { label: "Latência", render: (p: typeof planos[0]) => p.latencia },
                            { label: "Mensalidade", render: (p: typeof planos[0]) => `R$ ${p.preco.toFixed(2)}` },
                            { label: "Franquia", render: (p: typeof planos[0]) => p.franquia },
                            { label: "Contrato", render: (p: typeof planos[0]) => p.contrato },
                            { label: "Instalação", render: (p: typeof planos[0]) => p.instalacao },
                        ].map((row, i) => (
                            <motion.div
                                key={i}
                                initial={{ opacity: 0, x: -10 }}
                                whileInView={{ opacity: 1, x: 0 }}
                                transition={{ delay: i * 0.05 }}
                                className="grid gap-4 mb-2"
                                style={{ gridTemplateColumns: `160px repeat(${comparados.length}, 1fr)` }}
                            >
                                <div className="flex items-center text-white/40 text-sm px-2">{row.label}</div>
                                {comparados.map((p) => (
                                    <div key={p.id} className="bg-white/5 border border-white/10 rounded-xl p-4 text-center text-sm font-medium">
                                        {row.render(p)}
                                    </div>
                                ))}
                            </motion.div>
                        ))}

                        {/* PROS */}
                        <div className="grid gap-4 mt-6" style={{ gridTemplateColumns: `160px repeat(${comparados.length}, 1fr)` }}>
                            <div className="text-white/40 text-sm px-2 pt-2">Positivos</div>
                            {comparados.map((p) => (
                                <div key={p.id} className="bg-white/5 border border-white/10 rounded-xl p-4">
                                    <ul className="flex flex-col gap-2">
                                        {p.pros.map((pro, j) => (
                                            <li key={j} className="flex items-start gap-2 text-xs text-white/60">
                                                <CheckCircle className="w-3 h-3 text-green-400 flex-shrink-0 mt-0.5" />
                                                {pro}
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            ))}
                        </div>

                        {/* CONTRAS */}
                        <div className="grid gap-4 mt-2" style={{ gridTemplateColumns: `160px repeat(${comparados.length}, 1fr)` }}>
                            <div className="text-white/40 text-sm px-2 pt-2">Negativos</div>
                            {comparados.map((p) => (
                                <div key={p.id} className="bg-white/5 border border-white/10 rounded-xl p-4">
                                    <ul className="flex flex-col gap-2">
                                        {p.contras.map((contra, j) => (
                                            <li key={j} className="flex items-start gap-2 text-xs text-white/60">
                                                <XCircle className="w-3 h-3 text-red-400 flex-shrink-0 mt-0.5" />
                                                {contra}
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            ))}
                        </div>

                        {/* CTA */}
                        <div className="grid gap-4 mt-4" style={{ gridTemplateColumns: `160px repeat(${comparados.length}, 1fr)` }}>
                            <div />
                            {comparados.map((p) => (
                                <motion.button
                                    key={p.id}
                                    whileTap={{ scale: 0.95 }}
                                    className="bg-blue-600 hover:bg-blue-500 transition text-white font-bold py-3 rounded-xl text-sm flex items-center justify-center gap-2"
                                >
                                    Contratar <ArrowRight className="w-4 h-4" />
                                </motion.button>
                            ))}
                        </div>

                    </div>
                </section>

                {/* CTA FINAL */}
                <section className="px-6 pb-8">
                    <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-purple-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
                        <BarChart2 className="text-blue-400 w-10 h-10 mx-auto mb-4" />
                        <h3 className="font-bold text-xl mb-2">Quer ver provedores da sua cidade?</h3>
                        <p className="text-white/50 text-sm mb-6">
                            Compare todos os provedores disponíveis no seu endereço específico.
                        </p>
                        <a
                            href="/"
                            className="inline-block bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm"
                        >
                            Buscar na minha cidade
                        </a>
                    </div>
                </section>

            </main>
            <Footer />
        </>
    );
}
