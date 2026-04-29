import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { notFound } from "next/navigation";
import { ChevronRight, Clock, User, ArrowRight, BookOpen } from "lucide-react";
import Link from "next/link";
import { supabase } from "@/lib/supabase";

async function getArtigo(slug: string) {
  const { data, error } = await supabase
    .from("artigos")
    .select("*")
    .eq("slug", slug)
    .eq("publicado", true)
    .single();

  if (error || !data) return null;
  return data;
}

async function getArtigosRelacionados(slug: string, tag: string) {
  const { data } = await supabase
    .from("artigos")
    .select("slug, titulo, emoji, tempo, tag")
    .eq("publicado", true)
    .neq("slug", slug)
    .limit(3);

  return data ?? [];
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const artigo = await getArtigo(slug);
  if (!artigo) return {};
  return {
    title: artigo.titulo,
    description: artigo.descricao,
    openGraph: {
      title: `${artigo.titulo} | Fibrado`,
      description: artigo.descricao,
      url: `https://fibrado.com.br/guias/${slug}`,
    },
  };
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

export default async function ArtigoPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const artigo = await getArtigo(slug);

  if (!artigo) notFound();

  const relacionados = await getArtigosRelacionados(slug, artigo.tag);
  const paragrafos = artigo.conteudo.trim().split("\n");

  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-12 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />

          <div className="max-w-3xl mx-auto relative z-10">

            {/* BREADCRUMB */}
            <div className="flex items-center gap-2 text-white/30 text-sm mb-6 flex-wrap">
              <Link href="/" className="hover:text-white transition">Início</Link>
              <ChevronRight className="w-3 h-3" />
              <Link href="/guias" className="hover:text-white transition">Guias</Link>
              <ChevronRight className="w-3 h-3" />
              <span className="text-white/60 truncate">{artigo.titulo}</span>
            </div>

            {/* TAG + TEMPO */}
            <div className="flex items-center gap-3 mb-4 flex-wrap">
              <span className={`text-xs px-2 py-0.5 rounded-full border ${tagColors[artigo.tag_color] ?? tagColors.blue}`}>
                {artigo.tag}
              </span>
              <span className="flex items-center gap-1 text-white/30 text-xs">
                <Clock className="w-3 h-3" /> {artigo.tempo} de leitura
              </span>
            </div>

            {/* TÍTULO */}
            <h1 className="text-3xl md:text-4xl font-bold mb-4 leading-tight">
              {artigo.titulo}
            </h1>

            <p className="text-white/50 text-lg mb-6">{artigo.descricao}</p>

            <div className="flex items-center gap-4 text-white/30 text-sm">
              <span className="flex items-center gap-1">
                <User className="w-4 h-4" /> {artigo.autor} · Técnico de Telecom
              </span>
              <span className="flex items-center gap-1">
                <BookOpen className="w-4 h-4" /> {artigo.tempo} de leitura
              </span>
            </div>
          </div>
        </section>

        {/* CONTEÚDO */}
        <section className="px-6 py-12">
          <div className="max-w-3xl mx-auto">
            <article>
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
                    <li key={i} className="text-white/70 my-1.5 list-none flex items-start gap-2 ml-2">
                      <span className="w-1.5 h-1.5 bg-blue-400 rounded-full mt-2 flex-shrink-0" />
                      {linha.replace("- ", "")}
                    </li>
                  );
                }
                if (linha.trim() === "") return <div key={i} className="my-3" />;
                return <p key={i} className="text-white/70 leading-relaxed my-3">{linha}</p>;
              })}
            </article>

            {/* CTA */}
            <div className="mt-12 bg-gradient-to-r from-blue-900/30 to-blue-800/10 border border-blue-500/20 rounded-2xl p-6 text-center">
              <h3 className="font-bold text-lg mb-2">Compare provedores na sua cidade</h3>
              <p className="text-white/50 text-sm mb-4">Veja qual internet está disponível no seu endereço agora.</p>
              <Link href="/" className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-6 py-3 rounded-xl text-sm">
                Buscar provedores <ArrowRight className="w-4 h-4" />
              </Link>
            </div>

            {/* ARTIGOS RELACIONADOS */}
            {relacionados.length > 0 && (
              <div className="mt-10">
                <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-4">
                  Leia também
                </p>
                <div className="flex flex-col gap-3">
                  {relacionados.map((r: any) => (
                    <Link
                      key={r.slug}
                      href={`/guias/${r.slug}`}
                      className="group bg-white/5 hover:bg-blue-500/5 border border-white/10 hover:border-blue-500/30 rounded-xl p-4 transition-all flex items-center gap-3"
                    >
                      <span className="text-2xl">{r.emoji}</span>
                      <div className="flex-1">
                        <span className="text-white/70 group-hover:text-white transition text-sm font-medium">
                          {r.titulo}
                        </span>
                        <div className="flex items-center gap-1 text-white/30 text-xs mt-0.5">
                          <Clock className="w-3 h-3" /> {r.tempo}
                        </div>
                      </div>
                      <ArrowRight className="w-4 h-4 text-white/20 group-hover:text-blue-400 transition flex-shrink-0" />
                    </Link>
                  ))}
                </div>
              </div>
            )}

            {/* VER TODOS */}
            <div className="mt-6">
              <Link
                href="/guias"
                className="group bg-white/5 hover:bg-blue-500/5 border border-white/10 hover:border-blue-500/30 rounded-2xl p-5 transition-all flex items-center justify-between"
              >
                <div className="flex items-center gap-3">
                  <BookOpen className="text-blue-400 w-5 h-5" />
                  <span className="text-white/70 group-hover:text-white transition text-sm">
                    Ver todos os artigos
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
