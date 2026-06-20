# Automação de Infraestrutura: Vagrant (IaC)

Este guia detalha a utilização do Vagrant para a criação automatizada e reprodutível do cluster de computação distribuída.

## 1. Arquitetura do Vagrantfile
O script de automação foi desenhado para instanciar 4 nós (node1 a node4) com as seguintes restrições de hardware para conformidade com máquinas de 8 GB de RAM:

*   **SO:** Ubuntu 22.04 LTS.
*   **Memória:** 1024 MB por nó.
*   **CPU:** 1 vCPU por nó.
*   **Rede:** Interface `private_network` com IPs estáticos (192.168.56.101-104).

## 2. Procedimento de Deploy
Com o Vagrant e o VirtualBox instalados no hospedeiro, execute a partir da raiz do projeto:

```bash
vagrant up
```

## 3. Otimizações
*   **Linked Clones:** O Vagrantfile utiliza `v.linked_clone = true`. Isso faz com que as VMs compartilhem o mesmo disco base (master image), reduzindo drasticamente o tempo de criação e o espaço em disco.
*   **Provisionamento Automático:** O script já realiza o `apt install` do OpenMPI e a configuração das chaves SSH internas durante o boot inicial.

## 4. Comandos Úteis
*   Acessar o nó mestre: `vagrant ssh node1`
*   Desligar o cluster: `vagrant halt`
*   Destruir e limpar o ambiente: `vagrant destroy -f`