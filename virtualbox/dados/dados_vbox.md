## Resultados dos Benchmarks: Ambiente VirtualBox (Local)

As secções seguintes detalham os resultados dos testes *OSU Micro-Benchmarks* executados num ambiente local virtualizado utilizando o VirtualBox. A topologia do cluster é composta por 4 Máquinas Virtuais (`server1`, `server2`, `mpiserver3` e `mpiserver4`).

### 1. Latência Ponto-a-Ponto (osu_latency)

O teste de latência ponto-a-ponto foi executado com 2 processos (`NP=2`), estabelecendo comunicação direta entre a VM `server1` (Rank 0) e a VM `server2` (Rank 1).

| Tamanho (Bytes) | Latência (µs) |
| :--- | :--- |
| 1 | 364,80 |
| 2 | 455,66 |
| 4 | 347,49 |
| 8 | 425,43 |
| 16 | 450,60 |
| 32 | 759,04 |
| 64 | 814,48 |
| 128 | 491,57 |
| 256 | 393,10 |
| 512 | 356,40 |
| 1024 | 375,66 |
| 2048 | 589,50 |
| 4096 | 528,95 |
| 8192 | 774,76 |
| 16384 | 1189,39 |
| 32768 | 798,07 |
| 65536 | 1908,21 |
| 131072 | 1786,54 |
| 262144 | 1908,35 |
| 524288 | 2655,49 |
| 1048576 | 5416,08 |
| 2097152 | 9493,63 |
| 4194304 | 15398,73 |

---

### 2. Comunicação Coletiva: Broadcast (osu_bcast)

 O teste de *Broadcast* enviou dados de um nó raiz(`server1`) para todos os nós participantes. O processamento foi distribuído pelas 4 VMs em três cenários de carga distintos: **NP=4** (1 processo por VM), **NP=8** (2 processos por VM) e **NP=16** (4 processos por VM).

| Tamanho (Bytes) | Latência NP=4 (µs) | Latência NP=8 (µs) | Latência NP=16 (µs) |
| :--- | :--- | :--- | :--- |
| 1 | 1268,70 | 17225,31 | 3189,71 |
| 2 | 1349,73 | 16219,13 | 3447,71 |
| 4 | 1325,34 | 16362,78 | 3117,64 |
| 8 | 1177,12 | 19633,28 | 3240,86 |
| 16 | 1157,63 | 19616,45 | 3228,87 |
| 32 | 1174,23 | 23972,89 | 3533,87 |
| 64 | 1188,85 | 16920,22 | 3205,37 |
| 128 | 1348,95 | 15652,41 | 3315,00 |
| 256 | 1198,95 | 16357,41 | 3211,98 |
| 512 | 1356,95 | 19591,88 | 2991,66 |
| 1024 | 1331,32 | 15481,06 | 3111,73 |
| 2048 | 1304,05 | 15839,09 | 3354,75 |
| 4096 | 1508,51 | 19259,83 | 3239,29 |
| 8192 | 1247,12 | 18923,40 | 3245,21 |
| 16384 | 1601,09 | 20612,83 | 3656,84 |
| 32768 | 1516,13 | 14142,77 | 3819,32 |
| 65536 | 3876,52 | 25341,15 | 9270,27 |
| 131072 | 4809,51 | 29762,06 | 12846,59 |
| 262144 | 6607,53 | 29356,32 | 14469,76 |
| 524288 | 9271,52 | 36844,55 | 21803,29 |
| 1048576 | 20021,94 | 43703,31 | 48089,79 |

**Análise Técnica:** A consolidação dos resultados de *Broadcast* revela o aumento do total de tempo do VirtualBox à medida que o número de processos sofre um incremento. Destaca-se a latência no cenário NP=8 com pequenos pacotes, que apresentou um desvio acentuado em comparação com a execução nativa ou em ambiente *cloud* (AWS). 