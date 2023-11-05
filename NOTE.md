# Bitizen 加密算法第二次评估

## 硬件

### x86_64

####  cpu

Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz

```
root@arweave:/opt/bitizen# cat /proc/cpuinfo 
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.032
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 0
cpu cores       : 4
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.241
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 1
cpu cores       : 4
apicid          : 2
initial apicid  : 2
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 2
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.070
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 2
cpu cores       : 4
apicid          : 4
initial apicid  : 4
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 3
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.242
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 3
cpu cores       : 4
apicid          : 6
initial apicid  : 6
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 4
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.451
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 0
cpu cores       : 4
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 5
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 801.324
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 1
cpu cores       : 4
apicid          : 3
initial apicid  : 3
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 6
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.104
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 2
cpu cores       : 4
apicid          : 5
initial apicid  : 5
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

processor       : 7
vendor_id       : GenuineIntel
cpu family      : 6
model           : 60
model name      : Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
stepping        : 3
microcode       : 0x28
cpu MHz         : 800.409
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 3
cpu cores       : 4
apicid          : 7
initial apicid  : 7
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 8000.32
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:

```

#### memory

```bash
df -h
Filesystem                         Size  Used Avail Use% Mounted on
udev                               7.8G     0  7.8G   0% /dev
tmpfs                              1.6G  1.5M  1.6G   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  233G   14G  207G   7% /
tmpfs                              7.8G     0  7.8G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
tmpfs                              7.8G     0  7.8G   0% /sys/fs/cgroup
/dev/sda1                          916G   28K  870G   1% /opt/data
/dev/sdb2                          974M  210M  697M  24% /boot
/dev/sdb1                          511M  6.1M  505M   2% /boot/efi
/dev/loop1                          64M   64M     0 100% /snap/core20/1822
/dev/loop0                          56M   56M     0 100% /snap/core18/2697
/dev/loop2                          92M   92M     0 100% /snap/lxd/23991
/dev/loop3                          56M   56M     0 100% /snap/core18/2796
/dev/loop4                          50M   50M     0 100% /snap/snapd/18357
/dev/loop5                          50M   50M     0 100% /snap/snapd/17950
/dev/loop6                          92M   92M     0 100% /snap/lxd/24061
/dev/loop7                          64M   64M     0 100% /snap/core20/2015
tmpfs                              1.6G     0  1.6G   0% /run/user/1000
tmpfs                              1.6G     0  1.6G   0% /run/user/0

free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       2.3Gi        11Gi       1.0Mi       1.8Gi        12Gi
Swap:         4.0Gi          0B       4.0Gi
```

### aarch64

#### cpu

Rochip RK3566

```bash
cat /proc/cpuinfo
processor       : 0
BogoMIPS        : 48.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x2
CPU part        : 0xd05
CPU revision    : 0

processor       : 1
BogoMIPS        : 48.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x2
CPU part        : 0xd05
CPU revision    : 0

processor       : 2
BogoMIPS        : 48.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x2
CPU part        : 0xd05
CPU revision    : 0

processor       : 3
BogoMIPS        : 48.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x2
CPU part        : 0xd05
CPU revision    : 0

Hardware        : RK3500
Serial          : dddd13e07e86f914

```

#### memory

```bash
free -h
              total        used        free      shared  buff/cache   available
Mem:          1.9Gi       292Mi        20Mi       0.0Ki       1.6Gi       1.6Gi
```

```bash
df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            983M     0  983M   0% /dev
tmpfs           199M  396K  199M   1% /run
/dev/mmcblk0p2   58G  7.0G   49G  13% /
tmpfs           995M     0  995M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           995M     0  995M   0% /sys/fs/cgroup
overlay          58G  7.0G   49G  13% /var/lib/docker/overlay2/bc0ed913fdf3ccdd202416f9d8df7d08594814239b28a1e932c985afebfdcb67/merged
tmpfs           199M     0  199M   0% /run/user/1000
```

## 软件

### x86_64

#### Linux 

```
uname -r
5.4.0-139-generic
```

#### ubuntu 20.04

```
cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.5 LTS"
```

#### python

```
python3 --version
Python 3.8.10
```

### aarch64

#### linux

```bash
uname -r
4.19.193-22-xx-xx
```

#### debian

```bash
cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

#### python

```bash
python3 --version
Python 3.7.3
```

## 测试环境搭建

### x86_64 服务端

```
apt install python3-pip
python3 -m pip install websockets requests websocket-client
```

### aarch64 客户端

```
apt install netdata
pip3 install websockets requests websocket-client
```

### 网络延时

```
root@aarch64:/opt/bitizen# ping 192.168.192.4
PING 192.168.192.4 (192.168.192.4) 56(84) bytes of data.
64 bytes from 192.168.192.4: icmp_seq=1 ttl=64 time=0.430 ms
64 bytes from 192.168.192.4: icmp_seq=2 ttl=64 time=0.634 ms
64 bytes from 192.168.192.4: icmp_seq=3 ttl=64 time=0.669 ms
64 bytes from 192.168.192.4: icmp_seq=4 ttl=64 time=0.652 ms
64 bytes from 192.168.192.4: icmp_seq=5 ttl=64 time=0.660 ms
64 bytes from 192.168.192.4: icmp_seq=6 ttl=64 time=0.346 ms
64 bytes from 192.168.192.4: icmp_seq=7 ttl=64 time=0.671 ms
64 bytes from 192.168.192.4: icmp_seq=8 ttl=64 time=0.629 ms
64 bytes from 192.168.192.4: icmp_seq=9 ttl=64 time=0.645 ms
64 bytes from 192.168.192.4: icmp_seq=10 ttl=64 time=0.632 ms
64 bytes from 192.168.192.4: icmp_seq=11 ttl=64 time=0.657 ms
64 bytes from 192.168.192.4: icmp_seq=12 ttl=64 time=0.631 ms
64 bytes from 192.168.192.4: icmp_seq=13 ttl=64 time=0.655 ms
```

## 测试结果

|                    | x86_64 | aarch64 |
| ------------------ | ------ | ------- |
| CMP 协议测试       | 2.105  | 24.827  |
| CMP Keygen 测试    | 3.580  | 40.030  |
| CMP Reshare 测试   | 4.480  | 34.149  |
| FROST 签名测试     | 0.217  | 0.329   |
| FROST Keygen 测试  | 0.219  | 0.329   |
| FROST Reshare 测试 | 0.219  | 3.022   |

分析：

- CMP 协议测试跑满了一个核心（1/4），使用率 30%
- aaarch64 版本测试耗时远高于 x86_64 平台数据，10倍差异
  - 上一版本测试 x86_64 与 aarch64 差异大概在 20% 左右

## 测试日志

### CMP 协议测试

#### B (x86_64) + A (x86_64)

```
python3 test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_b.txt
participant_id b
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 06:42:04 Found msg: message: round 2, from: b, to , protocol: cmp/sign
2023/11/05 06:42:04 Found msg: message: round 2, from: b, to a, protocol: cmp/sign
--- step 1 TIME 0.1285402774810791 seconds ---
calling PerformRound
2023/11/05 06:42:08 Found msg: message: round 3, from: b, to , protocol: cmp/sign
2023/11/05 06:42:08 Found msg: message: round 3, from: b, to a, protocol: cmp/sign
--- step 2 TIME 0.8707950115203857 seconds ---
calling PerformRound
2023/11/05 06:42:09 Found msg: message: round 4, from: b, to , protocol: cmp/sign
2023/11/05 06:42:09 Found msg: message: round 4, from: b, to a, protocol: cmp/sign
--- step 3 TIME 0.5885250568389893 seconds ---
calling PerformRound
2023/11/05 06:42:09 Found msg: message: round 5, from: b, to , protocol: cmp/sign
--- step 4 TIME 0.09123492240905762 seconds ---
calling PerformRound
--- step 5 TIME 0.0004267692565917969 seconds ---
calling CmpSignResult
SIGN END omFSWCEDYHHEYafjzHdpp6Y1i92QOzPPAeyuGK8KZUZvj1O9aoJhU1ggrLtm2i6okqYfqCIOH3u5/flqPatMI2F81Gi5xAp1B58=--- SIGN TIME 4.911971807479858 seconds ---



