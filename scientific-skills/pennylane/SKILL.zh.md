---
name: pennylane
description: 用于量子计算、量子机器学习和量子化学的跨平台 Python 库。支持构建和训练具有自动微分的量子电路，与 PyTorch/JAX/TensorFlow 无缝集成，以及跨模拟器和量子硬件（IBM、Amazon Braket、Google、Rigetti、IonQ）的设备无关执行。在处理量子电路、变分量子算法（VQE、QAOA）、量子神经网络、混合量子-经典模型、分子模拟、量子化学计算，或任何需要基于梯度的优化、硬件不可知编程或量子机器学习工作流程的量子计算任务时使用。
---

# PennyLane

## 概述

PennyLane 是一个量子计算库，能够像训练神经网络一样训练量子计算机。它提供量子电路的自动微分、设备无关的编程，以及与经典机器学习框架的无缝集成。

## 安装

使用 uv 安装：
```bash
uv pip install pennylane
```

对于量子硬件访问，安装设备插件：
```bash
# IBM Quantum
uv pip install pennylane-qiskit

# Amazon Braket
uv pip install amazon-braket-pennylane-plugin

# Google Cirq
uv pip install pennylane-cirq

# Rigetti Forest
uv pip install pennylane-rigetti

# IonQ
uv pip install pennylane-ionq
```

## 快速开始

构建量子电路并优化其参数：

```python
import pennylane as qml
from pennylane import numpy as np

# 创建设备
dev = qml.device('default.qubit', wires=2)

# 定义量子电路
@qml.qnode(dev)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# 优化参数
opt = qml.GradientDescentOptimizer(stepsize=0.1)
params = np.array([0.1, 0.2], requires_grad=True)

for i in range(100):
    params = opt.step(circuit, params)
```

## 核心功能

### 1. 量子电路构建

使用门、测量和态准备构建电路。参见 `references/quantum_circuits.md` 了解：
- 单量子比特和多量子比特门
- 受控操作和条件逻辑
- 中电路测量和自适应电路
- 各种测量类型（期望值、概率、样本）
- 电路检查和调试

### 2. 量子机器学习

创建混合量子-经典模型。参见 `references/quantum_ml.md` 了解：
- 与 PyTorch、JAX、TensorFlow 集成
- 量子神经网络和变分分类器
- 数据编码策略（角度、幅度、基、IQP）
- 使用反向传播训练混合模型
- 具有量子电路的迁移学习

### 3. 量子化学

模拟分子并计算基态能量。参见 `references/quantum_chemistry.md` 了解：
- 分子哈密顿量生成
- 变分量子本征求解器 (VQE)
- 用于化学的 UCCSD ansatz
- 几何优化和解离曲线
- 分子性质计算

### 4. 设备管理

在模拟器或量子硬件上执行。参见 `references/devices_backends.md` 了解：
- 内置模拟器（default.qubit、lightning.qubit、default.mixed）
- 硬件插件（IBM、Amazon Braket、Google、Rigetti、IonQ）
- 设备选择和配置