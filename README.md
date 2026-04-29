"use client";

import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { notFound } from "next/navigation";
import { ChevronRight, Clock, User, ArrowRight, BookOpen } from "lucide-react";
import Link from "next/link";
import { motion } from "framer-motion";
import { use } from "react";

const artigos: Record<string, {
  titulo: string;
  descricao: string;
  tempo: string;
  tag: string;
  tagColor: string;
  conteudo: string;
}> = {
  "melhor-internet-petropolis-rj-2026": {
    titulo: "Melhor internet em Petrópolis RJ 2026",
    descricao: "Compare os melhores provedores de internet disponíveis em Petrópolis. Fibra, satélite e rádio — guia técnico atualizado.",
    tempo: "5 min",
    tag: "Cidade",
    tagColor: "blue",
    conteudo: `Petrópolis é uma das cidades serranas do Rio de Janeiro com maior crescimento no acesso à internet de alta velocidade. Em 2026, moradores e empresas têm mais opções do que nunca — mas nem todas entregam o que prometem.

## Provedores disponíveis em Petrópolis

### Claro Fibra
A Claro é a operadora com maior cobertura em Petrópolis, atendendo principalmente o centro e bairros como Quitandinha, Valparaíso e Alto da Serra. Oferece planos a partir de R$99,90/mês com velocidades de até 600 Mbps.

**Pontos positivos:** cobertura ampla, velocidade estável, instalação grátis.
**Pontos negativos:** fidelidade de 12 meses, suporte demorado.

### Vivo Fibra
A Vivo atende partes do centro e região do Carangola. Planos a partir de R$109,99/mês com até 500 Mbps. Melhor avaliação de satisfação entre os clientes da cidade.

### Starlink
Para quem mora em condomínios de altitude, zona rural de Petrópolis ou regiões sem cobertura de fibra — o Starlink é a melhor opção disponível. Velocidade média de 100–200 Mbps com latência de 20–40ms.

**Custo:** R$236/mês + kit de R$999 a R$1.680.

## Qual escolher em Petrópolis?

- **Centro e bairros urbanos:** Claro Fibra ou Vivo Fibra
- **Regiões serranas e rurais:** Starlink
- **Melhor custo-benefício:** Claro Fibra 300 Mbps

## Teste sua internet agora

Antes de contratar, acesse fast.com ou speedtest.net e teste a velocidade atual. Se estiver abaixo do contratado, você tem direito a rescisão sem multa.`,
  },

  "starlink-vale-a-pena-rio-de-janeiro": {
    titulo: "Starlink vale a pena no Rio de Janeiro?",
    descricao: "Análise técnica completa do Starlink no RJ. Velocidade real, latência, cobertura e comparativo com fibra óptica.",
    tempo: "7 min",
    tag: "Satélite",
    tagColor: "purple",
    conteudo: `O Starlink chegou ao Brasil prometendo revolucionar o acesso à internet em áreas remotas. Mas vale a pena no Rio de Janeiro, onde já existe cobertura de fibra óptica em boa parte do estado?

## O que é o Starlink?

O Starlink é o serviço de internet via satélite de órbita baixa (LEO) da SpaceX. Diferente dos satélites convencionais que ficam a 35.000 km de altitude, os satélites Starlink orbitam a 550 km — o que reduz drasticamente a latência.

## Velocidade real no RJ

Nos testes realizados em diferentes regiões do Rio de Janeiro, o Starlink entrega:

- **Velocidade de download:** 80–200 Mbps
- **Velocidade de upload:** 10–20 Mbps
- **Latência:** 20–40ms
- **Estabilidade:** cai em chuvas fortes por 2–5 minutos

## Quando o Starlink vale a pena no RJ?

**Vale a pena se você:**
- Mora em zona rural, condomínio de altitude ou área sem fibra
- Precisa de internet em sítio, fazenda ou chácara
- Quer backup de conexão para home office crítico

**Não vale a pena se você:**
- Mora em área urbana com fibra disponível
- Tem orçamento limitado
- Usa muito streaming em 4K

## Veredicto técnico

Como técnico de telecom que trabalha no campo, minha análise é direta: o Starlink é a melhor solução para quem não tem fibra. Para quem tem fibra disponível, só faz sentido como backup.`,
  },

  "internet-rural-interior-rj": {
    titulo: "Internet rural no interior do RJ: qual escolher em 2026",
    descricao: "Guia completo para escolher internet no interior do Rio de Janeiro. Starlink, 4G rural e satélite comparados por um técnico de campo.",
    tempo: "6 min",
    tag: "Rural",
    tagColor: "green",
    conteudo: `Quem mora no interior fluminense sabe a dificuldade: a fibra óptica não chega, o 4G é instável e o satélite convencional tem latência de 600ms. Em 2026, as opções melhoraram — mas ainda exigem atenção na hora de escolher.

## Opções disponíveis no interior do RJ

### 1. Starlink (Recomendado)
Melhor opção para a grande maioria das cidades do interior fluminense. Cobre desde o Vale do Paraíba até o Norte Fluminense com velocidade consistente.

### 2. Internet 4G Rural
Se sua propriedade tem cobertura de sinal 4G de pelo menos 2 barras, um roteador rural com antena direcional pode entregar 20–80 Mbps por R$100–150/mês.

### 3. Provedores Regionais
Muitas cidades do interior têm provedores locais que usam rádio ou fibra própria. Geralmente mais baratos que as grandes operadoras e com suporte mais ágil.

### 4. Satélite Convencional (Evite)
Latência de 600ms+. Inviável para videochamadas, jogos e qualquer uso moderno.

## Recomendação por região

- **Serrana (Petrópolis, Teresópolis):** Starlink ou fibra local
- **Norte Fluminense (Campos, Macaé):** Starlink ou 4G rural
- **Costa Verde (Angra, Paraty):** Starlink

## Dica de técnico

Antes de contratar qualquer serviço de rádio ou 4G rural, peça um teste de 7 dias. Qualquer provedor sério oferece isso.`,
  },

  "claro-vs-vivo-fibra-rj": {
    titulo: "Claro vs Vivo Fibra: qual é melhor no RJ em 2026",
    descricao: "Comparativo técnico entre Claro Fibra e Vivo Fibra no Rio de Janeiro. Velocidade, estabilidade, preço e suporte analisados.",
    tempo: "5 min",
    tag: "Comparativo",
    tagColor: "orange",
    conteudo: `Claro e Vivo são as duas maiores operadoras de fibra óptica do Rio de Janeiro. Mas qual entrega mais pelo seu dinheiro em 2026?

## Cobertura no RJ

**Claro Fibra** tem a maior cobertura do estado, atendendo praticamente todas as cidades da Região Metropolitana, Baixada Fluminense, Serrana e parte do interior.

**Vivo Fibra** tem cobertura menor, focada principalmente na capital, Niterói e algumas cidades da Região Metropolitana.

**Vantagem: Claro**

## Velocidade e estabilidade

Nos testes realizados em campo, a Vivo apresenta velocidade mais consistente durante horários de pico (19h–22h), enquanto a Claro tende a cair mais em bairros de alta densidade.

**Vantagem: Vivo**

## Preço

- **300 Mbps:** Claro R$89,99 vs Vivo R$99,99
- **500 Mbps:** Claro R$99,90 vs Vivo R$109,99
- **1 Gbps:** Claro R$129,99 vs Vivo R$139,99

**Vantagem: Claro**

## Veredicto final

- **Escolha a Claro** se preço e cobertura são prioridade
- **Escolha a Vivo** se estabilidade no horário de pico é essencial`,
  },

  "como-testar-velocidade-real-internet": {
    titulo: "Como testar a velocidade real da sua internet",
    descricao: "Guia técnico para medir a velocidade real da internet. Aprenda a identificar se seu provedor está entregando o que prometeu.",
    tempo: "4 min",
    tag: "Dica técnica",
    tagColor: "cyan",
    conteudo: `Seu provedor promete 300 Mbps mas você sente a internet lenta? Aprenda a testar a velocidade real e saber se está sendo enganado.

## Por que o teste de velocidade pode mentir

A maioria das pessoas faz o teste errado e aceita um resultado abaixo do contratado sem questionar. Fatores que distorcem o resultado:

- **Wi-Fi lento:** o gargalo pode estar no roteador, não no provedor
- **Hora do teste:** fazer às 21h no horário de pico dá resultado diferente das 10h
- **Servidor do teste:** alguns provedores priorizam tráfego para servidores de teste

## Como fazer o teste correto

### Passo 1 — Conecte no cabo
Use um cabo de rede diretamente no roteador. Wi-Fi sempre perde velocidade.

### Passo 2 — Feche tudo
Feche todos os programas, apps e outros dispositivos conectados à rede.

### Passo 3 — Use os sites certos
- **fast.com** (Netflix) — mais difícil de o provedor trapacear
- **speedtest.net** — o mais conhecido
- **brasilbandalarga.com.br** — teste oficial do Anatel

### Passo 4 — Teste 3 vezes em horários diferentes
- Manhã (9h–11h), Tarde (15h–17h), Noite (20h–22h)

## O que fazer se a velocidade estiver abaixo

Se a média ficou abaixo de 80% do contratado, você tem direito por lei a:

1. Solicitar reparo sem custo
2. Abater proporcional na fatura
3. Rescindir o contrato sem multa

**Guarde os prints dos testes** — eles são prova para reclamação no Anatel.`,
  },
};

