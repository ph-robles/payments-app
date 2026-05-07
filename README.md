import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Link from "next/link";
import { Zap, ArrowRight, CheckCircle, AlertTriangle, XCircle } from "lucide-react";

export const metadata = {
  title: "Teste de Velocidade da Internet | Fibrado",
  description: "Teste a velocidade real da sua internet agora. Descubra se seu provedor está entregando o que prometeu.",
};

export default function TesteVelocidadePage() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-[#1c1c24] text-white pt-24 pb-16">

        {/* HERO */}
        <section className="relative px-6 py-12 border-b border-white/10 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-cyan-900/10 pointer-events-none" />
          <div className="max-w-4xl mx-auto relative z-10 text-center">
            <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest">
              <Zap className="w-3 h-3" />
              Ferramenta gratuita
            </div>
            <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
              Teste sua<br />
              <span className="text-blue-400">velocidade agora</span>
            </h1>
            <p className="text-white/50 text-lg max-w-xl mx-auto">
              Descubra a velocidade real da sua internet e se seu provedor
              está entregando o que você está pagando.
            </p>
          </div>
        </section>

        {/* SPEEDTEST EMBED */}
        <section className="px-6 py-12">
          <div className="max-w-3xl mx-auto">
            <div className="bg-white/5 border border-white/10 rounded-2xl overflow-hidden">
              <iframe
                src="https://embed.speedtest.net/embed/widget.js"
                width="100%"
                height="550"
                style={{ border: "none" }}
              />
            </div>
            <p className="text-white/30 text-xs text-center mt-3">
              Powered by Ookla Speedtest · Resultados podem variar por horário e dispositivo
            </p>
          </div>
        </section>

        {/* COMO INTERPRETAR */}
        <section className="px-6 py-12 border-t border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Como interpretar o resultado
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-green-500/5 border border-green-500/20 rounded-2xl p-6">
                <CheckCircle className="text-green-400 w-8 h-8 mb-3" />
                <h3 className="font-bold mb-2 text-green-400">Acima de 80%</h3>
                <p className="text-white/50 text-sm">
                  Sua internet está dentro do esperado. Normal ter pequenas variações ao longo do dia.
                </p>
              </div>
              <div className="bg-yellow-500/5 border border-yellow-500/20 rounded-2xl p-6">
                <AlertTriangle className="text-yellow-400 w-8 h-8 mb-3" />
                <h3 className="font-bold mb-2 text-yellow-400">Entre 50% e 80%</h3>
                <p className="text-white/50 text-sm">
                  Pode ser horário de pico ou problema temporário. Teste em outros horários antes de reclamar.
                </p>
              </div>
              <div className="bg-red-500/5 border border-red-500/20 rounded-2xl p-6">
                <XCircle className="text-red-400 w-8 h-8 mb-3" />
                <h3 className="font-bold mb-2 text-red-400">Abaixo de 50%</h3>
                <p className="text-white/50 text-sm">
                  Abra um chamado na operadora. Guarde o print — você tem direito a reparo ou desconto na fatura.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* DICAS */}
        <section className="px-6 py-12 border-t border-white/10">
          <div className="max-w-4xl mx-auto">
            <p className="text-white/40 text-xs font-mono uppercase tracking-widest mb-8">
              Para um teste mais preciso
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {[
                { emoji: "🔌", titulo: "Use cabo de rede", texto: "Conecte o computador direto no roteador por cabo. Wi-Fi sempre perde velocidade." },
                { emoji: "📱", titulo: "Feche outros apps", texto: "Feche programas e abas abertas que possam estar consumindo internet em segundo plano." },
                { emoji: "🕐", titulo: "Teste em horários diferentes", texto: "Faça testes de manhã, tarde e noite. O horário de pico (19h–22h) costuma ser mais lento." },
                { emoji: "🔄", titulo: "Faça 3 testes seguidos", texto: "Tire a média dos 3 resultados para ter uma medição mais confiável." },
              ].map((d, i) => (
                <div key={i} className="bg-white/5 border border-white/10 rounded-2xl p-5 flex gap-4">
                  <span className="text-3xl flex-shrink-0">{d.emoji}</span>
                  <div>
                    <h3 className="font-bold mb-1">{d.titulo}</h3>
                    <p className="text-white/50 text-sm">{d.texto}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="px-6 pb-8">
          <div className="max-w-4xl mx-auto bg-gradient-to-r from-blue-900/30 to-cyan-900/20 border border-blue-500/20 rounded-2xl p-8 text-center">
            <Zap className="text-blue-400 w-10 h-10 mx-auto mb-4" />
            <h3 className="font-bold text-xl mb-2">Velocidade abaixo do esperado?</h3>
            <p className="text-white/50 text-sm mb-6">
              Compare outros provedores disponíveis na sua cidade e troque para um melhor.
            </p>
            <Link
              href="/"
              className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-500 transition text-white font-bold px-8 py-3 rounded-xl text-sm"
            >
              Comparar provedores <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </section>

      </main>
      <Footer />
    </>
  );
}