root@x86_64:/opt/bitizen# python3 test_client.py cmp_sign ws://192.168.192.4:8000 cmp_keyshare_a.txt
participant_id a   
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 06:42:07 Found msg: message: round 2, from: a, to , protocol: cmp/sign 
2023/11/05 06:42:07 Found msg: message: round 2, from: a, to b, protocol: cmp/sign
--- step 1 TIME 0.1288316249847412 seconds ---
calling PerformRound
2023/11/05 06:42:08 Found msg: message: round 3, from: a, to , protocol: cmp/sign
2023/11/05 06:42:08 Found msg: message: round 3, from: a, to b, protocol: cmp/sign
--- step 2 TIME 0.8737409114837646 seconds ---
calling PerformRound
2023/11/05 06:42:09 Found msg: message: round 4, from: a, to , protocol: cmp/sign 
2023/11/05 06:42:09 Found msg: message: round 4, from: a, to b, protocol: cmp/sign
--- step 3 TIME 0.5875899791717529 seconds ---
calling PerformRound
2023/11/05 06:42:09 Found msg: message: round 5, from: a, to , protocol: cmp/sign
--- step 4 TIME 0.0872194766998291 seconds ---
calling PerformRound
--- step 5 TIME 0.0005097389221191406 seconds ---
calling CmpSignResult
SIGN END omFSWCEDYHHEYafjzHdpp6Y1i92QOzPPAeyuGK8KZUZvj1O9aoJhU1ggrLtm2i6okqYfqCIOH3u5/flqPatMI2F81Gi5xAp1B58=--- SIGN TIME 2.104623794555664 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 ws_server.py 8000    # 机器 B 终端 1 中执行
python3 test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_b.txt         # 机器 B 终端 2 中执行

root@x86_64:/opt/bitizen# python3 test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_b.txt
participant_id b
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 05:53:45 Found msg: message: round 2, from: b, to , protocol: cmp/sign
2023/11/05 05:53:45 Found msg: message: round 2, from: b, to a, protocol: cmp/sign
--- step 1 TIME 0.12770414352416992 seconds ---
calling PerformRound
2023/11/05 05:53:56 Found msg: message: round 3, from: b, to , protocol: cmp/sign
2023/11/05 05:53:56 Found msg: message: round 3, from: b, to a, protocol: cmp/sign
--- step 2 TIME 0.8762531280517578 seconds ---
calling PerformRound
2023/11/05 05:54:09 Found msg: message: round 4, from: b, to , protocol: cmp/sign
2023/11/05 05:54:09 Found msg: message: round 4, from: b, to a, protocol: cmp/sign
--- step 3 TIME 0.5852887630462646 seconds ---
calling PerformRound
2023/11/05 05:54:17 Found msg: message: round 5, from: b, to , protocol: cmp/sign
--- step 4 TIME 0.0971524715423584 seconds ---
calling PerformRound
--- step 5 TIME 0.0012028217315673828 seconds ---
calling CmpSignResult
SIGN END omFSWCEDI5l1KUQEXP3HzwudT/NZXXWC7LgiO5e2GHGNhevgEa5hU1gg2UBIkdYiHyJYMTlI2rcumpj4ljkVZhsoTY4DDXK220I=
--- SIGN TIME 32.76248073577881 seconds ---

root@aarch64:/opt/bitizen# python3 test_client.py cmp_sign ws://192.168.192.4:8000 cmp_keyshare_a.txt
participant_id a
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 05:53:55 Found msg: message: round 2, from: a, to , protocol: cmp/sign
2023/11/05 05:53:55 Found msg: message: round 2, from: a, to b, protocol: cmp/sign
--- step 1 TIME 1.8636157512664795 seconds ---
calling PerformRound
2023/11/05 05:54:08 Found msg: message: round 3, from: a, to , protocol: cmp/sign
2023/11/05 05:54:08 Found msg: message: round 3, from: a, to b, protocol: cmp/sign
--- step 2 TIME 12.855089664459229 seconds ---
calling PerformRound
2023/11/05 05:54:17 Found msg: message: round 4, from: a, to , protocol: cmp/sign
2023/11/05 05:54:17 Found msg: message: round 4, from: a, to b, protocol: cmp/sign
--- step 3 TIME 8.554123878479004 seconds ---
calling PerformRound
2023/11/05 05:54:18 Found msg: message: round 5, from: a, to , protocol: cmp/sign
--- step 4 TIME 1.2836995124816895 seconds ---
calling PerformRound
--- step 5 TIME 0.005034446716308594 seconds ---
calling CmpSignResult
SIGN END omFSWCEDI5l1KUQEXP3HzwudT/NZXXWC7LgiO5e2GHGNhevgEa5hU1gg2UBIkdYiHyJYMTlI2rcumpj4ljkVZhsoTY4DDXK220I=
--- SIGN TIME 24.827894926071167 seconds ---
```

![image-20231105135609973](https://img.cactes.com/20231105-135612-968.png)

![image-20231105135940701](https://img.cactes.com/20231105-135942-384.png)

![image-20231105145656859](https://img.cactes.com/20231105-145658-468.png)



### CMP Keygen 测试

#### B (x86_64) + A (x86_64)

```
 python3 test_client.py cmp_keygen ws://127.0.0.1:8000 b
KEYGEN START
calling CmpKeygenInit
calling PerformRound
2023/11/05 07:18:35 Found msg: message: round 2, from: b, to , protocol: cmp/keygen-threshold
--- step 1 TIME 0.5790140628814697 seconds ---
calling PerformRound
2023/11/05 07:18:47 Found msg: message: round 3, from: b, to , protocol: cmp/keygen-threshold
--- step 2 TIME 0.0003609657287597656 seconds ---
calling PerformRound
2023/11/05 07:18:48 Found msg: message: round 4, from: b, to , protocol: cmp/keygen-threshold
2023/11/05 07:18:48 Found msg: message: round 4, from: b, to a, protocol: cmp/keygen-threshold
--- step 3 TIME 1.2312965393066406 seconds ---
calling PerformRound
2023/11/05 07:18:49 Found msg: message: round 5, from: b, to , protocol: cmp/keygen-threshold
--- step 4 TIME 0.38443613052368164 seconds ---
calling PerformRound
--- step 5 TIME 0.0004940032958984375 seconds ---
calling CmpKeygenResult
KEYGEN END WQiWqWJJRGFiaVRocmVzaG9sZAFlRUNEU0FYIJYR/kf1tf90F81r2IZtF6cIql9+fJ1nh9YHVfbVaiS/Z0VsR2FtYWxYIF+qdD8P9OeA5lkYrH4Mjd3A7u6nFEdL3Kzd6MWMkVBXYVBYgMDzdvt/fRqNhhV8mMMCyz1ZHF8HROwNMqksVxXygvFLkAzyHo7ZMPXGmzpr26aEBs81kwqnlrru2DGvp1EoFr4pF9f8rhiMSBE8yLOYI52PcUPgQELxJ2IByLyXcwA+aoA9jqVkE/l57TVlxRvcqlthGLsm90NtTjjs76qX5tQ/YVFYgMNJSlHJBZ5GNeWe9ECB/9Cr3CdCMz8Wpd2UgHzfSKjwQ7CO0FYkAxR48i3SZLakd78A4nrO05b/QuoO7hzu7ASdSvM80EvN6nmx6TsaYE4WCs3Sbsi1BZZYG/kXZvOHF7gwJhYq41VION068AfxMinnYAwc1w+BBqDnDEqiBCivY1JJRFggcQJ4982kdzbL99AC/bZbmyE6zd9oEcmSdouk+g1pqdVoQ2hhaW5LZXlYIAijjR4+ePb+4ebLZgXNlrqZDsJS816tGy2jAbitzXQNZlB1YmxpY4KmYklEYWFlRUNEU0FYIQIHX9er7eIsJ4PMoc1k0iAbtp7CJvgdjhAslYKoUvpyFWdFbEdhbWFsWCECHAdOfuZ7GH3h2xHVnwAFZ5A3rDrDHdVG0NxwRC9hLgZhTlkBALcmOSDEIACsOlGX69iABo5FN9GMdKHb9/pbVsqpYaqYsJHwW2n3YOwsEHHjGF3nHyZGXONvw9qNkWI9yng7NZ8CIfYPzoRZF6SZS5P5tPg4A/jAJ9Pvf5wWRRu6huOSM92YQApgf6UIdClNL9dv/55HZU4V6lAkh40fTV5kqPhIHXuFY/Sy5PTI8YcZ0lioxDEPshbmc581JTllFr798bjx4qn151A2ffyWd/mVYkJ3xT+RCSjX10EIh71LjoSjkDKna8rzp3enY2e60ubUCPY5QCVWftWbzmCTMd6fVMGSN+LOL/nM9dUbphnxne3u9oApWaer+j4uxBJDboWOEw1hU1kBAGY2Eie84V0l/tXsB9UjzRaQjXNobjjZRtDF+UcL1exGz3NleJupfeqQdPsIxIZmvX7Fe+OF++FezzrPc/6PeKOYCSbfg/qa1bCS4J3FZv1p+lPimPJuAXuZ/lSMZYUHAOHfc794Dj/4MuthaJ03MQwg/6F7HR4C+G53S6Uglb6VMTOKJceVBz6tAZPMEd/3uqRq64pzEcMF6pX4HPrxe53yzo11Vj3eTbeybXNhQhqsPNCFMhNUV+z/yxMfQA7TR1XUm4TM5DMT1cqpmTgSB6LcMljaKfHRhfo/hNBHwivLdP57I3AUmoDzbGGr7yCpO2tLzcMYDfzA832xwrq7tiNhVFkBAJl92S2Si21dwM69/OHXfn3xvY819TOXKXb582x4QR3ixWLZStRF8zjcH/fMpoK37Qo7y+rkXbDhM/XQQiEO/gngjhn78kPMn3y6rTq8Xq2Pk8/0cM8rTUZlIrvEgj//Ai9kAQIwsP9PwAIK9P1ms15UGKVwfUBilbbP5xCKAIiKQNMNDw35B9HAcBHS1PueeVS4KYuP6tE8caBD/62Bq4/jv85mnidMnRTG5K3E1IsvaqVLRiuHCAtC6uFb0AV/UIQaaXfDp97QikrIkkxnjGpRQS4/h5ccpAxkXGn3WejyLYqeIYO+VzIZbhXACVnnbwB433EYwS97m+zs0rPtOOamYklEYWJlRUNEU0FYIQMfifZw/eAIEO6D5mCYO9Tt47eYboOIW+tBBnr+cVDbZGdFbEdhbWFsWCED83XzeRCKPnV8XqVuXkkloBukQC4J9vBCsSRdFwSV3pBhTlkBAJMwsRKExGLL2GPbixkH1Q3lVLpejIbKyNshNZDBv/ERe7+/sfRpQhpRmbKAZXapNzr74ZseMXXc7uv5KNI4IArko9goGwg77WI4paRk8hAYOw9i0LWQ1EIMnvHhyERgYToz80v14W7IIk3lcLGv9RWkaaXKxpxvj53wMJV28wrr/LavPds20lff3uJC3fmgDhO/nHOdBoxksqZQGV6oAwXtnH5BcmoP7pRIS24mkh/xH/KOdzTfx1FNPF7n/TSRyzpmYcjLI5Np+kay2uTADiqlv9/qOHkKZ5vmypFcWWCG0/yw7FvGmACncTdbbO4lGeS3x5NwERmVQbo9exbw7xFhU1kBADiWilumhYi6ASDmZozgcsnZ9lVpNvFysILZ8/4kw+1gHWTLXK1OwJzI0c0+bXbhCzzuz2zuh0uWZKRwwf8UKMC+gGE79I0FCZ3nHsCyjWyrXA3aazt67lQIudbiH7+yRZELlu74McBwGDj8sSBvJjtg8qu3E8iq385PCSKErmDP+Gvhd6DfSWhkrANQrqRpNS6K9HmRmLvhbVnorymnwvTWEYo/tRBhaUjrBGcogQvqcp89Sjl1rF6VzDesUYWqDmlf7d/sYPMGexeJtxIhjo66zZe3eGjdUvShu1DaCKtyTJ+ZHK0GMBd/POd8AOIpl+xlkuWrpWX+UHv5B67sxbVhVFkBAI5qMh37GXvqhU9XTe+Zcv7QVcX4dWhqTrfNZl6GY+ChdagAiaODmQiBoOWGzJSbVJDRWAhcYi4cton2+9JBudGFlR2nwjsexhMRpwJBS/1IUqhXKdqQwMzwhjfP53VAha0otY1ql6ojTgwHMCnkPaTwq9PVigDDxoUpetWPlue8jMDhmOXVfa591JB6iIn/E3bh/l3fc2peRUNP29PEZQ2ZcrwmGbX+Iaoljo9rVlouZAuDawmlTKWSdyNm3azlkctgJCjNDeQ4zmQYpgL3bnRiIP0JgeXB2RxWTod1oFbrJLx2FMk1Wa83aFYw1qChrzoCJwGGyuKrfGCP0VLwLZ8=
--- KEYGEN TIME 14.417959451675415 seconds ---

