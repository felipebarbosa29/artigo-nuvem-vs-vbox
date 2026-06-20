# Avaliação de Desempenho OpenMPI: VirtualBox vs. Nuvem AWS

Este repositório contém os artefatos, dados brutos, códigos-fonte modificados e scripts de geração de gráficos utilizados no artigo de análise de desempenho do middleware de comunicação OpenMPI, empregando a suíte OSU Micro-Benchmarks (OMB) v7.3.

## 📌 Objetivo do Estudo

O objetivo central é avaliar e comparar o impacto da infraestrutura subjacente na comunicação de processos MPI. Foram analisados dois cenários distintos:
1. **Ambiente Local (VirtualBox):** Foco na identificação de gargalos de CPU e Hypervisor durante operações coletivas (`osu_bcast`) em cenários de superlotação de processos (*oversubscription*).
2. **Ambiente em Nuvem (AWS):** Foco no impacto da distância geográfica física e do isolamento da pilha TCP/IP na latência ponto a ponto (`osu_latency`) utilizando túneis inter-regionais (VPC Peering).

---

## 📁 Estrutura de Diretórios

* `/virtualbox/`: Contém os dados brutos (`.txt`), scripts de plotagem em Python e gráficos (PNG/PDF) extraídos do cluster localizado na máquina hospedeira.
* `/aws_nuvem/`: Contém os dados consolidados, scripts e gráficos vetoriais comprovando o piso de latência física estabelecido pela distância entre os datacenters (aprox. 4.500 km).
* `/codigos_modificados/`: Código-fonte em C (`osu_latency.c` e `osu_bcast.c`) alterado com injeção de rotinas `gethostname()`. Essa modificação foi crucial para garantir a rastreabilidade topológica dos Ranks MPI durante a execução nos diferentes nós.

---

## 🛠️ Pré-requisitos de Infraestrutura

Para reproduzir os testes, os seguintes componentes base foram utilizados:
* **Ambiente Local:** HashiCorp Vagrant e Oracle VirtualBox.
* **Ambiente Nuvem:** Instâncias AWS EC2 (t2.micro) distribuídas geograficamente.
* **Dependências de Software (Ubuntu Linux):**
  * OpenMPI (`openmpi-bin`, `openmpi-common`, `libopenmpi-dev`)
  * Ferramentas de compilação C (`build-essential`)
  * Python 3 e Matplotlib (para a renderização dos gráficos de análise)

---

## 🚀 Execução: Ambiente Local (VirtualBox)

O cluster local é composto por 4 máquinas virtuais (1 vCPU, 512MB RAM) interligadas por uma rede privada isolada (Host-Only na sub-rede `192.168.56.0/24`).

### Comando de Execução (Broadcast)
Para forçar o cenário de *oversubscription* e analisar a degradação de desempenho do hypervisor, escalamos a operação de Broadcast em múltiplos processos. O comando abaixo exemplifica a execução distribuída forçando 8 Ranks concorrentes:

```bash
mpirun --hostfile hostfile --mca btl_tcp_if_include 192.168.56.0/24 --map-by node --oversubscribe -np 8 ./osu_bcast -i 100 -x 10
```
Detalhe Técnico: Os parâmetros -i 100 -x 10 foram injetados no benchmark para limitar a execução a 10 iterações de aquecimento (warmup) e 100 iterações de medição real, otimizando o tempo total do teste sem perder a estabilidade estatística.

☁️ Execução: Ambiente em Nuvem (AWS)
O experimento em nuvem consiste na comunicação entre duas instâncias isoladas em regiões distintas, conectadas exclusivamente via AWS VPC Peering:

Nó Master (Virgínia - us-east-1): VPC 172.31.0.0/16

Nó Worker (Oregon - us-west-2): VPC 10.0.0.0/16

Comando de Execução (Latência Inter-Regional)
Devido às rígidas barreiras de rede da nuvem pública (ausência de InfiniBand nativo e bloqueios de broadcast), foi necessário impor regras estritas ao framework MCA do OpenMPI para forçar a rota TCP transcontinental:

```Bash
mpirun --hostfile hostfile_aws \
  --mca pml ob1 \
  --mca btl tcp,self \
  --mca btl_tcp_if_include 172.31.0.0/16,10.0.0.0/16 \
  --mca btl_tcp_disable_family IPv6 \
  --map-by node -np 2 ./osu_latency -i 100 -x 10
```
A flag --mca btl_tcp_if_include foi necessário na execução do teste. Ela obriga o plano de dados do MPI a blindar o tráfego nas sub-redes das VPCs emparelhadas, impedindo que o tráfego tente ir para a internet pública ou falhe na tentativa de usar IPv6.

📈 Reprodutibilidade Gráfica
Para garantir a reprodutibilidade e transparência na geração dos resultados presentes no artigo, os gráficos vetoriais podem ser recriados localmente processando os dados brutos através dos scripts Python disponibilizados.

Com o Matplotlib instalado, execute a partir da raiz do repositório:

```Bash
# Renderizar resultados do cluster local
python3 virtualbox/scripts/plotar_graficos_wsl.py
```

# Renderizar resultados do cluster em nuvem
python3 aws_nuvem/scripts/plotar_grafico_aws.py




