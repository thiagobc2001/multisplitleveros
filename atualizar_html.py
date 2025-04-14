import pandas as pd
import json
import re

# Caminhos corrigidos
caminho_html = r'C:\Users\thiago.camargo\Python\teste\simulador.html'
caminho_excel = r'C:\Users\thiago.camargo\Desktop\condensadoras_multisplit_exemplo.xlsx'

# Lê a planilha Excel
df = pd.read_excel(caminho_excel)

# Formata os dados
evaporadoras = df[['TipoEvaporadora', 'BTUs']].drop_duplicates().rename(columns={
    'TipoEvaporadora': 'tipo',
    'BTUs': 'btus'
}).to_dict(orient='records')

condensadoras = df[['ModeloCondensadora', 'CapMin', 'CapMax', 'Marca', 'Código']].rename(columns={
    'ModeloCondensadora': 'modelo',
    'CapMin': 'min',
    'CapMax': 'max',
    'Marca': 'marca',
    'Código': 'codigo'
}).to_dict(orient='records')

# Monta o JSON no formato do HTML
dados_json = {
    'evaporadoras': evaporadoras,
    'condensadoras': condensadoras
}
json_str = json.dumps(dados_json, indent=2, ensure_ascii=False)

# Lê o HTML original
with open(caminho_html, 'r', encoding='utf-8') as f:
    html = f.read()

# Substitui a parte do dadosJSON no HTML
html_atualizado = re.sub(
    r'const dadosJSON = \{.*?\};',
    f'const dadosJSON = {json_str};',
    html,
    flags=re.DOTALL
)

# Salva o HTML modificado
with open(caminho_html, 'w', encoding='utf-8') as f:
    f.write(html_atualizado)

print('✅ HTML atualizado com sucesso!')
