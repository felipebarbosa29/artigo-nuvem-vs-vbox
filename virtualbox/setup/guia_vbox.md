# Configuração Manual: VirtualBox

Este documento descreve os passos para a montagem manual do cluster, caso a automação via Vagrant não seja utilizada.

## 1. Criação das Máquinas Virtuais
1. Criar uma VM base com Ubuntu 22.04 LTS.
2. Configurar 1 vCPU e 1024 MB de RAM.
3. Adicionar dois adaptadores de rede:
   *   **Adaptador 1:** NAT (para acesso à internet).
   *   **Adaptador 2:** Placa de rede exclusiva de hospedeiro (Host-only) para o tráfego MPI.

## 2. Tratamento de Conflitos de Clonagem
Ao clonar uma VM manualmente, é necessário resetar o `machine-id` para evitar que o servidor DHCP atribua o mesmo IP a máquinas diferentes:

```bash
sudo rm /etc/machine-id /var/lib/dbus/machine-id
sudo systemd-machine-id-setup
sudo reboot
```

## 3. Configuração de Rede Estática (Netplan)
Edite o arquivo `/etc/netplan/50-cloud-init.yaml` em cada nó para garantir que os IPs não mudem entre reboots:

```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      dhcp4: false
      addresses: [192.168.56.101/24]
```
*Aplique com: `sudo netplan apply`*