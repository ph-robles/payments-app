import Navbar from '@/components/Navbar'; import Footer from '@/components/Footer'; import { Gauge, Wifi, Download, Upload, Zap, ShieldCheck } from 'lucide-react'; import SpeedTestClient from './SpeedTestClient';

export default function SpeedTestPage(){ return ( <> <Navbar />

   <main className='min-h-screen bg-[#1c1c24] text-white pt-24 pb-16'>
    <section className='relative px-6 py-16 border-b border-white/10 overflow-hidden'>
      <div className='absolute inset-0 bg-gradient-to-br from-blue-900/20 via-transparent to-purple-900/10' />
      <div className='max-w-6xl mx-auto relative z-10'>
        <div className='inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono px-3 py-1.5 rounded-full mb-6 uppercase tracking-widest'>
          <Gauge className='w-3 h-3'/> Ferramenta gratuita
        </div>
        <h1 className='text-4xl md:text-5xl font-bold mb-4'>Teste de Velocidade <span className='text-blue-400'>Fibrado</span></h1>
        <p className='text-white/50 text-lg max-w-2xl'>Meça ping, download e upload em segundos com visual profissional.</p>
      </div>
    </section><section className='px-6 py-8 border-b border-white/10'>
  <div className='max-w-6xl mx-auto grid grid-cols-3 gap-4'>
    {[
      ['Tempo real','Resultados instantâneos'],
      ['100%','Gratuito'],
      ['Seguro','Sem cadastro']
    ].map((s,i)=>(<div key={i} className='bg-white/5 border border-white/10 rounded-2xl p-4 text-center'><div className='text-xl font-bold text-blue-400'>{s[0]}</div><div className='text-white/40 text-xs mt-1'>{s[1]}</div></div>))}
  </div>
</section>

<section className='px-6 py-12'>
  <div className='max-w-5xl mx-auto'>
    <SpeedTestClient />
  </div>
</section>

<section className='px-6 pb-8'>
  <div className='max-w-5xl mx-auto grid md:grid-cols-3 gap-4'>
    {[
      [Wifi,'Ping baixo melhora jogos e chamadas'],
      [Download,'Download alto acelera streaming'],
      [Upload,'Upload alto ajuda lives e backups']
    ].map(([Icon,text],i)=>(<div key={i} className='bg-white/5 border border-white/10 rounded-2xl p-6'><Icon className='text-blue-400 mb-3'/><p className='text-white/60 text-sm'>{text}</p></div>))}
  </div>
</section>

   </main>
   <Footer />
  </>
 )
}
