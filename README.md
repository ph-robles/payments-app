'use client';

import { useState } from 'react'; import { motion } from 'framer-motion'; import { Button } from '@/components/ui/button'; import { Gauge, Download, Upload, Wifi } from 'lucide-react';

export default function SpeedTestClient(){ const [ping,setPing]=useState<number|null>(null); const [download,setDownload]=useState<number|null>(null); const [upload,setUpload]=useState<number|null>(null); const [running,setRunning]=useState(false); const [status,setStatus]=useState('Pronto para iniciar'); const [needle,setNeedle]=useState(0);

async function measurePing(){const t=performance.now(); await fetch('https://www.cloudflare.com/cdn-cgi/trace?ts='+Date.now(),{cache:'no-store'}); return Math.round(performance.now()-t);} async function measureDownload(){const t=performance.now(); const r=await fetch('https://speed.cloudflare.com/__down?bytes=25000000&ts='+Date.now(),{cache:'no-store'}); const b=await r.blob(); return Number(((b.size8)/((performance.now()-t)/1000)/1000000).toFixed(1));} async function measureUpload(){const payload=new Blob([new Uint8Array(5000000)]); const t=performance.now(); await fetch('https://speed.cloudflare.com/__up',{method:'POST',body:payload}); return Number(((payload.size8)/((performance.now()-t)/1000)/1000000).toFixed(1));}

async function run(){ try{ setRunning(true); setPing(null); setDownload(null); setUpload(null); setNeedle(0); setStatus('Medindo ping...'); const p=await measurePing(); setPing(p); setStatus('Medindo download...'); const d=await measureDownload(); setDownload(d); setNeedle(Math.min(d,1000)/1000*180); setStatus('Medindo upload...'); const u=await measureUpload(); setUpload(u); setStatus('Teste concluído'); }catch(e){setStatus('Erro ao executar teste');} finally{setRunning(false);} }

const cards=[ {title:'Ping',icon:Wifi,value:ping!==null?ping+' ms':'--'}, {title:'Download',icon:Download,value:download!==null?download+' Mbps':'--'}, {title:'Upload',icon:Upload,value:upload!==null?upload+' Mbps':'--'} ];

return <div className='space-y-6'>

   <div className='bg-white/5 border border-white/10 rounded-3xl p-6 md:p-10'>
    <div className='grid md:grid-cols-2 gap-8 items-center'>
      <div className='flex flex-col items-center'>
        <div className='relative w-72 h-40 overflow-hidden'>
          <div className='absolute inset-x-0 bottom-0 h-72 rounded-full border-8 border-white/10'></div>
          <motion.div className='absolute left-1/2 bottom-0 origin-bottom h-28 w-1 bg-blue-400 rounded-full' animate={{rotate:needle-90}} transition={{duration:1}} />
          <div className='absolute bottom-0 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-blue-400'></div>
        </div>
        <div className='text-4xl font-bold mt-2'>{download??0}<span className='text-base text-white/50 ml-2'>Mbps</span></div>
        <p className='text-white/40 text-sm mt-2'>{status}</p>
      </div>
      <div className='grid gap-4'>
        {cards.map((c,i)=>{const Icon=c.icon; return <div key={i} className='bg-black/20 border border-white/10 rounded-2xl p-5 flex items-center gap-4'><Icon className='text-blue-400 w-5 h-5'/><div><div className='text-white/40 text-sm'>{c.title}</div><div className='text-2xl font-bold'>{c.value}</div></div></div>})}
        <Button onClick={run} disabled={running} className='h-12 rounded-2xl text-base font-bold bg-blue-600 hover:bg-blue-500'>
          <Gauge className='w-4 h-4 mr-2'/>{running?'Executando...':'Iniciar Teste'}
        </Button>
      </div>
    </div>
   </div>
 </div>
}
