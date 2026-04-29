function OrbitalAnimation() {
  return (
    <div className="relative w-64 h-64 mx-auto">

      {/* TERRA */}
      <div className="absolute bottom-4 left-1/2 -translate-x-1/2 w-32 h-32 rounded-full bg-gradient-to-br from-blue-600/60 to-blue-900/80 border border-blue-500/30 overflow-hidden">
        <div className="absolute top-4 left-4 w-10 h-6 rounded-full bg-green-700/50" />
        <div className="absolute top-8 left-12 w-14 h-7 rounded-full bg-green-700/40" />
        <div className="absolute top-3 right-4 w-6 h-4 rounded-full bg-green-700/50" />
        <div className="absolute inset-0 rounded-full bg-blue-400/10 border border-blue-400/20" />
      </div>

      {/* ÓRBITA */}
      <div className="absolute top-8 left-1/2 -translate-x-1/2 w-48 h-48 rounded-full border border-blue-400/20 border-dashed" />

      {/* SATÉLITE ORBITANDO */}
      <motion.div
        className="absolute w-48 h-48 top-8 left-1/2 -translate-x-1/2"
        animate={{ rotate: 360 }}
        transition={{ duration: 6, repeat: Infinity, ease: "linear" }}
        style={{ originX: "50%", originY: "50%" }}
      >
        <div className="absolute -top-2 left-1/2 -translate-x-1/2">
          <div className="w-6 h-4 bg-blue-500/80 rounded-sm border border-blue-400/50 relative">
            <div className="absolute -left-4 top-1/2 -translate-y-1/2 w-3 h-1.5 bg-blue-300/60" />
            <div className="absolute -right-4 top-1/2 -translate-y-1/2 w-3 h-1.5 bg-blue-300/60" />
          </div>
        </div>
      </motion.div>

      {/* SEGUNDO SATÉLITE */}
      <motion.div
        className="absolute w-36 h-36 top-14 left-1/2 -translate-x-1/2"
        animate={{ rotate: -360 }}
        transition={{ duration: 9, repeat: Infinity, ease: "linear" }}
        style={{ originX: "50%", originY: "50%" }}
      >
        <div className="absolute -top-1.5 left-1/2 -translate-x-1/2">
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
