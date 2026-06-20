# Resultados Experimentais: VirtualBox (Local)

Este documento consolida as medições obtidas com a suíte OSU Micro-Benchmarks v7.3 no cluster local virtualizado.

## 1. Latência Ponto-a-Ponto (osu_latency)
**Configuração:** 2 processos (NP=2), mapeados em nós distintos (`server1` e `server2`).

| Tamanho (Bytes) | Latência (µs) |
| :--- | :--- |
| 1 | 364,80 |
| 16 | 450,60 |
| 256 | 393,10 |
| 1024 | 375,66 |
| 4096 | 528,95 |
| 65536 | 1908,21 |
| 1048576 | 5416,08 |
| 4194304 | 15398,73 |

**Observação:** A latência média para pacotes pequenos (~360 µs)

---

## 2. Comunicação Coletiva: Broadcast (osu_bcast)
**Configuração:** Root no `server1`. Escalonamento em 4, 8 e 16 processos distribuídos nos 4 nós.

| Tamanho (Bytes) | NP=4 (µs) | NP=8 (µs) | NP=16 (µs) |
| :--- | :--- | :--- | :--- |
| 1 | 1268,70 | 17225,31 | 3189,71 |
| 16 | 1157,63 | 19616,45 | 3228,87 |
| 256 | 1198,95 | 16357,41 | 3211,98 |
| 1024 | 1331,32 | 15481,06 | 3111,73 |
| 4096 | 1508,51 | 19259,83 | 3239,29 |
| 65536 | 3876,52 | 25341,15 | 9270,27 |
| 1048576 | 20021,94 | 43703,31 | 48089,79 |

**Análise de Sobrecarga:**
*   **Cenário NP=4:** Desempenho mais estável devido ao mapeamento de 1 processo por vCPU física/virtual disponível por nó.
*   **Cenário NP=8 e NP=16:** 
