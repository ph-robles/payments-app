CREATE TABLE artigos (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  titulo TEXT NOT NULL,
  descricao TEXT NOT NULL,
  conteudo TEXT NOT NULL,
  tag TEXT NOT NULL,
  tag_color TEXT NOT NULL DEFAULT 'blue',
  emoji TEXT NOT NULL DEFAULT '📡',
  tempo TEXT NOT NULL DEFAULT '5 min',
  autor TEXT NOT NULL DEFAULT 'Raphael Robles',
  publicado BOOLEAN DEFAULT true,
  criado_em TIMESTAMP DEFAULT NOW()
);

-- Migra os 5 artigos já existentes
INSERT INTO artigos (slug, titulo, descricao, conteudo, tag, tag_color, emoji, tempo) VALUES
(
  'melhor-internet-petropolis-rj-2026',
  'Melhor internet em Petrópolis RJ 2026',
  'Compare os melhores provedores de internet disponíveis em Petrópolis. Fibra, satélite e rádio — guia técnico atualizado.',
  'Petrópolis é uma das cidades serranas do Rio de Janeiro com maior crescimento no acesso à internet de alta velocidade. Em 2026, moradores e empresas têm mais opções do que nunca — mas nem todas entregam o que prometem.

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

Antes de contratar, acesse fast.com ou speedtest.net e teste a velocidade atual. Se estiver abaixo do contratado, você tem direito a rescisão sem multa.',
  'Cidade', 'blue', '🏙️', '5 min'
),
(
  'starlink-vale-a-pena-rio-de-janeiro',
  'Starlink vale a pena no Rio de Janeiro?',
  'Análise técnica completa do Starlink no RJ. Velocidade real, latência, cobertura e comparativo com fibra óptica.',
  'O Starlink chegou ao Brasil prometendo revolucionar o acesso à internet em áreas remotas. Mas vale a pena no Rio de Janeiro, onde já existe cobertura de fibra óptica em boa parte do estado?

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

Como técnico de telecom que trabalha no campo, minha análise é direta: o Starlink é a melhor solução para quem não tem fibra. Para quem tem fibra disponível, só faz sentido como backup.',
  'Satélite', 'purple', '🛰️', '7 min'
),
(
  'internet-rural-interior-rj',
  'Internet rural no interior do RJ: qual escolher em 2026',
  'Guia completo para escolher internet no interior do Rio de Janeiro. Starlink, 4G rural e satélite comparados por um técnico de campo.',
  'Quem mora no interior fluminense sabe a dificuldade: a fibra óptica não chega, o 4G é instável e o satélite convencional tem latência de 600ms. Em 2026, as opções melhoraram — mas ainda exigem atenção na hora de escolher.

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

Antes de contratar qualquer serviço de rádio ou 4G rural, peça um teste de 7 dias. Qualquer provedor sério oferece isso.',
  'Rural', 'green', '🌿', '6 min'
),
(
  'claro-vs-vivo-fibra-rj',
  'Claro vs Vivo Fibra: qual é melhor no RJ em 2026',
  'Comparativo técnico entre Claro Fibra e Vivo Fibra no Rio de Janeiro. Velocidade, estabilidade, preço e suporte analisados.',
  'Claro e Vivo são as duas maiores operadoras de fibra óptica do Rio de Janeiro. Mas qual entrega mais pelo seu dinheiro em 2026?

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
- **Escolha a Vivo** se estabilidade no horário de pico é essencial',
  'Comparativo', 'orange', '⚡', '5 min'
),
(
  'como-testar-velocidade-real-internet',
  'Como testar a velocidade real da sua internet',
  'Guia técnico para medir a velocidade real da internet. Aprenda a identificar se seu provedor está entregando o que prometeu.',
  'Seu provedor promete 300 Mbps mas você sente a internet lenta? Aprenda a testar a velocidade real e saber se está sendo enganado.

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

**Guarde os prints dos testes** — eles são prova para reclamação no Anatel.',
  'Dica técnica', 'cyan', '📡', '4 min'
);
