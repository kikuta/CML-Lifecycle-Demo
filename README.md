# Cisco Modeling Labs (CML) API Demo for simulation lifecycle

* [CML2.0](https://developer.cisco.com/modeling-labs/) is network simulation platform by Cisco including Routers/Switches/Servers and more.
* CML2.0 supports lightweight and easy-to-use GUI as well as over 130 APIs
* Not only getting lab simulations information but also creating/deleting labs with configuration files by code
* CML APIs helps CI/CD, NetDevOps :-)
* To start learning CML APIs, it would be great to start following demos/hands-on. Enjoy!

![Lab lifecycle with CML](./SS1.png)

## Preparation. Change env_lab.py.yourifle to env_lab.py

env_lab.py must include the ip address of your CML, username, and password. You have to change the filename and host/username/password in it.

```
% cat env_lab.py.yourconfig 
CML = {
    "host": "<cml_ip_address>",
    "username": "<username>",
    "password": "<password>"
}
```

## Demo 1.  Get authentication Token
### auth.py
```
% python auth.py 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTU5NjQzNzc0NywiZXhwIjoxNTk2NTI0MTQ3LCJzdWIiOiIxMDEifQ.-csBly7oKqiN8WOcpm7uQFPL2PDiVp__sHAkaLk3NMc
```

## Demo 2. Get Simulated labs information on CML
### hellocml.py
```
% python hellocml.py 
#################################################################################################################
# Simulated labs on CML: 19 at CML Lab 10.71.154.73
#################################################################################################################
Test by tatsaito                          2020-06-11 13:33:46   STOPPED           https://10.71.154.73/lab/866cb6
test by rmaruyam                          2020-06-11 09:17:08   DEFINED_ON_CORE   https://10.71.154.73/lab/b3a6eb
To DNAC96                                 2020-06-17 05:01:40   STARTED           https://10.71.154.73/lab/2ba4d1
test by asai                              2020-06-17 07:21:17   STOPPED           https://10.71.154.73/lab/eeca34
CML-DevNet-Lab                            2020-06-22 11:16:04   STARTED           https://10.71.154.73/lab/48cadf
TEST Lab asai                             2020-06-23 17:42:14   STOPPED           https://10.71.154.73/lab/72cbd5
Lab asai                                  2020-06-24 11:00:16   STOPPED           https://10.71.154.73/lab/0fbd5d
TEST Lab asai                             2020-06-24 13:17:08   STOPPED           https://10.71.154.73/lab/f2d3c5
asai                                      2020-06-25 13:36:02   STOPPED           https://10.71.154.73/lab/0574e5
CML Basic Lab                             2020-06-26 13:37:36   STOPPED           https://10.71.154.73/lab/deaf38
manual_config_live_vis_configured.virl    2020-06-29 04:11:33   STOPPED           https://10.71.154.73/lab/80bbfd
Nov_webinar_demo_topology.virl            2020-06-29 06:25:31   DEFINED_ON_CORE   https://10.71.154.73/lab/65ccf2
July_webinar_ospf_eigrp.virl              2020-06-29 06:37:50   DEFINED_ON_CORE   https://10.71.154.73/lab/609fbc
Mar15_webinar_l2_unmanaged.virl           2020-06-29 06:38:18   DEFINED_ON_CORE   https://10.71.154.73/lab/bae85c
maruyama-API-Lab                          2020-07-19 09:07:25   STOPPED           https://10.71.154.73/lab/ebbddc
test-topology-kikuta                      2020-07-20 13:23:37   DEFINED_ON_CORE   https://10.71.154.73/lab/94d9b1
pyATS-test                                2020-07-21 03:08:31   STOPPED           https://10.71.154.73/lab/dede52
Lab at Tue 13:34 PM                       2020-07-21 13:34:27   DEFINED_ON_CORE   https://10.71.154.73/lab/26fbfb
guestshell-testmaru                       2020-07-22 11:54:07   STOPPED           https://10.71.154.73/lab/1bbb3d
#################################################################################################################
```

## Demo 3. Import and start a lab simulation with lab file (yaml)
### import.py
### test-topology.yaml

Please note you must have yaml file to import the lab. From CML GUI, you can download the yaml file, share it with team, or you can find yaml file on community like github.

![Lab YAML file download from GUI](./SS2.png)

```
% python import.py test-topology.yaml 
Please input an lab title [type q to quit]: test-by-kikuta
test-topology.yaml
<Response [200]>
```

## Demo 4. Delete a simulated lab
### delete.py
```
% python delete.py                   
Please input lab ID to be deleted? [type q to quit]: 42aaf9
<Response [200]>
```