python3 test_client.py cmp_keygen ws://127.0.0.1:8000 a 
KEYGEN START
calling CmpKeygenInit
calling PerformRound
2023/11/05 07:18:47 Found msg: message: round 2, from: a, to , protocol: cmp/keygen-threshold
--- step 1 TIME 1.5599305629730225 seconds ---
calling PerformRound
2023/11/05 07:18:47 Found msg: message: round 3, from: a, to , protocol: cmp/keygen-threshold
--- step 2 TIME 0.00017142295837402344 seconds ---
calling PerformRound
2023/11/05 07:18:48 Found msg: message: round 4, from: a, to , protocol: cmp/keygen-threshold
2023/11/05 07:18:48 Found msg: message: round 4, from: a, to b, protocol: cmp/keygen-threshold
--- step 3 TIME 1.2006566524505615 seconds ---
calling PerformRound
2023/11/05 07:18:49 Found msg: message: round 5, from: a, to , protocol: cmp/keygen-threshold
--- step 4 TIME 0.41375017166137695 seconds ---
calling PerformRound
--- step 5 TIME 0.0008409023284912109 seconds ---
calling CmpKeygenResult
KEYGEN END WQiWqWJJRGFhaVRocmVzaG9sZAFlRUNEU0FYIFaakodtUvQviXRMl/gEv9VeQoo3DXvTJXGHx8OAbbvcZ0VsR2FtYWxYIOp3Lw8aG57/807AWAH17qNjQ1Rm0cpGFqbqhaTVd4K0YVBYgMvyWpkpnafGsBDjpkarNtcsuqtqzqxyOvd55OhT90c6D0irjm3zRGvr/RWJvp37+wJ/MI0JzEiSf/9boCrGknFBG0KkjTpB2Q/URLy8YkAlNVJefECiIqnusJ5l9lmSmCTyyj7NNoe5sLBOyI6QvofUlUTd2KDXnr80YJZGQLTDYVFYgOXk/dsbJQCOW+uppKFi2dremF4RUKGKCl+WdOTta5EMQgYYCG8EG/9menrN6I5Rk//4rPBiTfcUWAfEPWAgZBz9eiPJIA+1W43JEzRCDg41jMS0ePR0YbuVT/JaFk0oZo8yrKRlmUsUWJjhxenzmS+wxGKHonPV+MbXTgJXTFvvY1JJRFggcQJ4982kdzbL99AC/bZbmyE6zd9oEcmSdouk+g1pqdVoQ2hhaW5LZXlYIAijjR4+ePb+4ebLZgXNlrqZDsJS816tGy2jAbitzXQNZlB1YmxpY4KmYklEYWFlRUNEU0FYIQIHX9er7eIsJ4PMoc1k0iAbtp7CJvgdjhAslYKoUvpyFWdFbEdhbWFsWCECHAdOfuZ7GH3h2xHVnwAFZ5A3rDrDHdVG0NxwRC9hLgZhTlkBALcmOSDEIACsOlGX69iABo5FN9GMdKHb9/pbVsqpYaqYsJHwW2n3YOwsEHHjGF3nHyZGXONvw9qNkWI9yng7NZ8CIfYPzoRZF6SZS5P5tPg4A/jAJ9Pvf5wWRRu6huOSM92YQApgf6UIdClNL9dv/55HZU4V6lAkh40fTV5kqPhIHXuFY/Sy5PTI8YcZ0lioxDEPshbmc581JTllFr798bjx4qn151A2ffyWd/mVYkJ3xT+RCSjX10EIh71LjoSjkDKna8rzp3enY2e60ubUCPY5QCVWftWbzmCTMd6fVMGSN+LOL/nM9dUbphnxne3u9oApWaer+j4uxBJDboWOEw1hU1kBAGY2Eie84V0l/tXsB9UjzRaQjXNobjjZRtDF+UcL1exGz3NleJupfeqQdPsIxIZmvX7Fe+OF++FezzrPc/6PeKOYCSbfg/qa1bCS4J3FZv1p+lPimPJuAXuZ/lSMZYUHAOHfc794Dj/4MuthaJ03MQwg/6F7HR4C+G53S6Uglb6VMTOKJceVBz6tAZPMEd/3uqRq64pzEcMF6pX4HPrxe53yzo11Vj3eTbeybXNhQhqsPNCFMhNUV+z/yxMfQA7TR1XUm4TM5DMT1cqpmTgSB6LcMljaKfHRhfo/hNBHwivLdP57I3AUmoDzbGGr7yCpO2tLzcMYDfzA832xwrq7tiNhVFkBAJl92S2Si21dwM69/OHXfn3xvY819TOXKXb582x4QR3ixWLZStRF8zjcH/fMpoK37Qo7y+rkXbDhM/XQQiEO/gngjhn78kPMn3y6rTq8Xq2Pk8/0cM8rTUZlIrvEgj//Ai9kAQIwsP9PwAIK9P1ms15UGKVwfUBilbbP5xCKAIiKQNMNDw35B9HAcBHS1PueeVS4KYuP6tE8caBD/62Bq4/jv85mnidMnRTG5K3E1IsvaqVLRiuHCAtC6uFb0AV/UIQaaXfDp97QikrIkkxnjGpRQS4/h5ccpAxkXGn3WejyLYqeIYO+VzIZbhXACVnnbwB433EYwS97m+zs0rPtOOamYklEYWJlRUNEU0FYIQMfifZw/eAIEO6D5mCYO9Tt47eYboOIW+tBBnr+cVDbZGdFbEdhbWFsWCED83XzeRCKPnV8XqVuXkkloBukQC4J9vBCsSRdFwSV3pBhTlkBAJMwsRKExGLL2GPbixkH1Q3lVLpejIbKyNshNZDBv/ERe7+/sfRpQhpRmbKAZXapNzr74ZseMXXc7uv5KNI4IArko9goGwg77WI4paRk8hAYOw9i0LWQ1EIMnvHhyERgYToz80v14W7IIk3lcLGv9RWkaaXKxpxvj53wMJV28wrr/LavPds20lff3uJC3fmgDhO/nHOdBoxksqZQGV6oAwXtnH5BcmoP7pRIS24mkh/xH/KOdzTfx1FNPF7n/TSRyzpmYcjLI5Np+kay2uTADiqlv9/qOHkKZ5vmypFcWWCG0/yw7FvGmACncTdbbO4lGeS3x5NwERmVQbo9exbw7xFhU1kBADiWilumhYi6ASDmZozgcsnZ9lVpNvFysILZ8/4kw+1gHWTLXK1OwJzI0c0+bXbhCzzuz2zuh0uWZKRwwf8UKMC+gGE79I0FCZ3nHsCyjWyrXA3aazt67lQIudbiH7+yRZELlu74McBwGDj8sSBvJjtg8qu3E8iq385PCSKErmDP+Gvhd6DfSWhkrANQrqRpNS6K9HmRmLvhbVnorymnwvTWEYo/tRBhaUjrBGcogQvqcp89Sjl1rF6VzDesUYWqDmlf7d/sYPMGexeJtxIhjo66zZe3eGjdUvShu1DaCKtyTJ+ZHK0GMBd/POd8AOIpl+xlkuWrpWX+UHv5B67sxbVhVFkBAI5qMh37GXvqhU9XTe+Zcv7QVcX4dWhqTrfNZl6GY+ChdagAiaODmQiBoOWGzJSbVJDRWAhcYi4cton2+9JBudGFlR2nwjsexhMRpwJBS/1IUqhXKdqQwMzwhjfP53VAha0otY1ql6ojTgwHMCnkPaTwq9PVigDDxoUpetWPlue8jMDhmOXVfa591JB6iIn/E3bh/l3fc2peRUNP29PEZQ2ZcrwmGbX+Iaoljo9rVlouZAuDawmlTKWSdyNm3azlkctgJCjNDeQ4zmQYpgL3bnRiIP0JgeXB2RxWTod1oFbrJLx2FMk1Wa83aFYw1qChrzoCJwGGyuKrfGCP0VLwLZ8=
--- KEYGEN TIME 3.579882860183716 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 test_client.py cmp_keygen ws://127.0.0.1:8000 b 
KEYGEN START
calling CmpKeygenInit
calling PerformRound
2023/11/05 07:21:15 Found msg: message: round 2, from: b, to , protocol: cmp/keygen-threshold
--- step 1 TIME 3.1477746963500977 seconds ---
calling PerformRound
2023/11/05 07:21:39 Found msg: message: round 3, from: b, to , protocol: cmp/keygen-threshold
--- step 2 TIME 0.0009655952453613281 seconds ---
calling PerformRound
2023/11/05 07:21:40 Found msg: message: round 4, from: b, to , protocol: cmp/keygen-threshold
2023/11/05 07:21:40 Found msg: message: round 4, from: b, to a, protocol: cmp/keygen-threshold
--- step 3 TIME 0.7920017242431641 seconds ---
calling PerformRound
2023/11/05 07:21:51 Found msg: message: round 5, from: b, to , protocol: cmp/keygen-threshold
--- step 4 TIME 0.2880229949951172 seconds ---
calling PerformRound
--- step 5 TIME 0.0012590885162353516 seconds ---
calling CmpKeygenResult
KEYGEN END WQiWqWJJRGFiaVRocmVzaG9sZAFlRUNEU0FYIM+yEPaJnsjEulrPsYYbmmdvYPNIgzVKX3S0WVC/JE7aZ0VsR2FtYWxYIBkWvVdPXX0gwuW/lZpPoSbHQ8LDCqRtA4urqA/eBCgIYVBYgNIuOdVFsWvh61r5PTq9FpM9Cg8JpweF2EMo1ooDiI8N7HWH1xfdVJglkz9+KGmdH4ULPpgswtkuc5RitS/GOcYm/bqsTbtsyinEhYbGx+3cuaLerrS/DnwohQjyCm+GoKMScUXseEHYW4kCnqBh9iS9PgraBC5GBrssETLOFZmDYVFYgPRZNHqCvWP9tItbj4I1APFgx9XdHFuXbl+bXVlWcE0BCoi+24mSmJNTm11QPFZp/qVPBOhbUaFXGTTlpscvmocpJ4dH8CR2vtTklscy7u0fMmG8kz+Z53Cw33tbSB/Ip+S3cOkGnCKwK42o4OCTIiZ046T6y+9a/tiLKYteKNNXY1JJRFgg5oEFxvFVoI2XhInDDZzG7Ax7/8x7qOmMyuuy3LNx6k1oQ2hhaW5LZXlYIEv2gjxqtTZ9K40Azkn7KBJQEYlenOGLrfMX9VcDzjU+ZlB1YmxpY4KmYklEYWFlRUNEU0FYIQJXac8KiL58GSBQB+nnKBb1IKKZIGape95A5xAbHZsDyWdFbEdhbWFsWCECwfEbLpp26M1ebV0nOwe1I/oHPkBY3UvxDsG0QEfzboNhTlkBALpaNKsFv7GGSWlgYtI3onh7Zv8/rxal1CjZWwqYPyZnv1KzqvV3MI41zUEpeT//inMDYsXZQdC7PLN9SJJiFx4uDmztKON5BKyytZq397vfebzHW+2cUzbzqiz/KrndwFXM0pKhMixtTs51emdnArKtZlaohp+wDhRfWn5xCT40qjN1zWCjPQGVL3Vr0/F1P6RgoaFhAilNnz6KVQVIn7QLfzQAepvBozJKMB7M+itfcLLPZlUX9PJd6U0v/A97asZ7FlqM4+U+XXUJmPMS3eUo54rH+HfBHHIxgt2AHTVNoqOZOhzUUc8s1NCVvaKUSHbAt+Q51mvDz4+xtOSnF6VhU1kBALhLc30hl+0mBOfN01GMckwRLET/GpSUy1utnSMHQAAoopJBs93M+xz0ipAEcWA/6lHpnTKKprP0EfrrLeA/azLsz5E+F/SEFxZ9nS6lqet6LgfjylY/ZXHoBuTLRNgtd8sSbtmDkxtFDc5JjCKTgyBN0JDzzNhl5nd9dhekHsvVtkNw8dH6mEMRfsblI3khrCV/dhR0Bwx/l9Wq9GlS6soytKekj0CMeIOKGcmEKwWyNtMKIyhzq4Kfc7QdFtXqBC4vGbyDoejKI9UwfarMrdmMJcoaikfW86iLKXqnYuEHMdO1+GvzU8L5hd+IbfMQCQ2wis1qPWLCOIFDF17u+Q9hVFkBAAJcQwzglB/f3fsSyjMVMxlx9u2UMwj8UJeCrIo7Ucti9Mpx5K2aa/7Ghi9pOnAFMHLsErtY59ynqEXJ7OZqCMedgoFtoZNU+UEpmE20STYcGJG5o23sAA0Hhl0wfHFErhJHcgFA7ciAscG+UPSAcjfmO6I+4lc4x4qZOciuTQJNfFdk6X1REc9j4JO2NNuldfIRSXZA2VTdMyfvDsGhTWplALt2ZZDYs6oc42D+xiKlf5SifSVKDlE7xA9A2WTsYQGjOPuf+d55WQgCkwaM+5PIBlhhyUiU9CY5hEZqjs1R3czo8+QBrDBpr6UOIPi/lIDk3uM2zK2OpoMzSCHEwJSmYklEYWJlRUNEU0FYIQPWd5KG2fgvZBYM611iTbht6Cm5UKDv2J1GEH54FbhV8mdFbEdhbWFsWCECXie6oGD2RkUtZmt+/Vj/XAUvQQVI7rXY9/RT4/IA30VhTlkBAMidTEdasC7kQnTvFh+1gDFXhI6v9TVyKTUJaAPx+vPfrq1UUTqpirWL4KAlG2qb7n5w2cYNPX5ZkLIFeDNnXqMzVGQKpReBSP0iUAwrHcjPb4lhhi1j4nCuiQUIpVSQlbTXQEzaXT27JSQJI61f2mJU3Yj4c4aI+8hT34HgJ55Wi0/fIKwjWq7FJbnoTUaay/oM4CX8POxhMY6215t+wP+QM894Fk1Tozl/pp/hgIMgFam3ZQbfrLCvHNkBMJUE0s0/7PeJFnUapUXIJ0PGaxQ+WNIkMQAPLaqO7anDa09IJKrgwlH8nYqVzcUCYUL9c7LEOTwhEryUgzQu/u1WJIVhU1kBAAvNL4oeWTIjcbIWAuRD3HV2dWheXRjeKosdktfPGC7uSq6GJOfbS97RnRe01Gy+cBZ9U1GflZKw3R4Q55drkn/nSTWyu63m3whKBOywoTk69WuH6snBRFHrEI6RgJc2pbVZhodHOGsfpF2KHIil5T3pcG6wW1ttX4NiV4XFFFpOKRQ2kBKkHeeuTPaWs1smAJtFVSiQTmb39yZqN77e1q7/RGhzVq3kLYYSxVm55BmrqSlitSHhOr3IySWCH6iOMbQz2uiPql1Yf44MrGdPI4BlquFdfYXkqS3YBH75X6v0wrQuAJEn9Srs6HBdv/Zjd8iFbPwHN/0TkyQn1C4K+gthVFkBAIpOAFw3tGakVU5TJP8Lj8aTNgfq8jO1Ff4CRlmJaLAatoPn8WmVqnyGPeFvPy1N4nTLMEUtyUru5reeC08PCUv5rqdKweqnyNyAnaewkCFzJ8JWxI9GXhsNvH+FjDP6EU9lM47Z1h4DPmQBWw6DGv3f2bgpzuj6W9y+/Ux8eKLBqJytNhEyn6niNhh3ZYFVVxpZS617bxtoM8mG9Wti0Ly5apnje6SoZPN8I/+ukLvyYYAUX90coGy28qhmID9gmXjvgV+CZ/XJPIUXVoV5SqutZ/SaIjGm6TYW7Aq9P5No6vmLwGk3ZQJDOVTVTuJpoUHzYNizhyZ9TEWMDXLgiiA=
--- KEYGEN TIME 44.09746432304382 seconds ---


