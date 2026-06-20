# Desempenho OpenMPI: VirtualBox vs. Nuvem AWS

Artefatos, dados brutos, códigos modificados e scripts de plotagem utilizados no artigo sobre o uso de VirtualBox e Nuvem para Práticas de Computação Distribuída (suíte OSU Micro-Benchmarks v7.3).

## 📌 Objetivo

O ensino de computação distribuída esbarra no custo e na complexidade de manter clusters físicos dedicados. Este trabalho avalia o uso de Máquinas Virtuais locais e Nuvem Pública como alternativas viáveis, focando em três pontos:
1. Configuração e viabilidade das ferramentas.
2. Exemplos práticos de experimentos.
3. Requisitos de sistema necessários.

---

## 📁 Estrutura do Repositório

* `/virtualbox/`: Dados brutos (`.txt`), scripts Python e gráficos (PNG/PDF) do cluster local.
* `/aws_nuvem/`: Dados, scripts e gráficos vetoriais do teste inter-regional (distância de ~4.500 km).
* `/codigos_modificados/`: Código-fonte em C (`osu_latency.c` e `osu_bcast.c`) com a injeção da rotina `gethostname()` para rastreamento dos Ranks MPI entre os nós.

---

## 🛠️ Pré-requisitos e Ambiente

* **Ambiente Local:** Cluster com 4 VMs gerenciadas via Vagrant e Oracle VirtualBox (1 vCPU, 512MB RAM por nó) em rede Host-Only (`192.168.56.0/24`).
* **Ambiente Nuvem:** 2 instâncias AWS EC2 (t2.micro) conectadas por VPC Peering entre as regiões de Virginia (`us-east-1` / `172.31.0.0/16`) e Oregon (`us-west-2` / `10.0.0.0/16`).
* **Software Base (Ubuntu):** OpenMPI (`libopenmpi-dev`), `build-essential`, Python 3 e Matplotlib.

---

## 🚀 Como Executar os Testes

### 1. Cluster Local (VirtualBox) - Teste de Broadcast
Cenário de *oversubscription* (8 processos concorrentes em 4 nós) para avaliar o impacto do hypervisor em operações coletivas:

```bash
mpirun --hostfile hostfile --mca btl_tcp_if_include 192.168.56.0/24 --map-by node --oversubscribe -np 8 ./osu_bcast -i 100 -x 10
```

***Nota: As flags -i 100 -x 10 definem 10 iterações de warmup e 100 de medição para garantir estabilidade estatística sem estender o tempo de execução.

## 2. Nuvem AWS - Teste de Latência Inter-Regional
Medição de latência ponto a ponto através do túnel de VPC Peering:

```bash
mpirun --hostfile hostfile_aws \
  --mca pml ob1 \
  --mca btl tcp,self \
  --mca btl_tcp_if_include 172.31.0.0/16,10.0.0.0/16 \
  --mca btl_tcp_disable_family IPv6 \
  --map-by node -np 2 ./osu_latency -i 100 -x 10
```
Nota: A flag --mca btl_tcp_if_include isola o tráfego do MPI dentro das sub-redes das VPCs emparelhadas, impedindo falhas por rotas IPv6 ou tentativas de saída para a internet pública.

📈 Geração dos Gráficos
Para processar os logs brutos e gerar os gráficos vetoriais do artigo, execute a partir da raiz do repositório:

```bash
# Gráficos do ambiente local (VirtualBox)
python3 virtualbox/scripts/plotar_graficos_wsl.py

# Gráficos do ambiente em nuvem (AWS)
python3 aws_nuvem/scripts/plotar_graph_aws.py
```