## Demo 5. Get a testbed file (yaml) for pyATS
### pyats_testbed.py
```
% python pyats_testbed.py 
Please input lab ID to be deleted? [type q to quit]: 48cadf
testbed:
  name: CML-DevNet-Lab
  tacacs:
    login_prompt: 'login:'
    password_prompt: 'Password:'
    username: '%ENV{PYATS_USERNAME}'
  passwords:
    tacacs: '%ENV{PYATS_PASSWORD}'
    enable: '%ENV{PYATS_AUTH_PASS}'
    line: '%ENV{PYATS_PASSWORD}'
devices:
  terminal_server:
    os: linux
    type: linux
    connections:
      cli:
        protocol: ssh
        ip: 10.71.154.73
        username: change_me
        password: change_me
  csr1000v-3:
    os: iosxe
    type: router
    series: csr1000v
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n5/0
  ubuntu-WorkStation:
    os: linux
    type: server
    tacacs:
      username: cisco
    passwords:
      linux: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n7/0
  iosv-0:
    os: ios
    type: router
    series: iosv
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n9/0
  iosv-1:
    os: ios
    type: router
    series: iosv
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n10/0
  iosvl2-0_0:
    os: ios
    type: switch
    series: iosv
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n11/0
  iosvl2-1_0:
    os: ios
    type: switch
    series: iosv
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n0/0
  desktop-0:
    os: linux
    type: server
    tacacs:
      username: cisco
    passwords:
      linux: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n2/0
  ubuntu-Netbox:
    os: linux
    type: server
    tacacs:
      username: cisco
    passwords:
      linux: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n8/0
  nxos9000-0:
    os: nxos
    type: switch
    series: n9k
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n1/0
  csr1000v-2:
    os: iosxe
    type: router
    series: csr1000v
    tacacs:
      username: cisco
    passwords:
      tacacs: cisco
    connections:
      defaults:
        class: unicon.Unicon
      a:
        protocol: telnet
        proxy: terminal_server
        command: open /48cadf/n4/0
topology:
  csr1000v-3:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet1:
        link: l5
        type: ethernet
      GigabitEthernet2:
        link: l11
        type: ethernet
      GigabitEthernet3:
        link: l12
        type: ethernet
      GigabitEthernet4:
        link: l17
        type: ethernet
      GigabitEthernet5:
        type: ethernet
      GigabitEthernet6:
        type: ethernet
      GigabitEthernet7:
        type: ethernet
      GigabitEthernet8:
        type: ethernet
  ubuntu-WorkStation:
    interfaces:
      enp0s2:
        link: l15
        type: ethernet
  iosv-0:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet0/0:
        link: l2
        type: ethernet
      GigabitEthernet0/1:
        link: l13
        type: ethernet
      GigabitEthernet0/2:
        link: l7
        type: ethernet
      GigabitEthernet0/3:
        link: l16
        type: ethernet
      GigabitEthernet0/4:
        type: ethernet
      GigabitEthernet0/5:
        type: ethernet
      GigabitEthernet0/6:
        type: ethernet
      GigabitEthernet0/7:
        type: ethernet
  iosv-1:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet0/0:
        link: l3
        type: ethernet
      GigabitEthernet0/1:
        type: ethernet
      GigabitEthernet0/2:
        link: l11
        type: ethernet
      GigabitEthernet0/3:
        link: l16
        type: ethernet
      GigabitEthernet0/4:
        type: ethernet
      GigabitEthernet0/5:
        link: l19
        type: ethernet
      GigabitEthernet0/6:
        type: ethernet
      GigabitEthernet0/7:
        type: ethernet
  iosvl2-0_0:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet0/0:
        link: l1
        type: ethernet
      GigabitEthernet0/1:
        link: l9
        type: ethernet
      GigabitEthernet0/2:
        link: l13
        type: ethernet
      GigabitEthernet0/3:
        type: ethernet
      GigabitEthernet1/0:
        type: ethernet
      GigabitEthernet1/1:
        type: ethernet
      GigabitEthernet1/2:
        type: ethernet
      GigabitEthernet1/3:
        type: ethernet
  iosvl2-1_0:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet0/0:
        link: l8
        type: ethernet
      GigabitEthernet0/1:
        link: l9
        type: ethernet
      GigabitEthernet0/2:
        type: ethernet
      GigabitEthernet0/3:
        link: l19
        type: ethernet
      GigabitEthernet1/0:
        type: ethernet
      GigabitEthernet1/1:
        type: ethernet
      GigabitEthernet1/2:
        type: ethernet
      GigabitEthernet1/3:
        type: ethernet
  desktop-0:
    interfaces:
      eth0:
        link: l14
        type: ethernet
  ubuntu-Netbox:
    interfaces:
      enp0s2:
        link: l18
        type: ethernet
  nxos9000-0:
    interfaces:
      Loopback0:
        type: loopback
      mgmt0:
        link: l6
        type: ethernet
      Ethernet1/1:
        link: l10
        type: ethernet
      Ethernet1/2:
        link: l12
        type: ethernet
      Ethernet1/3:
        type: ethernet
      Ethernet1/4:
        type: ethernet
      Ethernet1/5:
        type: ethernet
      Ethernet1/6:
        type: ethernet
      Ethernet1/7:
        link: l20
        type: ethernet
  csr1000v-2:
    interfaces:
      Loopback0:
        type: loopback
      GigabitEthernet1:
        link: l4
        type: ethernet
      GigabitEthernet2:
        link: l7
        type: ethernet
      GigabitEthernet3:
        link: l10
        type: ethernet
      GigabitEthernet4:
        link: l17
        type: ethernet
```
```
% ls | grep 48cadf
pyatsTb_48cadf.yaml
```

## Reference

* [CML2.0 on Cisco DevNet](https://developer.cisco.com/modeling-labs/)

* [Cisco Modeling Labs (CML)を使ってネットワークを学ぼう！（基礎編）](https://learningnetwork.cisco.com/s/article/jp-webinar-cml01)

* [Cisco Modeling Labs (CML)を使ってネットワークを学ぼう！（応用編）](https://learningnetwork.cisco.com/s/article/jp-webinar-cml02)

* [Cisco Modeling Labs (CML)を使ってネットワークを学ぼう！（DevNet編）](https://learningnetwork.cisco.com/s/article/jp-webinar-cml03)