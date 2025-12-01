---
name: qutip
description: "使用 QuTiP（Python 中的量子工具箱）进行量子力学模拟和分析。在处理量子系统时使用，包括：(1) 量子态（kets、bras、密度矩阵），(2) 量子算符和门，(3) 时间演化动力学（薛定谔、主方程、蒙特卡洛），(4) 具有耗散的开放量子系统，(5) 量子测量和纠缠，(6) 可视化（布洛赫球、维格纳函数），(7) 稳态和关联函数，或 (8) 高级方法（Floquet 理论、HEOM、随机求解器）。处理量子光学、量子计算和凝聚态物理等各个领域的闭合和开放量子系统。"
---

# QuTiP：Python 中的量子工具箱

## 概述

QuTiP 提供用于模拟和分析量子力学系统的综合工具。它处理闭合（幺正）和开放（耗散）量子系统，具有针对不同场景优化的多个求解器。

## 安装

```bash
uv pip install qutip
```

可选包用于额外功能：

```bash
# 量子信息处理（电路、门）
uv pip install qutip-qip

# 量子轨迹查看器
uv pip install qutip-qt
```

## 快速开始

```python
from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# 创建量子态
psi = basis(2, 0)  # |0⟩ 态

# 创建算符
H = sigmax()  # 哈密顿量

# 时间演化
tlist = np.linspace(0, 10, 100)
result = sesolve(H, psi, tlist, e_ops=[sigmax()])

# 绘制结果
plt.plot(tlist, result.expect[0])
plt.xlabel('时间')
plt.ylabel('⟨σz⟩')
plt.show()
```

## 核心功能

### 1. 量子对象和态

创建和操作量子态和算符：

```python
# 态
psi = basis(N, n)     # Fock 态 |n⟩
psi = coherent(N, alpha)  # 相干态 |α⟩
rho = thermal_dm(N, n_avg)  # 热密度矩阵

# 算符
a = destroy(N)        # 湮灭算符
n = num(N)           # 数算符
sx, sy, sz = sigmax(), sigmay(), sigmaz()  # 泡利矩阵

# 复合系统
psi_AB = tensor(psi_A, psi_B)  # 张量积
```

**参见** `references/core_concepts.md` 了解量子对象、态和算符的综合覆盖。

### 2. 时间演化和动力学

针对不同场景的多个求解器：

```python
# 闭合系统（幺正演化）
result = sesolve(H, psi0, tlist, e_ops=[num(N)])

# 开放系统（耗散）
c_ops = [np.sqrt(0.1) * destroy(N)]  # 坍缩算符
result = mesolve(H, psi0, tlist, c_ops, e_ops=[num(N)])

# 量子轨迹（蒙特卡洛）
result = mcsolve(H, psi0, tlist, c_ops, ntraj=500, e_ops=[num(N)])
```

**求解器选择指南：**
- `sesolve`：纯态、幺正演化
- `mesolve`：混合态、一般开放系统
- `mcsolve`：量子跳跃、光子计数、个体轨迹
- `brmesolve`：弱系统-浴耦合
- `fmmesolve`：含时哈密顿量（Floquet）

**参见** `references/time_evolution.md` 了解详细求解器文档、含时哈密顿量和高级选项。

### 3. 分析和测量