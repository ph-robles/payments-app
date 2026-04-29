import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { BookOpen, Clock, ChevronRight, ArrowRight, Zap } from "lucide-react";
import { supabase } from "@/lib/supabase";

async function getArtigos() {
  const { data, error } = await supabase
    .from("artigos")
    .select("slug, titulo, descricao, tag, tag_color, emoji, tempo")
    .eq("publicado", true)
    .order("criado_em", { ascending: false });

  if (error || !data) return [];
  return data;
}

const tagColors: Record<string, string> = {
  blue: "bg-blue-500/10 text-blue-400 border-blue-500/20",
  purple: "bg-purple-500/10 text-purple-400 border-purple-500/20",
  green: "bg-green-500/10 text-green-400 border-green-500/20",
  orange: "bg-orange-500/10 text-orange-400 border-orange-500/20",
  cyan: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20",
  red: "bg-red-500/10 text-red-400 border-red-500/20",
  yellow: "bg-yellow-500/10 text-yellow-400 border-yellow-500/20",
  pink: "bg-pink-500/10 text-pink-400 border-pink-500/20",
};

export default async function GuiasPage() {
  const artigos = await getArtigos();

  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-16 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

          <div className="max-w-6xl mx-auto relative z-10">
            <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
              <BookOpen className="w-3 h-3" />
              Portal técnico independente
            </div>
            <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
              Guias e Artigos<br />
              <span className="text-blue-400">de Tecnologia</span>
            </h1>
            <p className="text-white/50 text-lg max-w-2xl">
              Internet, redes, satélite, celulares, apps e tudo sobre tecnologia.
              Conteúdo técnico independente — para leigos e especialistas.
            </p>
          </div>
        </section>

        {/* STATS */}
        <section className="px-6 py-8 border-b border-white/10">
          <div className="max-w-6xl mx-auto grid grid-cols-3 gap-4">
            {[
              { valor: `${artigos.length}`, label: "Artigos publicados" },
              { valor: "100%", label: "Gratuito" },
              { valor: "2×", label: "Novos por semana" },
            ].map((s, i) => (
              <div key={i} className="bg-white/5 border border-white/10 rounded-2xl p-4 text-center">
                <div className="text-xl font-bold text-blue-400">{s.valor}</div>
                <div className="text-white/40 text-xs mt-1">{s.label}</div>
              </div>
            ))}
          </div>
        </section>

        {/* LISTA */}
        <section className="px-6 py-12">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Todos os artigos — mais recentes primeiro
            </p>

            <div className="flex flex-col gap-4">
              {artigos.map((artigo, i) => (
                <Link
                  key={artigo.slug}
                  href={`/guias/${artigo.slug}`}
                  className="group bg-white/5 hover:bg-blue-500/5 border border-white/10 hover:border-blue-500/30 rounded-2xl p-6 transition-all flex flex-col md:flex-row md:items-center gap-4"
                >
                  <div className="text-4xl flex-shrink-0 hidden md:block">{artigo.emoji}</div>

                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2 flex-wrap">
                      <span className={`text-xs px-2 py-0.5 rounded-full border ${tagColors[artigo.tag_color] ?? tagColors.blue}`}>
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

                  <ChevronRight className="w-5 h-5 text-white/20 group-hover:text-blue-400 transition flex-shrink-0 hidden md:block" />
                </Link>
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
            <Link href="/" className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm">
              Buscar internet <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
