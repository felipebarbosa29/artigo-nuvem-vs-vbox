import matplotlib.pyplot as plt

# 1. Dados Filtrados: Apenas os 6 pontos de referência (para manter o gráfico limpo)
sizes = [1, 16, 256, 4096, 65536, 1048576]
labels_x = ['1 B', '16 B', '256 B', '4 KB', '64 KB', '1 MB']

# Valores extraídos do Print 1 (Mesma máquina local - Norte da Virgínia)
lat_local = [1.20, 0.96, 0.97, 3.47, 10.93, 202.66]

# Valores extraídos do Print 2 (Inter-regiões: Virgínia -> Oregon)
lat_dist = [28659.51, 28286.30, 28287.12, 28315.99, 85005.58, 87179.18]

# 2. Configuração da Figura (Estética Limpa e Acadêmica)
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Cores idênticas ao modelo enviado (Paleta Seaborn)
cor_azul = '#4C72B0'
cor_laranja = '#DD8452'

# 3. Plotando as linhas com marcadores específicos
ax.plot(sizes, lat_local, marker='o', markersize=8, linewidth=2.5, color=cor_azul, label='Linha de Base Local (N. Virgínia)')
ax.plot(sizes, lat_dist, marker='s', markersize=8, linewidth=2.5, color=cor_laranja, label='Rede Distribuída (Virgínia $\\rightarrow$ Oregon)')

# 4. Escalas Logarítmicas
ax.set_xscale('log', base=2)
ax.set_yscale('log', base=10)

# 5. Configuração do Eixo X 
ax.set_xticks(sizes)
ax.set_xticklabels(labels_x, rotation=45, ha='right', fontsize=12)

# Configuração do Eixo Y
ax.tick_params(axis='y', labelsize=12)

# 6. Títulos e Textos Traduzidos
ax.set_title('OSU Micro-Benchmarks: LATÊNCIA (Ponto-a-Ponto)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Tamanho da Mensagem', fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel('Latência (µs)', fontsize=14, fontweight='bold', labelpad=10)

# 7. Grid (Grade) tracejada em cinza claro
ax.grid(True, which='major', linestyle='--', color='#d3d3d3', linewidth=1.2)

# 8. Legenda centralizada à esquerda (espaço vazio) e com fonte reduzida
legend = ax.legend(fontsize=11, loc='center left', frameon=True)
legend.get_frame().set_edgecolor('#cccccc')
legend.get_frame().set_linewidth(1.5)

# Borda do gráfico cinza claro
for spine in ax.spines.values():
    spine.set_edgecolor('#cccccc')
    spine.set_linewidth(1.5)

plt.tight_layout()

# 9. Salvando nos formatos solicitados
plt.savefig('grafico_latencia_aws.png', format='png', dpi=300, bbox_inches='tight')
plt.savefig('grafico_latencia_aws.pdf', format='pdf', bbox_inches='tight')

print("Gráficos gerados com sucesso: 'grafico_latencia_aws.png' e 'grafico_latencia_aws.pdf'")
