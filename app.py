import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Comparador de Preços Inteligente",
    page_icon="💎",
    layout="centered"
)

# Estilização CSS personalizada (Design limpo, escuro e tooltips)
st.markdown("""
    <style>
        .stApp {
            background-color: #121214;
            color: #f4f4f5;
        }
        .plan-card {
            background-color: #18181b;
            border: 1px solid #27272a;
            border-radius: 16px;
            padding: 24px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            border-bottom: 1px dotted #71717a;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 220px;
            background-color: #27272a;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 6px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -110px;
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 11px;
            border: 1px solid #3f3f46;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        .section-box {
            background-color: #18181b;
            border: 1px solid #27272a;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("<h1 style='text-align: center; color: white;'>Escolha seu plano</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a1a1aa;'>Selecione o melhor plano para você e economize com segurança.</p>", unsafe_allow_html=True)

# Seletor de período (Mensal / Anual)
col_pad1, col_center, col_pad2 = st.columns([1, 2, 1])
with col_center:
    tipo_cobranca = st.radio(
        "Período de cobrança",
        ["Mensal", "Anual (Economize)"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.write("") 

# Colunas dos 3 planos
col1, col2, col3 = st.columns(3)

# --- PLANO BASIC ---
with col1:
    st.markdown("""
        <div class="plan-card">
            <div>
                <h3 style="color: #a78bfa; margin-top:0;">Basic</h3>
    """, unsafe_allow_html=True)
    
    if tipo_cobranca == "Mensal":
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 9,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
        st.markdown("<span style='background: rgba(124,58,237,0.2); color:#c084fc; padding: 3px 8px; border-radius: 4px; font-size:11px; font-weight:600;'>7 dias grátis para testar</span>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 6,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
        st.markdown("<span style='color:#71717a; font-size:11px;'>R$ 83,88 cobrado anualmente</span>", unsafe_allow_html=True)

    st.markdown("""
                <hr style="border-color: #27272a; margin: 15px 0;">
                <ul style="list-style: none; padding: 0; font-size: 13px; color: #d4d4d8; display: flex; flex-direction: column; gap: 10px;">
                    <li>✓ <span class="tooltip">Comparação de preços<span class="tooltiptext">Compare o preço do produto em diferentes lojas.</span></span></li>
                    <li>✓ <span class="tooltip">Preço final com frete<span class="tooltiptext">Veja quanto realmente vai pagar, incluindo o frete.</span></span></li>
                    <li>✓ <span class="tooltip">Histórico de preços<span class="tooltiptext">Veja a evolução do preço e descubra se está barato.</span></span></li>
                    <li>✓ <span class="tooltip">Análise básica de segurança<span class="tooltiptext">Identificamos sinais que podem indicar riscos na loja.</span></span></li>
                    <li>✓ <span class="tooltip">3 alertas de preço<span class="tooltiptext">Defina um valor e avisaremos quando o produto chegar nele.</span></span></li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Iniciar 7 dias grátis", key="btn_basic", use_container_width=True):
        st.success("Plano Basic selecionado!")

# --- PLANO PLUS ---
with col2:
    st.markdown("""
        <div class="plan-card">
            <div>
                <h3 style="color: #fb7185; margin-top:0;">Plus</h3>
    """, unsafe_allow_html=True)
    
    if tipo_cobranca == "Mensal":
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 19,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 15,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
        st.markdown("<span style='color:#71717a; font-size:11px;'>R$ 191,88 cobrado anualmente</span>", unsafe_allow_html=True)

    st.markdown("""
                <hr style="border-color: #27272a; margin: 15px 0;">
                <ul style="list-style: none; padding: 0; font-size: 13px; color: #d4d4d8; display: flex; flex-direction: column; gap: 10px;">
                    <li>✓ <span class="tooltip">Comparação de preços<span class="tooltiptext">Compare o preço do produto em diferentes lojas.</span></span></li>
                    <li>✓ <span class="tooltip">Preço final com frete<span class="tooltiptext">Veja quanto realmente vai pagar, incluindo o frete.</span></span></li>
                    <li>✓ <span class="tooltip">Histórico de preços<span class="tooltiptext">Veja a evolução do preço e descubra se está barato.</span></span></li>
                    <li>✓ <span class="tooltip">Análise básica de segurança<span class="tooltiptext">Identificamos sinais que podem indicar riscos na loja.</span></span></li>
                    <li>✓ <span class="tooltip">10 alertas de preço<span class="tooltiptext">Monitore até 10 produtos e avisa quando o preço cair.</span></span></li>
                    <li>✓ <span class="tooltip">2 cupons semanais<span class="tooltiptext">Resgate cupons exclusivos toda semana para economizar mais.</span></span></li>
                    <li>✓ <span class="tooltip">Notificação de queda de preços<span class="tooltiptext">Receba avisos instantâneos quando os produtos favoritos caírem.</span></span></li>
                    <li>✓ <span class="tooltip">Índice de economia<span class="tooltiptext">Acompanhe em tempo real quanto dinheiro você já poupou no site.</span></span></li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Assinar Plus", key="btn_plus", use_container_width=True):
        st.success("Plano Plus selecionado!")

# --- PLANO PREMIUM ---
with col3:
    st.markdown("""
        <div class="plan-card" style="border-color: #7c3aed;">
            <div>
                <h3 style="color: #fcd34d; margin-top:0;">Premium</h3>
    """, unsafe_allow_html=True)
    
    if tipo_cobranca == "Mensal":
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 29,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='font-size: 24px; color: white;'>R$ 24,99 <span style='font-size:13px; color:#a1a1aa;'>/ mês</span></h2>", unsafe_allow_html=True)
        st.markdown("<span style='color:#71717a; font-size:11px;'>R$ 299,88 cobrado anualmente</span>", unsafe_allow_html=True)

    st.markdown("""
                <hr style="border-color: #27272a; margin: 15px 0;">
                <ul style="list-style: none; padding: 0; font-size: 13px; color: #d4d4d8; display: flex; flex-direction: column; gap: 10px;">
                    <li>✓ <span class="tooltip">Comparação de preços<span class="tooltiptext">Compare o preço do produto em diferentes lojas.</span></span></li>
                    <li>✓ <span class="tooltip">Preço final com frete<span class="tooltiptext">Veja quanto realmente vai pagar, incluindo o frete.</span></span></li>
                    <li>✓ <span class="tooltip">Histórico de preços<span class="tooltiptext">Veja a evolução do preço e descubra se está barato.</span></span></li>
                    <li>✓ <span class="tooltip">Análise avançada de segurança (IA)<span class="tooltiptext">Blindagem total contra golpes com verificação profunda de lojas.</span></span></li>
                    <li>✓ <span class="tooltip">Alertas de preço ilimitados<span class="tooltiptext">Monitore quantos produtos quiser sem nenhuma restrição.</span></span></li>
                    <li>✓ <span class="tooltip">10 cupons mensais<span class="tooltiptext">Acesse cupons exclusivos todos os meses para maximizar sua economia.</span></span></li>
                    <li>✓ <span class="tooltip">Notificações no WhatsApp<span class="tooltiptext">Receba avisos instantâneos e alertas relâmpago direto no seu celular.</span></span></li>
                    <li>✓ <span class="tooltip">Índice de economia detalhado<span class="tooltiptext">Acompanhe em tempo real quanto dinheiro você já poupou na plataforma.</span></span></li>
                    <li>✓ <span class="tooltip">Assistente de IA para Orçamentos<span class="tooltiptext">Planeje compras complexas (ex: mobiliar o quarto) respeitando seu limite de preço.</span></span></li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Assinar Premium", key="btn_premium", use_container_width=True):
        st.success("Plano Premium selecionado!")

# --- SEÇÃO: COMO O APP FUNCIONA ---
st.write("")
st.write("")
st.markdown("<h2 style='text-align: center; color: white; margin-top: 40px;'>Como o app funciona?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a1a1aa; margin-bottom: 30px;'>Simples, rápido e direto ao ponto em 3 passos:</p>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown("""
        <div class="section-box">
            <h4 style="color: #a78bfa;">1. Busque o produto</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Digite o que você quer comprar. Nossa tecnologia varre a internet inteira em segundos.</p>
        </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <div class="section-box">
            <h4 style="color: #fb7185;">2. Compare e Proteja-se</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Mostramos o preço real com frete, histórico de valores e alertamos se a loja é segura contra golpes.</p>
        </div>
    """, unsafe_allow_html=True)

with col_f3:
    st.markdown("""
        <div class="section-box">
            <h4 style="color: #fcd34d;">3. Economize de verdade</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Ative alertas de preço, receba cupons ou use nossa IA para planejar orçamentos completos.</p>
        </div>
    """, unsafe_allow_html=True)

# --- SEÇÃO: POR QUE VOCÊ DEVERIA USAR ---
st.markdown("<h2 style='text-align: center; color: white; margin-top: 40px;'>Por que você deveria usar?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a1a1aa; margin-bottom: 30px;'>Chega de perder tempo e dinheiro na internet:</p>", unsafe_allow_html=True)

col_v1, col_v2 = st.columns(2)
with col_v1:
    st.markdown("""
        <div class="section-box">
            <h4 style="color: #38bdf8;">🛡️ Zero risco de cair em golpes</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Nossa análise inteligente identifica sinais suspeitos em lojas virtuais antes de você colocar o cartão de crédito.</p>
        </div>
        <div class="section-box">
            <h4 style="color: #38bdf8;">💰 Economia real com frete incluso</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Não adianta o produto estar barato se o frete for absurdo. Calculamos o valor final para você não ter surpresas.</p>
        </div>
    """, unsafe_allow_html=True)

with col_v2:
    st.markdown("""
        <div class="section-box">
            <h4 style="color: #38bdf8;">🤖 Inteligência para grandes compras</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Quer mobiliar a casa inteira? Nossa IA monta o carrinho ideal respeitando exatamente o seu orçamento máximo.</p>
        </div>
        <div class="section-box">
            <h4 style="color: #38bdf8;">🔔 Avisos no momento certo</h4>
            <p style="font-size: 13px; color: #d4d4d8;">Defina quanto quer pagar e seja avisado por notificação ou WhatsApp assim que o preço cair para a sua meta.</p>
        </div>
    """, unsafe_allow_html=True)
