import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const cep = searchParams.get("cep")?.replace(/\D/g, "");

  if (!cep || cep.length !== 8) {
    return NextResponse.json({ error: "CEP inválido" }, { status: 400 });
  }

  try {
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();

    if (data.erro) {
      return NextResponse.json({ error: "CEP não encontrado" }, { status: 404 });
    }

    const cidade = data.localidade;
    const estado = data.uf;

    const slug = cidade
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/\s+/g, "-")
      .replace(/[^a-z0-9-]/g, "");

    return NextResponse.json({
      cidade,
      estado,
      slug: `${slug}-${estado.toLowerCase()}`,
      cep: data.cep,
      bairro: data.bairro,
    });
  } catch {
    return NextResponse.json({ error: "Erro ao buscar CEP" }, { status: 500 });
  }
}