python3 test_client.py cmp_keygen ws://192.168.192.4:8000 a
KEYGEN START
calling CmpKeygenInit
calling PerformRound
2023/11/05 07:21:39 Found msg: message: round 2, from: a, to , protocol: cmp/keygen-threshold
--- step 1 TIME 23.35508418083191 seconds ---
calling PerformRound
2023/11/05 07:21:39 Found msg: message: round 3, from: a, to , protocol: cmp/keygen-threshold
--- step 2 TIME 0.004318714141845703 seconds ---
calling PerformRound
2023/11/05 07:21:50 Found msg: message: round 4, from: a, to , protocol: cmp/keygen-threshold
2023/11/05 07:21:50 Found msg: message: round 4, from: a, to b, protocol: cmp/keygen-threshold
--- step 3 TIME 10.796962261199951 seconds ---
calling PerformRound
2023/11/05 07:21:56 Found msg: message: round 5, from: a, to , protocol: cmp/keygen-threshold
--- step 4 TIME 5.634730339050293 seconds ---
calling PerformRound
--- step 5 TIME 0.007602691650390625 seconds ---
calling CmpKeygenResult
KEYGEN END WQiWqWJJRGFhaVRocmVzaG9sZAFlRUNEU0FYIGzjYdmrPWWrgUnOuQifnkgz8szNwjNKvjCwxWjsQeSFZ0VsR2FtYWxYIDieIn+sG7oZ6BY0iQX9yl8G9pmdx5AQZDeFTtco40+kYVBYgOjvt/6szfUaTMK4TdgxqM7oYygxjSlLo4sgyeTena538xGPQws7HZLoO4sgKzIHg01pgBIzFT1cQ6+FyqBzuLFXWm+iEiZuTb4ZEbK7Rfh70oA3H5/WG90webR0b1Z+8TT86Azl8yUSgggYE+vId5QE8+8Iudgwv6MduaGMbEIrYVFYgMzNtoeF84CS60kCpTJgY16lzMWkiTYd46PEvuesFpiOXrJ9BZUcvmyWSOCXoNfxGvbsLmemrvtCEXG7vR3ddQTEaegcTA5pDP0PXG7XUZROTNW6wWTV/+0BtRotW0Jdq9JkAEA6yqneoxsO69s8Uk/oP7kfl9EJwMqJImlDyrVvY1JJRFgg5oEFxvFVoI2XhInDDZzG7Ax7/8x7qOmMyuuy3LNx6k1oQ2hhaW5LZXlYIEv2gjxqtTZ9K40Azkn7KBJQEYlenOGLrfMX9VcDzjU+ZlB1YmxpY4KmYklEYWFlRUNEU0FYIQJXac8KiL58GSBQB+nnKBb1IKKZIGape95A5xAbHZsDyWdFbEdhbWFsWCECwfEbLpp26M1ebV0nOwe1I/oHPkBY3UvxDsG0QEfzboNhTlkBALpaNKsFv7GGSWlgYtI3onh7Zv8/rxal1CjZWwqYPyZnv1KzqvV3MI41zUEpeT//inMDYsXZQdC7PLN9SJJiFx4uDmztKON5BKyytZq397vfebzHW+2cUzbzqiz/KrndwFXM0pKhMixtTs51emdnArKtZlaohp+wDhRfWn5xCT40qjN1zWCjPQGVL3Vr0/F1P6RgoaFhAilNnz6KVQVIn7QLfzQAepvBozJKMB7M+itfcLLPZlUX9PJd6U0v/A97asZ7FlqM4+U+XXUJmPMS3eUo54rH+HfBHHIxgt2AHTVNoqOZOhzUUc8s1NCVvaKUSHbAt+Q51mvDz4+xtOSnF6VhU1kBALhLc30hl+0mBOfN01GMckwRLET/GpSUy1utnSMHQAAoopJBs93M+xz0ipAEcWA/6lHpnTKKprP0EfrrLeA/azLsz5E+F/SEFxZ9nS6lqet6LgfjylY/ZXHoBuTLRNgtd8sSbtmDkxtFDc5JjCKTgyBN0JDzzNhl5nd9dhekHsvVtkNw8dH6mEMRfsblI3khrCV/dhR0Bwx/l9Wq9GlS6soytKekj0CMeIOKGcmEKwWyNtMKIyhzq4Kfc7QdFtXqBC4vGbyDoejKI9UwfarMrdmMJcoaikfW86iLKXqnYuEHMdO1+GvzU8L5hd+IbfMQCQ2wis1qPWLCOIFDF17u+Q9hVFkBAAJcQwzglB/f3fsSyjMVMxlx9u2UMwj8UJeCrIo7Ucti9Mpx5K2aa/7Ghi9pOnAFMHLsErtY59ynqEXJ7OZqCMedgoFtoZNU+UEpmE20STYcGJG5o23sAA0Hhl0wfHFErhJHcgFA7ciAscG+UPSAcjfmO6I+4lc4x4qZOciuTQJNfFdk6X1REc9j4JO2NNuldfIRSXZA2VTdMyfvDsGhTWplALt2ZZDYs6oc42D+xiKlf5SifSVKDlE7xA9A2WTsYQGjOPuf+d55WQgCkwaM+5PIBlhhyUiU9CY5hEZqjs1R3czo8+QBrDBpr6UOIPi/lIDk3uM2zK2OpoMzSCHEwJSmYklEYWJlRUNEU0FYIQPWd5KG2fgvZBYM611iTbht6Cm5UKDv2J1GEH54FbhV8mdFbEdhbWFsWCECXie6oGD2RkUtZmt+/Vj/XAUvQQVI7rXY9/RT4/IA30VhTlkBAMidTEdasC7kQnTvFh+1gDFXhI6v9TVyKTUJaAPx+vPfrq1UUTqpirWL4KAlG2qb7n5w2cYNPX5ZkLIFeDNnXqMzVGQKpReBSP0iUAwrHcjPb4lhhi1j4nCuiQUIpVSQlbTXQEzaXT27JSQJI61f2mJU3Yj4c4aI+8hT34HgJ55Wi0/fIKwjWq7FJbnoTUaay/oM4CX8POxhMY6215t+wP+QM894Fk1Tozl/pp/hgIMgFam3ZQbfrLCvHNkBMJUE0s0/7PeJFnUapUXIJ0PGaxQ+WNIkMQAPLaqO7anDa09IJKrgwlH8nYqVzcUCYUL9c7LEOTwhEryUgzQu/u1WJIVhU1kBAAvNL4oeWTIjcbIWAuRD3HV2dWheXRjeKosdktfPGC7uSq6GJOfbS97RnRe01Gy+cBZ9U1GflZKw3R4Q55drkn/nSTWyu63m3whKBOywoTk69WuH6snBRFHrEI6RgJc2pbVZhodHOGsfpF2KHIil5T3pcG6wW1ttX4NiV4XFFFpOKRQ2kBKkHeeuTPaWs1smAJtFVSiQTmb39yZqN77e1q7/RGhzVq3kLYYSxVm55BmrqSlitSHhOr3IySWCH6iOMbQz2uiPql1Yf44MrGdPI4BlquFdfYXkqS3YBH75X6v0wrQuAJEn9Srs6HBdv/Zjd8iFbPwHN/0TkyQn1C4K+gthVFkBAIpOAFw3tGakVU5TJP8Lj8aTNgfq8jO1Ff4CRlmJaLAatoPn8WmVqnyGPeFvPy1N4nTLMEUtyUru5reeC08PCUv5rqdKweqnyNyAnaewkCFzJ8JWxI9GXhsNvH+FjDP6EU9lM47Z1h4DPmQBWw6DGv3f2bgpzuj6W9y+/Ux8eKLBqJytNhEyn6niNhh3ZYFVVxpZS617bxtoM8mG9Wti0Ly5apnje6SoZPN8I/+ukLvyYYAUX90coGy28qhmID9gmXjvgV+CZ/XJPIUXVoV5SqutZ/SaIjGm6TYW7Aq9P5No6vmLwGk3ZQJDOVTVTuJpoUHzYNizhyZ9TEWMDXLgiiA=
--- KEYGEN TIME 40.03767776489258 seconds ---
```

![image-20231105154049225](https://img.cactes.com/20231105-154050-873.png)

### CMP Reshare 测试


#### B (x86_64) + A (x86_64)

```
python3 test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_b.txt
RESHARE START
calling CmpReshareInit
2023/11/05 07:29:06 INFO: ReshareInit, selfID b reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:29:07 Found msg: message: round 2, from: b, to , protocol: cmp/reshare-threshold
--- step 1 TIME 0.997626781463623 seconds ---
calling PerformRound
2023/11/05 07:29:11 Found msg: message: round 3, from: b, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.0004220008850097656 seconds ---
calling PerformRound
2023/11/05 07:29:13 Found msg: message: round 4, from: b, to , protocol: cmp/reshare-threshold 
2023/11/05 07:29:13 Found msg: message: round 4, from: b, to a, protocol: cmp/reshare-threshold
2023/11/05 07:29:13 Found msg: message: round 4, from: b, to c, protocol: cmp/reshare-threshold
--- step 3 TIME 1.8278310298919678 seconds ---
calling PerformRound
2023/11/05 07:29:15 Found msg: message: round 5, from: b, to , protocol: cmp/reshare-threshold
--- step 4 TIME 1.1032118797302246 seconds ---
calling PerformRound
--- step 5 TIME 0.002754688262939453 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 9.168818473815918 seconds ---

