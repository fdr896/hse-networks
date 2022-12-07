## Лабораторная работа 1

### Топология сети
![](images/network_view.png)

### VPC могут посылать друг другу ping
![](images/ping.png)

### Настроены vlan 10 и vlan 20
* VPC-1 находится во vlan10, его ip адрес 10.0.10.2 с маской 255.255.255.0
![](images/R1_client_vlan10.png)
* VPC-2 находится во vlan20, его ip адрес 10.0.20.2 с маской 255.255.255.0
![](images/R2_client_vlan20.png)
* У коммутаторов R1, R2, R3 настроены trunk порты
![](images/R1_interfaces.png)
![](images/R2_interfaces.png)
![](images/R3_interfaces.png)

### Настроен STP
* Коммутатор R3 является корнем vlan 10 и vlan 20
![](images/R3_stp_vlan10.png)
![](images/R3_stp_vlan20.png)
* Между коммутаторами R1 и R2 заблокирован линк (в обоих vlan)
  - vlan 10
  ![](images/R1_stp_vlan10.png)
  ![](images/R2_stp_vlan10.png)
  - vlan 20
  ![](images/R1_stp_vlan20.png)
  ![](images/R2_stp_vlan20.png)

### На роутере R6 настроено два виртуальных порта
![](images/R6_ip_interface.png)