# Laboratório de Computação Distribuída: VirtualBox e AWS

Este repositório contém os artefatos técnicos, scripts de automação e dados experimentais utilizados no estudo de viabilidade de laboratórios de computação distribuída para a UNIVESP. O projeto foca na acessibilidade, permitindo que alunos repliquem clusters de alto desempenho em hardware modesto ou na nuvem.

> **Nota:** Este estudo integra um projeto de Iniciação Científica (IC) na UNIVESP para avaliar simuladores e ferramentas para o aprendizado de sistemas distribuídos.

---

## 📌 Visão Geral do Projeto

O trabalho está estruturado em dois pilares independentes, conforme as exigências pedagógicas:

1.  **Ambiente Local (VirtualBox):** Focado na análise de comunicações coletivas (**Broadcast**) em um cluster de 4 nós.
2.  **Ambiente em Nuvem (AWS):** Focado na medição de **Latência Ponto-a-Ponto** entre regiões geograficamente distantes (Virgínia do Norte e Oregon).

---

## 📁 Estrutura do Repositório

*   `/virtualbox/`: Scripts de automação (Vagrant), guias de instalação manual e dados brutos do teste de Broadcast.
*   `/aws_nuvem/`: Configurações de redes virtuais privadas e dados de latência inter-regional.
*   `/codigos_modificados/`: Código-fonte C dos benchmarks OSU com a inclusão da rotina `gethostname()` para identificação precisa dos nós.

---

## 🛠️ Infraestrutura e Configuração

### 1. Cluster Local (VirtualBox + Vagrant)

*   **Configuração:** 4 Máquinas Virtuais (Ubuntu 22.04).
*   **Recursos:** 1 vCPU e 1 GB de RAM por nó.
*   **Cálculo de Memória (Viabilidade em 8 GB):**
    Para garantir a execução sem travamentos em computadores de 8 GB de RAM, seguimos o orçamento:
    - **Windows 10/11:** 2,0 GB
    - **4 VMs (1 GB cada):** 4,0 GB
    - **Hipervisor (VBox) + Processos:** 0,5 GB
    - **Total Estimado:** **6,5 GB** (Margem livre de 1,5 GB).
*   **Automação:** O uso do Vagrant garante que os limites de hardware sejam respeitados.

### 2. Nuvem AWS

*   **Instâncias:** 2 instâncias `t2.micro` (Free Tier).
*   **Rede:** Conectividade via **redes virtuais privadas** interconectadas entre `us-east-1` (Virgínia do Norte) e `us-west-2` (Oregon), cobrindo ~4.500 km.

---

## 🚀 Como Executar os Experimentos

### Teste de Broadcast (VirtualBox)
Para validar a comunicação coletiva no cluster local:
```bash
mpirun --hostfile hostfile --mca btl_tcp_if_include 192.168.56.0/24 --map-by node -np 8 ./osu_bcast -i 100 -x 10
```

### Teste de Latência (AWS)
Para medir a latência transcontinental isolando o tráfego nas redes privadas:
```bash
mpirun --hostfile hostfile_aws \
  --mca pml ob1 \
  --mca btl tcp,self \
  --mca btl_tcp_if_include 172.31.0.0/16,10.0.0.0/16 \
  --map-by node -np 2 ./osu_latency -i 100 -x 10
```

---

## 📈 Resultados
Os resultados detalhados, incluindo os gráficos de latência inter-regional e desempenho de broadcast, estão disponíveis na pasta `/codigos_modificados/graficos/` e no artigo submetido ao ERAD-SP 2026.

---

## 🎓 Créditos
Desenvolvido por **Felipe Barbosa da Silva** sob orientação do **Prof. Dr. Mauricio G. Palma** como parte das atividades de Iniciação Científica da UNIVESP.