python3 test_client.py cmp_sign ws://192.168.192.4:8000 cmp_keyshare_a.txt
participant_id a   
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 06:42:07 Found msg: message: round 2, from: a, to , protocol: cmp/sign 
2023/11/05 06:42:07 Found msg: message: round 2, from: a, to b, protocol: cmp/sign
--- step 1 TIME 0.1288316249847412 seconds ---
calling PerformRound
2023/11/05 06:42:08 Found msg: message: round 3, from: a, to , protocol: cmp/sign
2023/11/05 06:42:08 Found msg: message: round 3, from: a, to b, protocol: cmp/sign
--- step 2 TIME 0.8737409114837646 seconds ---
calling PerformRound
root@arweave:/opt/bitizen#
root@arweave:/opt/bitizen# 
root@arweave:/opt/bitizen# 
root@arweave:/opt/bitizen# python3 test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_a.txt
RESHARE START
calling CmpReshareInit
2023/11/05 07:29:08 INFO: ReshareInit, selfID a reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:29:11 Found msg: message: round 2, from: a, to , protocol: cmp/reshare-threshold
--- step 1 TIME 3.1349294185638428 seconds ---
calling PerformRound
2023/11/05 07:29:11 Found msg: message: round 3, from: a, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.00016188621520996094 seconds ---
calling PerformRound
2023/11/05 07:29:13 Found msg: message: round 4, from: a, to , protocol: cmp/reshare-threshold 
2023/11/05 07:29:13 Found msg: message: round 4, from: a, to b, protocol: cmp/reshare-threshold
2023/11/05 07:29:13 Found msg: message: round 4, from: a, to c, protocol: cmp/reshare-threshold
--- step 3 TIME 1.964146375656128 seconds ---
calling PerformRound
2023/11/05 07:29:15 Found msg: message: round 5, from: a, to , protocol: cmp/reshare-threshold
--- step 4 TIME 1.1446735858917236 seconds ---
calling PerformRound
--- step 5 TIME 0.0015170574188232422 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 6.673508167266846 seconds ---

