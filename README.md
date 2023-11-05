# 准备工作
在执行 python 脚本前，请在各个测试系统中先安装 Python 依赖：
```
python -m pip install websockets
python -m pip install requests websocket-client
```

# CMP 协议测试
## CMP 签名测试
CMP 签名测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开两个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_b.txt         # 机器 B 终端 2 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py cmp_sign ws://127.0.0.1:8000 cmp_keyshare_a.txt         # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如输出：
```
SIGN END omFSWCECKBR/PQYKpg89OBEdHPNM5AlzWbKbwys6ADevFOcR3gVhU1ggkhsL8HFUL1APrNjkR1mxrGuqRYEUM/E3Vnvx8TRkgi4=
--- SIGN TIME 3.252570867538452 seconds --
```

## CMP Keygen 测试
CMP Keygen 测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开两个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py cmp_keygen ws://127.0.0.1:8000 b         # 机器 B 终端 2 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py cmp_keygen ws://127.0.0.1:8000 a         # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如：
```
--- KEYGEN TIME 7.124267101287842 seconds --
```

## CMP Reshare 测试
CMP Reshare 测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开三个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_b.txt         # 机器 B 终端 2 中执行
python test_client.py cmp_reshare ws://127.0.0.1:8000 cmp_keyshare_a.txt         # 机器 B 终端 3 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py cmp_reshare ws://127.0.0.1:8000                   # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如：
```
--- RESHARE TIME 7.796919107437134 seconds --
```


# FROST 协议测试
## FROST 签名测试
FROST 签名测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开两个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py frost_sign ws://127.0.0.1:8000 frost_keyshare_b.txt         # 机器 B 终端 2 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py frost_sign ws://127.0.0.1:8000 frost_keyshare_a.txt         # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如输出：
```
SIGN END omFSWCECKBR/PQYKpg89OBEdHPNM5AlzWbKbwys6ADevFOcR3gVhU1ggkhsL8HFUL1APrNjkR1mxrGuqRYEUM/E3Vnvx8TRkgi4=
--- SIGN TIME 0.22266817092895508 seconds --
```

## FROST Keygen 测试
FROST Keygen 测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开两个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py frost_keygen ws://127.0.0.1:8000 b         # 机器 B 终端 2 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py frost_keygen ws://127.0.0.1:8000 a         # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如：
```
--- KEYGEN TIME 0.22201013565063477 seconds --
```

## FROST Reshare 测试
FROST Reshare 测试步骤：

假设有两台机器：A（ARM Linux）和 B（X86 Linux）

测试步骤：
第一步，在机器 B 上打开三个终端，分别执行：
```
python ws_server.py 8000    # 机器 B 终端 1 中执行
python test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_b.txt         # 机器 B 终端 2 中执行
python test_client.py frost_reshare ws://127.0.0.1:8000 frost_keyshare_a.txt         # 机器 B 终端 3 中执行
```

第二步，在机器 A 上执行（这个命令需要当机器 B 上执行命令后，马上执行。机器 A 上命令和机器 B 上命令的执行时间不能相差 20 秒，否则会失败。如果失败则杀死前面测试进程，重新开始）：
```
python test_client.py frost_reshare ws://127.0.0.1:8000                   # 机器 A 中执行
```

结束后，在机器 A（不是机器 B，因为机器 B 中代码先执行，首轮有额外的等待时间）上查看执行时间，如：
```
--- RESHARE TIME 0.2241520881652832 seconds --
```

