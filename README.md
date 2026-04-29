01:12:06.695 Running build in Washington, D.C., USA (East) – iad1
01:12:06.695 Build machine configuration: 2 cores, 8 GB
01:12:06.813 Cloning github.com/ph-robles/fibrado (Branch: main, Commit: e71b413)
01:12:07.190 Cloning completed: 376.000ms
01:12:09.539 Restored build cache from previous deployment (Gx4VBwTCMaQVe1tfULJP5oT9yTpu)
01:12:09.744 Running "vercel build"
01:12:10.407 Vercel CLI 51.6.1
01:12:10.663 Installing dependencies...
01:12:12.386 
01:12:12.386 up to date in 967ms
01:12:12.387 
01:12:12.387 158 packages are looking for funding
01:12:12.387   run `npm fund` for details
01:12:12.414 Detected Next.js version: 16.2.3
01:12:12.418 Running "npm run build"
01:12:12.569 
01:12:12.569 > fibrado@0.1.0 build
01:12:12.570 > next build
01:12:12.570 
01:12:13.327   Applying modifyConfig from Vercel
01:12:13.342 ▲ Next.js 16.2.3 (Turbopack)
01:12:13.343 
01:12:13.375   Creating an optimized production build ...
01:12:23.088 
01:12:23.090 > Build error occurred
01:12:23.091 Error: Turbopack build failed with 1 errors:
01:12:23.092 ./app/starlink/page.tsx:87:14
01:12:23.092 You are attempting to export "metadata" from a component marked with "use client", which is disallowed. "metadata" must be resolved on the server before the page component is rendered. Keep your page as a Server Component and move Client Component logic to a separate file. Read more: https://nextjs.org/docs/app/api-reference/functions/generate-metadata#why-generatemetadata-is-server-component-only
01:12:23.092   [90m85 |[0m }
01:12:23.092   [90m86 |[0m
01:12:23.093 [31m[1m>[0m [90m87 |[0m [36mexport[0m [36mconst[0m metadata = {
01:12:23.093   [90m   |[0m              [31m[1m^^^^^^^^[0m
01:12:23.093   [90m88 |[0m     title: [32m"Starlink no Brasil 2026"[0m,
01:12:23.093   [90m89 |[0m     description: [32m"Tudo sobre o Starlink no Brasil. Preço, velocidade, instalação e compara...[0m
01:12:23.093   [90m90 |[0m };
01:12:23.093 
01:12:23.093 Ecmascript file had an error
01:12:23.094 
01:12:23.094 Import traces:
01:12:23.094   Client Component Browser:
01:12:23.094     ./app/starlink/page.tsx [Client Component Browser]
01:12:23.094     ./app/starlink/page.tsx [Server Component]
01:12:23.094 
01:12:23.094   Client Component SSR:
01:12:23.094     ./app/starlink/page.tsx [Client Component SSR]
01:12:23.095     ./app/starlink/page.tsx [Server Component]
01:12:23.095 
01:12:23.095 
01:12:23.095     at <unknown> (./app/starlink/page.tsx:87:14)
01:12:23.142 Error: Command "npm run build" exited with 1