python3 test_client.py cmp_reshare ws://127.0.0.1:8000  
RESHARE START
calling CmpReshareInit
2023/11/05 07:29:10 INFO: ReshareInit, selfID c reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:29:11 Found msg: message: round 2, from: c, to , protocol: cmp/reshare-threshold
--- step 1 TIME 0.3999803066253662 seconds ---
calling PerformRound
2023/11/05 07:29:12 Found msg: message: round 3, from: c, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.00044155120849609375 seconds ---
calling PerformRound
2023/11/05 07:29:13 Found msg: message: round 4, from: c, to , protocol: cmp/reshare-threshold 
2023/11/05 07:29:13 Found msg: message: round 4, from: c, to a, protocol: cmp/reshare-threshold
2023/11/05 07:29:13 Found msg: message: round 4, from: c, to b, protocol: cmp/reshare-threshold
--- step 3 TIME 1.8243563175201416 seconds ---
calling PerformRound
2023/11/05 07:29:15 Found msg: message: round 5, from: c, to , protocol: cmp/reshare-threshold
--- step 4 TIME 1.0471696853637695 seconds ---
calling PerformRound
--- step 5 TIME 0.0008401870727539062 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 4.484289646148682 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_b.txt
RESHARE START
calling CmpReshareInit
2023/11/05 07:31:51 INFO: ReshareInit, selfID b reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:31:54 Found msg: message: round 2, from: b, to , protocol: cmp/reshare-threshold
--- step 1 TIME 3.7496840953826904 seconds ---
calling PerformRound
2023/11/05 07:32:03 Found msg: message: round 3, from: b, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.0010273456573486328 seconds ---
calling PerformRound
2023/11/05 07:32:04 Found msg: message: round 4, from: b, to , protocol: cmp/reshare-threshold 
2023/11/05 07:32:04 Found msg: message: round 4, from: b, to a, protocol: cmp/reshare-threshold
2023/11/05 07:32:04 Found msg: message: round 4, from: b, to c, protocol: cmp/reshare-threshold
--- step 3 TIME 1.5213656425476074 seconds ---
calling PerformRound
2023/11/05 07:32:19 Found msg: message: round 5, from: b, to , protocol: cmp/reshare-threshold
--- step 4 TIME 0.8818116188049316 seconds ---
calling PerformRound
--- step 5 TIME 0.00449061393737793 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 38.238563537597656 seconds ---

python3 test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_a.txt
RESHARE START
calling CmpReshareInit
2023/11/05 07:31:41 INFO: ReshareInit, selfID a reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:31:43 Found msg: message: round 2, from: a, to , protocol: cmp/reshare-threshold
--- step 1 TIME 1.9619805812835693 seconds ---
calling PerformRound
2023/11/05 07:32:03 Found msg: message: round 3, from: a, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.0009930133819580078 seconds ---
calling PerformRound
2023/11/05 07:32:04 Found msg: message: round 4, from: a, to , protocol: cmp/reshare-threshold 
2023/11/05 07:32:04 Found msg: message: round 4, from: a, to b, protocol: cmp/reshare-threshold
2023/11/05 07:32:04 Found msg: message: round 4, from: a, to c, protocol: cmp/reshare-threshold
--- step 3 TIME 1.4360053539276123 seconds ---
calling PerformRound
2023/11/05 07:32:19 Found msg: message: round 5, from: a, to , protocol: cmp/reshare-threshold
--- step 4 TIME 0.8631980419158936 seconds ---
calling PerformRound
--- step 5 TIME 0.002907276153564453 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 47.76490259170532 seconds ---

