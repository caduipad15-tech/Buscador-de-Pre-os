import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Comparador de Preços Inteligente",
    page_icon="💎",
    layout="wide"
)

# Estilização CSS com as novas cores ajustadas (Plus azul claro vivo, Basic verde, Premium dourado real)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');

        .stApp { 
            background-color: #0b0f19 !important; 
            font-family: 'Poppins', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, label, span { 
            font-family: 'Poppins', sans-serif !important; 
        }

        .card-base {
            background-color: #111827;
            border-radius: 20px;
            padding: 30px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        }

        /* 1. BASIC - Cor verde anterior do Plus */
        .card-basic { border: 2px solid #22c55e; }
        .card-basic h3 { color: #22c55e !important; font-weight: 800; font-size: 26px; }

        /* 2. PLUS - Azul claro bem vivo e brilhante (não fosco) */
        .card-plus { 
            border: 2px solid #00f0ff; 
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.25);
        }
        .card-plus h3 { color: #00f0ff !important; font-weight: 800; font-size: 26px; }

        /* 3. PREMIUM - Dourado real com brilho refinado */
        .card-premium {
            border: 2px solid #ffd700;
            box-shadow: 0 0 35px rgba(255, 215, 0, 0.45);
            background: linear-gradient(145deg, #111827, #1f2937);
        }
        .card-premium h3 {
            color: #ffd700 !important;
            font-weight: 800;
            font-size: 26px;
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.7);
        }

        .preco-gigante {
            font-size: 42px;
            font-weight: 900;
            color: #ffffff !important;
            margin: 15px 0 5px 0;
            line-height: 1;
        }
        .preco-gigante span { font-size: 14px; font-weight: 400; color: #9ca3af !important; }
        .sub-info { font-size: 13px; font-weight: 600; margin-bottom: 20px; }

        ul.lista-beneficios { list-style: none; padding: 0; margin: 0 0 25px 0; }
        ul.lista-beneficios li {
            color: #e2e8f0 !important;
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 12px;
            border-bottom: 1px solid #1f2937;
            padding-bottom: 8px;
        }

        div[data-testid="stButton"] button {
            background-color: #f3f4f6 !important;
            color: #0b0f19 !important;
            border-radius: 12px !important;
            font-weight: 800 !important;
            font-size: 15px !important;
            border: none !important;
            padding: 12px !important;
            width: 100% !important;
        }
        div[data-testid="stButton"] button:hover { background-color: #ffffff !important; }

        div[role="radiogroup"] { justify-content: center; }
        div[role="radiogroup"] label p { color: #ffffff !important; font-weight: 600; }

        .section-box {
            background-color: #111827;
            border: 1px solid #1f2937;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 900; font-size: 36px; margin-top: 10px;'>Escolha seu plano ideal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 15px; margin-bottom: 30px;'>Selecione o melhor plano para você e economize com segurança total.</p>", unsafe_allow_html=True)

col_pad1, col_center, col_pad2 = st.columns([2, 2, 2])
with col_center:
    tipo_cobranca = st.radio(
        "Período de cobrança",
        ["Mensal", "Anual (Economize)"],
        horizontal=True,
        label_visibility="collapsed",
        key="radio_cobranca_principal"
    )

st.write("") 
st.write("")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    preco_basic = "R$ 9,99" if tipo_cobranca == "Mensal" else "R$ 6,99"
    sub_basic = "7 dias grátis para testar" if tipo_cobranca == "Mensal" else "R$ 83,88 cobrado anualmente"
    st.markdown(f"""
        <div class="card-base card-basic">
            <div>
                <h3>Basic</h3>
                <div class="preco-gigante">{preco_basic} <span>/ mês</span></div>
                <div class="sub-info" style="color: #22c55e;">{sub_basic}</div>
                <ul class="lista-beneficios">
                    <li>✓ Comparação de preços</li>
                    <li>✓ Preço final com frete</li>
                    <li>✓ Histórico de preços</li>
                    <li>✓ Análise básica de segurança</li>
                    <li>✓ 3 alertas de preço</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Iniciar 7 dias grátis", key="btn_basic_unico", use_container_width=True)

with col2:
    preco_plus = "R$ 19,99" if tipo_cobranca == "Mensal" else "R$ 15,99"
    sub_plus = "Mais popular" if tipo_cobranca == "Mensal" else "R$ 191,88 cobrado anualmente"
    st.markdown(f"""
        <div class="card-base card-plus">
            <div>
                <h3>Plus</h3>
                <div class="preco-gigante">{preco_plus} <span>/ mês</span></div>
                <div class="sub-info" style="color: #00f0ff;">{sub_plus}</div>
                <ul class="lista-beneficios">
                    <li>✓ Comparação de preços</li>
                    <li>✓ Preço final com frete</li>
                    <li>✓ Histórico de preços</li>
                    <li>✓ Análise básica de segurança</li>
                    <li>✓ 10 alertas de preço</li>
                    <li>✓ 2 cupons semanais</li>
                    <li>✓ Notificação de queda de preços</li>
                    <li>✓ Índice de economia</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Assinar Plus", key="btn_plus_unico", use_container_width=True)

with col3:
    preco_premium = "R$ 29,99" if tipo_cobranca == "Mensal" else "R$ 24,99"
    sub_premium = "Acesso Total e IA" if tipo_cobranca == "Mensal" else "R$ 299,88 cobrado anualmente"
    st.markdown(f"""
        <div class="card-base card-premium">
            <div>
                <h3>Premium ⭐</h3>
                <div class="preco-gigante">{preco_premium} <span>/ mês</span></div>
                <div class="sub-info" style="color: #ffd700;">{sub_premium}</div>
                <ul class="lista-beneficios">
                    <li>✓ Comparação de preços</li>
                    <li>✓ Preço final com frete</li>
                    <li>✓ Histórico de preços</li>
                    <li>✓ Análise avançada de segurança (IA)</li>
                    <li>✓ Alertas de preço ilimitados</li>
                    <li>✓ 10 cupons mensais</li>
                    <li>✓ Notificações no WhatsApp</li>
                    <li>✓ Índice de economia detalhado</li>
                    <li>✓ Assistente de IA para Orçamentos</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Assinar Premium", key="btn_premium_unico", use_container_width=True)

st.write("")
st.write("")
st.markdown("<h2 style='text-align: center; color: #ffffff; font-weight: 800; margin-top: 60px;'>Como o app funciona?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; margin-bottom: 30px;'>Simples, rápido e direto ao ponto em 3 passos:</p>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3, gap="large")
with col_f1:
    st.markdown("""<div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 10px;">1. Busque o produto</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Digite o que você quer comprar. Nossa tecnologia varre a internet inteira em segundos.</p></div>""", unsafe_allow_html=True)
with col_f2:
    st.markdown("""<div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 10px;">2. Compare e Proteja-se</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Mostramos o preço real com frete, histórico de valores e alertamos se a loja é segura contra golpes.</p></div>""", unsafe_allow_html=True)
with col_f3:
    st.markdown("""<div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 10px;">3. Economize de verdade</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Ative alertas de preço, receba cupons ou use nossa IA para planejar orçamentos completos.</p></div>""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #ffffff; font-weight: 800; margin-top: 60px;'>Por que você deveria usar?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; margin-bottom: 30px;'>Chega de perder tempo e dinheiro na internet:</p>", unsafe_allow_html=True)

col_v1, col_v2 = st.columns(2, gap="large")
with col_v1:
    st.markdown("""
        <div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 8px;">🛡️ Zero risco de cair em golpes</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Nossa análise inteligente identifica sinais suspeitos em lojas virtuais antes de você colocar o cartão de crédito.</p></div>
        <div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 8px;">💰 Economia real com frete incluso</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Não adianta o produto estar barato se o frete for absurdo. Calculamos o valor final para você não ter surpresas.</p></div>
    """, unsafe_allow_html=True)
with col_v2:
    st.markdown("""
        <div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 8px;">🤖 Inteligência para grandes compras</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Quer mobiliar a casa inteira? Nossa IA monta o carrinho ideal respeitando exatamente o seu orçamento máximo.</p></div>
        <div class="section-box"><h4 style="color: #00f0ff; font-weight: 700; margin-bottom: 8px;">🔔 Avisos no momento certo</h4><p style="font-size: 13px; color: #9ca3af; margin:0;">Defina quanto quer pagar e seja avisado por notificação ou WhatsApp assim que o preço cair para a sua meta.</p></div>
    """, unsafe_allow_html=True)
