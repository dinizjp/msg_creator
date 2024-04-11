import streamlit as st

# Título do aplicativo
st.title('Gerador de Mensagens para Sorteios de WhatsApp')

# Entradas do usuário
numero_sorteio = st.text_input('Número do Sorteio')
nome_kit = st.text_input('Nome do Kit')
preco_cotinha = st.text_input('Preço por Cotinha')
link_sorteio = st.text_input('Link do Sorteio')
kit_opcoes = st.checkbox('Kit com Opções de Escolha')

# Opções de emojis
opcoes_emojis_normal = {
    'Sorte': '🚀🍀',
    'Carne': '🥩🔥',
    'Cerveja': '🍺🍖',
    'Top': '🔝😱',
    'Benção': '💥🙏🏼'
}

opcoes_emojis_opcao = {
    'Sorte': '🎲💥',
    'Carne': '🍖🚀',
    'Cerveja': '🍻🔥',
    'Top': '✨🙏',
    'Benção': '💰👀'
}

# Seleção do conjunto de emojis
if kit_opcoes:
    emoji_escolhido = st.selectbox('Escolha o conjunto de emojis para o kit com opção:', list(opcoes_emojis_opcao.keys()))
else:
    emoji_escolhido = st.selectbox('Escolha o conjunto de emojis para o kit normal:', list(opcoes_emojis_normal.keys()))

# Modelo de mensagem selecionado automaticamente com base na escolha de opções
def gerar_mensagem(numero_sorteio, nome_kit, preco_cotinha, link_sorteio, kit_opcoes, emoji):
    emoji_selecionado = opcoes_emojis_opcao[emoji] if kit_opcoes else opcoes_emojis_normal[emoji]
    mensagem_comum = "LINK 👇🏻🔗💰 (SE NÃO TIVER EM AZUL PRA CLICAR NO LINK, SALVE NOSSO CONTATO!!!!)📌\n"
    if kit_opcoes:
        mensagem = f"{emoji_selecionado}SORTEIO #{numero_sorteio} - {nome_kit} {emoji_selecionado}\n\n* GANHADOR IRÁ ESCOLHER UM DOS KITS ACIMA 👆🏼👆🏼\n\n💸 APENAS R$ {preco_cotinha} A COTINHA {emoji_selecionado}\n\n{mensagem_comum}{link_sorteio}"
    else:
        mensagem = f"{emoji_selecionado} SORTEIO {numero_sorteio}- {nome_kit} {emoji_selecionado}\n\n💸 SOMENTE R$ {preco_cotinha} A COTINHA\n\n{mensagem_comum}{link_sorteio}"
    return mensagem

# Botão para gerar mensagem
if st.button('Gerar Mensagem'):
    mensagem_gerada = gerar_mensagem(numero_sorteio, nome_kit, preco_cotinha, link_sorteio, kit_opcoes, emoji_escolhido)
    st.text_area("Mensagem Gerada:", mensagem_gerada, height=250)


# Função para converter números em emojis
def numero_para_emoji(numero):
    mapa_numeros = {
        '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
        '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
    }
    return ''.join(mapa_numeros[digito] for digito in str(numero))

# Opções de emojis para mensagem de reforço
opcoes_emojis_reforco = {
    'Alerta': '🚨',
    'Atenção': '⚠️',
    'Destaque': '✨',
    'Urgente': '❗',
    'Importante': '🔔'
}

# Entradas do usuário para a mensagem de reforço
st.header('Mensagem de Reforço para Sorteio')
cotas_restantes = st.text_input('Número de Cotinhas Restantes')
preco_cotinha_reforco = st.text_input('Preço por Cotinha para Reforço')
link_sorteio_reforco = st.text_input('Link do Sorteio para Reforço')
estilo_emoji_reforco = st.selectbox('Escolha o estilo de emoji para a mensagem de reforço:', list(opcoes_emojis_reforco.keys()))

# Função para gerar mensagem de reforço
def gerar_mensagem_reforco(cotas, preco, link, estilo_emoji):
    emoji_selecionado = opcoes_emojis_reforco[estilo_emoji]
    cotas_emoji = numero_para_emoji(cotas)
    mensagem = f"{emoji_selecionado}👆🏼 *Últimas {cotas_emoji} cotinhas livres!* 🔝🔝\n\n💸 *APENAS R$ {preco} A COTINHA* 💰💰\n\n*LINK DO SORTEIO* 👇🏻(SE NÃO TIVER EM AZUL PRA CLICAR NO LINK, SALVE NOSSO CONTATO!!!!)📌 \n {link}"
    return mensagem

# Botão para gerar mensagem de reforço
if st.button('Gerar Mensagem de Reforço'):
    mensagem_reforco_gerada = gerar_mensagem_reforco(cotas_restantes, preco_cotinha_reforco, link_sorteio_reforco, estilo_emoji_reforco)
    st.text_area("Mensagem de Reforço Gerada:", mensagem_reforco_gerada, height=250)