root@heliumbeauty-b4:/opt/bitizen# python3 test_client.py cmp_reshare ws://192.168.192.4:8000
RESHARE START
calling CmpReshareInit
2023/11/05 07:31:55 INFO: ReshareInit, selfID c reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:32:02 Found msg: message: round 2, from: c, to , protocol: cmp/reshare-threshold
--- step 1 TIME 7.7035603523254395 seconds ---
calling PerformRound
2023/11/05 07:32:02 Found msg: message: round 3, from: c, to , protocol: cmp/reshare-threshold
--- step 2 TIME 0.00446009635925293 seconds ---
calling PerformRound
2023/11/05 07:32:18 Found msg: message: round 4, from: c, to , protocol: cmp/reshare-threshold
2023/11/05 07:32:18 Found msg: message: round 4, from: c, to a, protocol: cmp/reshare-threshold
2023/11/05 07:32:18 Found msg: message: round 4, from: c, to b, protocol: cmp/reshare-threshold
--- step 3 TIME 14.728848934173584 seconds ---
calling PerformRound
2023/11/05 07:32:29 Found msg: message: round 5, from: c, to , protocol: cmp/reshare-threshold
--- step 4 TIME 11.241387367248535 seconds ---  
calling PerformRound
--- step 5 TIME 0.009467124938964844 seconds ---
calling CmpReshareResult
RESHARE END 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
--- RESHARE TIME 34.149404764175415 seconds ---
```



### FROST 签名测试


#### B (x86_64) + A (x86_64)

```
python3 test_client.py frost_sign ws://127.0.0.1:8000 frost_keyshare_b.txt
participant_id b
SIGN START
calling FrostTaprootSignInit
calling PerformRound
2023/11/05 07:37:39 Found msg: message: round 2, from: b, to , protocol: frost/sign-threshold-taproot
--- step 1 TIME 0.014138460159301758 seconds ---
calling PerformRound
2023/11/05 07:37:41 Found msg: message: round 3, from: b, to , protocol: frost/sign-threshold-taproot        
--- step 2 TIME 0.0010647773742675781 seconds ---
calling PerformRound
--- step 3 TIME 0.0009737014770507812 seconds ---
calling FrostTaprootSignResult
SIGN END WEBk63kDMB0adSa9jIV1YMXYuzraJ5L4fKvqupMBqUbcvrzbISOz47i9o1Hu5cGz1b++0ertyC4fmSQKVQZZG5n5
--- SIGN TIME 2.221835136413574 seconds ---

python3 test_client.py frost_sign ws://127.0.0.1:8000 frost_keyshare_a.txt
participant_id a
SIGN START
calling FrostTaprootSignInit
calling PerformRound
2023/11/05 07:37:41 Found msg: message: round 2, from: a, to , protocol: frost/sign-threshold-taproot
--- step 1 TIME 0.012713193893432617 seconds ---
calling PerformRound
2023/11/05 07:37:41 Found msg: message: round 3, from: a, to , protocol: frost/sign-threshold-taproot        
--- step 2 TIME 0.0005362033843994141 seconds ---
calling PerformRound
--- step 3 TIME 0.0014896392822265625 seconds ---
calling FrostTaprootSignResult
SIGN END WEBk63kDMB0adSa9jIV1YMXYuzraJ5L4fKvqupMBqUbcvrzbISOz47i9o1Hu5cGz1b++0ertyC4fmSQKVQZZG5n5
--- SIGN TIME 0.21653079986572266 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 test_client.py frost_sign ws://127.0.0.1:8000 frost_keyshare_b.txt 
participant_id b
SIGN START
calling FrostTaprootSignInit
calling PerformRound
2023/11/05 07:40:10 Found msg: message: round 2, from: b, to , protocol: frost/sign-threshold-taproot        
--- step 1 TIME 0.014165401458740234 seconds ---
calling PerformRound
2023/11/05 07:40:13 Found msg: message: round 3, from: b, to , protocol: frost/sign-threshold-taproot
--- step 2 TIME 0.002012968063354492 seconds ---
calling PerformRound
--- step 3 TIME 0.0019004344940185547 seconds ---
calling FrostTaprootSignResult
SIGN END WECS0or4PBmaCBGrhxJ3jc9W60w35htFTIV4Qx2LY+obbzjNTe/iPC9VmQJlphbO5Qool2OUaWXO+0Ln3kHmnk9m
--- SIGN TIME 3.0250813961029053 seconds ---

python3 test_client.py frost_sign ws://192.168.192.4:8000 frost_keyshare_a.txt 
participant_id a
SIGN START
calling FrostTaprootSignInit
calling PerformRound
2023/11/05 07:40:13 Found msg: message: round 2, from: a, to , protocol: frost/sign-threshold-taproot
--- step 1 TIME 0.10707211494445801 seconds ---
calling PerformRound
2023/11/05 07:40:13 Found msg: message: round 3, from: a, to , protocol: frost/sign-threshold-taproot        
--- step 2 TIME 0.006788730621337891 seconds ---
calling PerformRound
--- step 3 TIME 0.0062198638916015625 seconds ---
calling FrostTaprootSignResult
SIGN END WECS0or4PBmaCBGrhxJ3jc9W60w35htFTIV4Qx2LY+obbzjNTe/iPC9VmQJlphbO5Qool2OUaWXO+0Ln3kHmnk9m
--- SIGN TIME 0.3291943073272705 seconds ---
```

### FROST Keygen 测试


#### B (x86_64) + A (x86_64)

```
python3 test_client.py frost_keygen ws://127.0.0.1:8000 b 
KEYGEN START
calling FrostTaprootKeygenInit
calling PerformRound
2023/11/05 07:48:00 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot
--- step 1 TIME 0.015922069549560547 seconds ---
calling PerformRound
2023/11/05 07:48:00 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot      
2023/11/05 07:48:00 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.0005385875701904297 seconds ---
calling PerformRound
--- step 3 TIME 0.0004837512969970703 seconds ---
calling FrostTaprootKeygenResult
KEYGEN END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCAtrI34pDJubvzViM+/MkwlD0wc01gc0OJMa49t1kS29mlQdWJsaWNLZXlYIJitbEqZoJ8gx3eL0dxTVzXCA+5qD+s2jKtsJWGoSV6baENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOiYWFYIQIMmxRa2qxabL5dJfclMiq4/gcaZ1ZlD/nP+vo9/roO+GFiWCECUoofE+Ext3ik68RAwJ08dg5DQ+Fgg5IdkEDlVFR46gU=
--- KEYGEN TIME 0.21930384635925293 seconds ---

python3 test_client.py frost_keygen ws://127.0.0.1:8000 a
KEYGEN START
calling FrostTaprootKeygenInit
calling PerformRound
2023/11/05 07:48:00 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot
--- step 1 TIME 0.015922069549560547 seconds ---
calling PerformRound
2023/11/05 07:48:00 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot      
2023/11/05 07:48:00 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.0005385875701904297 seconds ---
calling PerformRound
--- step 3 TIME 0.0004837512969970703 seconds ---
calling FrostTaprootKeygenResult
KEYGEN END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCAtrI34pDJubvzViM+/MkwlD0wc01gc0OJMa49t1kS29mlQdWJsaWNLZXlYIJitbEqZoJ8gx3eL0dxTVzXCA+5qD+s2jKtsJWGoSV6baENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOiYWFYIQIMmxRa2qxabL5dJfclMiq4/gcaZ1ZlD/nP+vo9/roO+GFiWCECUoofE+Ext3ik68RAwJ08dg5DQ+Fgg5IdkEDlVFR46gU=
--- KEYGEN TIME 0.21930384635925293 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 test_client.py frost_keygen ws://127.0.0.1:8000 b 
KEYGEN START
calling FrostTaprootKeygenInit
calling PerformRound
2023/11/05 07:49:02 Found msg: message: round 2, from: b, to , protocol: frost/keygen-threshold-taproot
--- step 1 TIME 0.016228914260864258 seconds ---
calling PerformRound
2023/11/05 07:49:05 Found msg: message: round 3, from: b, to , protocol: frost/keygen-threshold-taproot
2023/11/05 07:49:05 Found msg: message: round 3, from: b, to a, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.002110719680786133 seconds ---
calling PerformRound
--- step 3 TIME 0.0013203620910644531 seconds ---
calling FrostTaprootKeygenResult
KEYGEN END pmJJRGFiaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCAN7BuX5k9CubcvFia0qeVBGNXPriSe3si5sBk0H8ShqWlQdWJsaWNLZXlYIBaG628yZp9b7Xru6D3MUMce8UrZCv+bRXrTOlzNiBcYaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOiYWJYIQJf1/aDY9fqn/tR8BNpfeLHwuRYjgThiqA1GB/VaOBeTGFhWCEDSaSkC7ZY+WL2x4CYkf5JP47tu/0JPq0pb5JBR+2r2q8=
--- KEYGEN TIME 3.4280714988708496 seconds ---