const tagColors: Record<string, string> = {
  blue: "bg-blue-500/10 text-blue-400 border-blue-500/20",
  purple: "bg-purple-500/10 text-purple-400 border-purple-500/20",
  green: "bg-green-500/10 text-green-400 border-green-500/20",
  orange: "bg-orange-500/10 text-orange-400 border-orange-500/20",
  cyan: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20",
};

export default function ArtigoPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = use(params);
  const artigo = artigos[slug];

  if (!artigo) notFound();

  const paragrafos = artigo.conteudo.trim().split("\n");

  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO DO ARTIGO */}
        <section className="relative px-6 py-12 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

          {/* PARTÍCULAS */}
          {[...Array(10)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-blue-400/20 rounded-full"
              style={{ top: `${Math.random() * 100}%`, left: `${Math.random() * 100}%` }}
              animate={{ opacity: [0.1, 0.6, 0.1] }}
              transition={{ duration: 3 + Math.random() * 3, repeat: Infinity, delay: Math.random() * 2 }}
            />
          ))}

          <div className="max-w-3xl mx-auto relative z-10">

            {/* BREADCRUMB */}
            <div className="flex items-center gap-2 text-white/30 text-sm mb-6 flex-wrap">
              <Link href="/" className="hover:text-white transition">Início</Link>
              <ChevronRight className="w-3 h-3" />
              <Link href="/guias" className="hover:text-white transition">Guias</Link>
              <ChevronRight className="w-3 h-3" />
              <span className="text-white/60 truncate">{artigo.titulo}</span>
            </div>

            {/* TAG */}
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className="flex items-center gap-3 mb-4 flex-wrap"
            >
              <span className={`text-xs px-2 py-0.5 rounded-full border ${tagColors[artigo.tagColor]}`}>
                {artigo.tag}
              </span>
              <span className="flex items-center gap-1 text-white/30 text-xs">
                <Clock className="w-3 h-3" /> {artigo.tempo} de leitura
              </span>
            </motion.div>

            {/* TÍTULO */}
            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1 }}
              className="text-3xl md:text-4xl font-bold mb-4 leading-tight"
            >
              {artigo.titulo}
            </motion.h1>

            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.2 }}
              className="text-white/50 text-lg mb-6"
            >
              {artigo.descricao}
            </motion.p>

            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.3 }}
              className="flex items-center gap-4 text-white/30 text-sm"
            >
              <span className="flex items-center gap-1">
                <User className="w-4 h-4" /> Raphael Robles · Técnico de Telecom
              </span>
              <span className="flex items-center gap-1">
                <BookOpen className="w-4 h-4" /> {artigo.tempo} de leitura
              </span>
            </motion.div>
          </div>
        </section>

        {/* CONTEÚDO */}
        <section className="px-6 py-12">
          <div className="max-w-3xl mx-auto">
            <motion.article
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
            >
              {paragrafos.map((linha, i) => {
                if (linha.startsWith("## ")) {
                  return (
                    <h2 key={i} className="text-xl font-bold text-white mt-10 mb-4 pb-2 border-b border-white/10 flex items-center gap-2">
                      <span className="w-1 h-6 bg-blue-400 rounded-full flex-shrink-0" />
                      {linha.replace("## ", "")}
                    </h2>
                  );
                }
                if (linha.startsWith("### ")) {
                  return <h3 key={i} className="text-lg font-bold text-blue-400 mt-6 mb-3">{linha.replace("### ", "")}</h3>;
                }
                if (linha.startsWith("**") && linha.endsWith("**")) {
                  return <p key={i} className="font-bold text-white mt-4">{linha.replace(/\*\*/g, "")}</p>;
                }
                if (linha.startsWith("- ")) {
                  return (
                    <li key={i} className="text-white/70 ml-4 my-1.5 list-none flex items-start gap-2">
                      <span className="w-1.5 h-1.5 bg-blue-400 rounded-full mt-2 flex-shrink-0" />
                      {linha.replace("- ", "")}
                    </li>
                  );
                }
                if (linha.trim() === "") return <div key={i} className="my-3" />;
                return <p key={i} className="text-white/70 leading-relaxed my-3">{linha}</p>;
              })}
            </motion.article>

            {/* CTA */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              className="mt-12 bg-gradient-to-r from-blue-900/30 to-blue-800/10 border border-blue-500/20 rounded-2xl p-6 text-center"
            >
              <h3 className="font-bold text-lg mb-2">Compare provedores na sua cidade</h3>
              <p className="text-white/50 text-sm mb-4">Veja qual internet está disponível no seu endereço agora.</p>
              <Link href="/" className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm">
                Buscar provedores <ArrowRight className="w-4 h-4" />
              </Link>
            </motion.div>

            {/* OUTROS GUIAS */}
            <div className="mt-10">
              <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-4">
                Mais guias técnicos
              </p>
              <Link
                href="/guias"
                className="group bg-white/5 hover:bg-blue-500/5 border border-white/10 hover:border-blue-500/30 rounded-2xl p-5 transition-all flex items-center justify-between"
              >
                <div className="flex items-center gap-3">
                  <BookOpen className="text-blue-400 w-5 h-5" />
                  <span className="text-white/70 group-hover:text-white transition text-sm">
                    Ver todos os guias técnicos
                  </span>
                </div>
                <ArrowRight className="w-4 h-4 text-white/30 group-hover:text-blue-400 transition" />
              </Link>
            </div>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
