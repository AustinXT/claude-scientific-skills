---
name: qiskit
description: 用于构建、优化和执行量子电路的综合量子计算工具包。在使用量子算法、模拟或量子硬件时使用，包括：(1) 使用门和测量构建量子电路，(2) 运行量子算法（VQE、QAOA、Grover），(3) 为硬件转译/优化电路，(4) 在 IBM Quantum 或其他提供商上执行，(5) 量子化学和材料科学，(6) 量子机器学习，(7) 可视化电路和结果，或 (8) 任何量子计算开发任务。
---

# Qiskit

## 概述

Qiskit 是世界上最受欢迎的开源量子计算框架，拥有 1300 万次下载。构建量子电路，为硬件优化，在模拟器或真实量子计算机上执行，并分析结果。支持 IBM Quantum（100+ 量子比特系统）、IonQ、Amazon Braket 和其他提供商。

**主要特性：**
- 比竞争对手快 83 倍的转译
- 优化电路中的双量子比特门减少 29%
- 后端无关执行（本地模拟器或云硬件）
- 用于优化、化学和 ML 的综合算法库

## 快速开始

### 安装

```bash
uv pip install qiskit
uv pip install "qiskit[visualization]" matplotlib
```

### 第一个电路

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# 创建贝尔态（纠缠量子比特）
qc = QuantumCircuit(2)
qc.h(0)           # 在量子比特 0 上应用 Hadamard
qc.cx(0, 1)       # 从量子比特 0 到 1 的 CNOT
qc.measure_all()    # 测量两个量子比特

# 本地运行
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': ~512, '11': ~512}
```

### 可视化

```python
from qiskit.visualization import plot_histogram

qc.draw('mpl')           # 电路图
plot_histogram(counts)   # 结果直方图
```

## 核心功能

### 1. 设置和安装
有关详细的安装、身份验证和 IBM Quantum 账户设置：
- **参见 `references/setup.md`**

涵盖的主题：
- 使用 uv 安装
- Python 环境设置
- IBM Quantum 账户和 API 令牌配置
- 本地 vs 云执行

### 2. 构建量子电路
有关使用门、测量和组合构建量子电路：
- **参见 `references/circuits.md`**

涵盖的主题：
- 使用 QuantumCircuit 创建电路
- 单量子比特门（H、X、Y、Z、旋转、相位门）
- 多量子比特门（CNOT、SWAP、Toffoli）
- 测量和屏障
- 电路组合和属性
- 变分算法的参数化电路

### 3. 原语（Sampler 和 Estimator）
有关执行量子电路和计算结果：
- **参见 `references/primitives.md`**

涵盖的主题：
- **Sampler**：获取比特串测量和概率分布
- **Estimator**：计算可观测量子的期望值
- V2 接口（StatevectorSampler、StatevectorEstimator）
- IBM Quantum Runtime 的硬件原语
- 会话和批处理模式
- 参数绑定

### 4. 转译和优化
有关为硬件执行优化电路：
- **参见 `references/transpilation.md`**

涵盖的主题：
- 为什么需要转译
- 优化级别（0-3）
- 六个转译阶段（init、layout、routing、translation、optimization、scheduling）
- 高级特性（虚拟量子比特消除、门取消）
- 常见参数（initial_layout、approximation_degree、seed）