python3 test_client.py frost_keygen ws://192.168.192.4:8000 a   
KEYGEN START
calling FrostTaprootKeygenInit
calling PerformRound
2023/11/05 07:49:05 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot
--- step 1 TIME 0.10852599143981934 seconds ---
calling PerformRound
2023/11/05 07:49:05 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot      
2023/11/05 07:49:05 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.00734710693359375 seconds ---
calling PerformRound
--- step 3 TIME 0.0029277801513671875 seconds ---
calling FrostTaprootKeygenResult
KEYGEN END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCCRcVoAvTe/5EZzdFQTnwHyldKUOzlNy/mU/NRLWazpAWlQdWJsaWNLZXlYIBaG628yZp9b7Xru6D3MUMce8UrZCv+bRXrTOlzNiBcYaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOiYWFYIQNJpKQLtlj5YvbHgJiR/kk/ju27/Qk+rSlvkkFH7avar2FiWCECX9f2g2PX6p/7UfATaX3ix8LkWI4E4YqgNRgf1WjgXkw=
--- KEYGEN TIME 0.32875680923461914 seconds ---
```

### FROST Reshare 测试

#### B (x86_64) + A (x86_64)

```
python3 test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_b.txt 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:53:27 INFO: ReshareInit, selfID b reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:53:27 Found msg: message: round 2, from: b, to , protocol: frost/keygen-threshold-taproot      
--- step 1 TIME 0.0004525184631347656 seconds ---
calling PerformRound
2023/11/05 07:53:44 Found msg: message: round 3, from: b, to , protocol: frost/keygen-threshold-taproot
2023/11/05 07:53:44 Found msg: message: round 3, from: b, to a, protocol: frost/keygen-threshold-taproot     
2023/11/05 07:53:44 Found msg: message: round 3, from: b, to c, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.0013382434844970703 seconds ---
calling PerformRound
--- step 3 TIME 0.001074075698852539 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFiaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCBLX9F6tTg7w+IGj1ytugx79re0xwHMonyH17tTX4X7OWlQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWFYIQMKrP1cMGnw/8dz7q8Cyy67dBZ52pNv+fhlK9fMpKjTOGFiWCEDNlI+u5vvcJj+MbCbLLubiLNUlld1xnlOHHxDTUcOko9hY1ghAuM9RPB+/UMLj6WMgU3SSm1AbJVnxzuHtFdWc73c1vC4
--- RESHARE TIME 16.045639991760254 seconds ---

python3 test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_a.txt 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:53:35 INFO: ReshareInit, selfID a reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:53:35 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot      
--- step 1 TIME 0.0006227493286132812 seconds ---
calling PerformRound
2023/11/05 07:53:43 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot
2023/11/05 07:53:43 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
2023/11/05 07:53:43 Found msg: message: round 3, from: a, to c, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.0009875297546386719 seconds ---
calling PerformRound
--- step 3 TIME 0.0014462471008300781 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCBqUMEUeLvGbdmFajrIjWWFyX3JddCz6plbRxVtkI+2a2lQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWJYIQIkVvW+Qpo8F5XI1WnyRdEzDNTzq6R0fl/4dXXRRfXM2mFjWCECJ2h6kKytwv1qH99CwhzO8qRWEGSb9p3cANW8LsVIjbxhYVghAgMlXQCkpOii4XS2E7jVuV2mUTuT0sDMPGgBrB5/GzsL
--- RESHARE TIME 9.035743474960327 seconds ---

python3 test_client.py frost_reshare ws://127.0.0.1:8000 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:53:43 INFO: ReshareInit, selfID c reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:53:43 Found msg: message: round 2, from: c, to , protocol: frost/keygen-threshold-taproot 
--- step 1 TIME 0.0003631114959716797 seconds ---
calling PerformRound
2023/11/05 07:53:43 Found msg: message: round 3, from: c, to , protocol: frost/keygen-threshold-taproot 
2023/11/05 07:53:43 Found msg: message: round 3, from: c, to a, protocol: frost/keygen-threshold-taproot
2023/11/05 07:53:43 Found msg: message: round 3, from: c, to b, protocol: frost/keygen-threshold-taproot
--- step 2 TIME 0.0010528564453125 seconds ---
calling PerformRound
--- step 3 TIME 0.0008897781372070312 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFjaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCAsbuHg8bSxGeqHtH6S5rNyI/GgGDLlWl+0aGE5LnxAB2lQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWFYIQI/73Uht1f1j9zO80lszoMPF9clJXfBxnz8TfZfpntjiGFiWCEC5ApIZynyVxav8dOx2ydDajyLv5slWfou7YC3M4W9nfRhY1ghA/LGETbir3jNmeyKrKfkrz4y0EhuLs26Vf3HNyw8TzrC
--- RESHARE TIME 0.21934032440185547 seconds ---
```

#### B (x86_64) + A (aarch64)

```
python3 test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_b.txt 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:58:36 INFO: ReshareInit, selfID b reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:58:36 Found msg: message: round 2, from: b, to , protocol: frost/keygen-threshold-taproot      
--- step 1 TIME 0.00046944618225097656 seconds ---
calling PerformRound
2023/11/05 07:58:41 Found msg: message: round 3, from: b, to , protocol: frost/keygen-threshold-taproot
2023/11/05 07:58:41 Found msg: message: round 3, from: b, to a, protocol: frost/keygen-threshold-taproot     
2023/11/05 07:58:41 Found msg: message: round 3, from: b, to c, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.0025849342346191406 seconds ---
calling PerformRound
--- step 3 TIME 0.0021729469299316406 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFiaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCCX9OmGlVor+zsQ9Ld4bfFP7BHYFzMFdN4eB7Ocu3BzkGlQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWFYIQKeRYvUeWWRxlr4gHfRpxyko7VKDD/TKafBGR20QJIAJ2FiWCECNFvXmt6jgsy9r45y7b665ymlBP9SR3fmJa48PIPtKuNhY1ghAwHMRDYcqQDklTFvntVfbhk5K5YV4iXeRKZKZ1J6ImxN
--- RESHARE TIME 4.42948579788208 seconds ---

python3 test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_a.txt 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:58:38 INFO: ReshareInit, selfID a reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:58:38 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot      
--- step 1 TIME 0.0006172657012939453 seconds ---
calling PerformRound
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot      
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to c, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.002512693405151367 seconds ---
calling PerformRound
--- step 3 TIME 0.0007915496826171875 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCB/Ql4bAF/6uYfbdbvVGuIjnCxPXOZPiNMFhZEK8I4fjGlQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWNYIQKhsay7v7FLx3XmnHZKNeo7VqkwxfMhpOH9xNrzH4Aig2FhWCEDenOiKrMxyFl7unVVCiZEVSFx54pRbdMAhPd7llazQbZhYlghA3pYV0GvJcbooNnftvE0o3v79cn04lqHksLyU1rKbsG3
--- RESHARE TIME 3.0219297409057617 seconds ---

python3 test_client.py frost_reshare ws://192.168.192.4:8000 
RESHARE START
calling FrostTaprootReshareInit
2023/11/05 07:58:38 INFO: ReshareInit, selfID a reshareParticipants [{a a} {b b} {c }] threshold 1
calling PerformRound
2023/11/05 07:58:38 Found msg: message: round 2, from: a, to , protocol: frost/keygen-threshold-taproot      
--- step 1 TIME 0.0006172657012939453 seconds ---
calling PerformRound
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to , protocol: frost/keygen-threshold-taproot      
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to b, protocol: frost/keygen-threshold-taproot     
2023/11/05 07:58:40 Found msg: message: round 3, from: a, to c, protocol: frost/keygen-threshold-taproot     
--- step 2 TIME 0.002512693405151367 seconds ---
calling PerformRound
--- step 3 TIME 0.0007915496826171875 seconds ---
calling FrostTaprootReshareResult
RESHARE END pmJJRGFhaVRocmVzaG9sZAFsUHJpdmF0ZVNoYXJlWCB/Ql4bAF/6uYfbdbvVGuIjnCxPXOZPiNMFhZEK8I4fjGlQdWJsaWNLZXlYINu4Yl0qlDVIsEAcvKh8PBlC/+gNSigJhDC+lshyZ9pxaENoYWluS2V59nJWZXJpZmljYXRpb25TaGFyZXOjYWNYIQKhsay7v7FLx3XmnHZKNeo7VqkwxfMhpOH9xNrzH4Aig2FhWCEDenOiKrMxyFl7unVVCiZEVSFx54pRbdMAhPd7llazQbZhYlghA3pYV0GvJcbooNnftvE0o3v79cn04lqHksLyU1rKbsG3
--- RESHARE TIME 3.0219297409057617 seconds ---
```

## 其他

单独执行客户端超时退出（预期中）

```
root@x86_64:/opt/bitizen# python3 test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_b.txt
participant_id b
SIGN START
calling CmpSignInit
calling PerformRound
2023/11/05 05:39:59 Found msg: message: round 2, from: b, to , protocol: cmp/sign
2023/11/05 05:39:59 Found msg: message: round 2, from: b, to a, protocol: cmp/sign
--- step 1 TIME 0.12831592559814453 seconds ---
Traceback (most recent call last):
  File "test_client.py", line 503, in <module>
    test_sign(prot, participant_id, keyshare_for_sign, bulletin_board)
  File "test_client.py", line 454, in test_sign
    result = sign(prot, ctx_id, participant_id, ["a", "b"], keyshare_for_sign, msg_hash_base64, bulletin_board)
  File "test_client.py", line 369, in sign
    next_input = get_next_input(ctx_id, self_id, participants, step, has_broadcast, has_p2p, bulletin_board) 
  File "test_client.py", line 269, in get_next_input
    data = poll_data(key, bulletin_board)
  File "test_client.py", line 292, in poll_data
    raise ValueError("No data found for key " + key)
ValueError: No data found for key 201234567890-2-True-a-
```

