---
name: reactome-database
description: "查询 Reactome REST API 进行通路分析、富集、基因-通路映射、疾病通路、分子相互作用、表达分析，用于系统生物学研究。"
---

# Reactome Database

## 概述

Reactome 是一个免费的、开源的精选通路数据库，包含 2,825+ 个人类通路。通过 REST API 和 Python 客户端查询生物通路、执行过表达和表达分析、将基因映射到通路、通过 REST API 探索分子相互作用，用于系统生物学研究。

## 何时使用此技能

此技能应该用于：
- 对基因或蛋白质列表执行通路富集分析
- 分析基因表达数据以识别相关的生物通路
- 查询特定通路信息、反应或分子相互作用
- 将基因或蛋白质映射到生物通路和过程
- 探索疾病相关通路和机制
- 在 Reactome Pathway Browser 中可视化分析结果
- 进行跨物种比较通路分析

## 核心功能

Reactome 提供两个主要的 API 服务和一个 Python 客户端库：

### 1. 内容服务 - 数据检索

查询和检索生物通路数据、分子相互作用和实体信息。

**常见操作：**
- 检索通路信息和层次结构
- 查询特定实体（蛋白质、反应、复合物）
- 获取通路中的参与分子
- 访问数据库版本和元数据
- 探索通路区域和位置

**API 基础 URL：** `https://reactome.org/ContentService`

### 2. 分析服务 - 通路分析

对基因列表和表达数据执行计算分析。

**分析类型：**
- **过表达分析**：从基因/蛋白质列表中识别统计学显著的通路
- **表达数据分析**：分析基因表达数据集以查找相关通路
- **物种比较**：比较不同生物体的通路数据

**API 基础 URL：** `https://reactome.org/AnalysisService`

### 3. reactome2py Python 包

包装 Reactome API 调用以便于程序化访问的 Python 客户端库。

**安装：**
```bash
uv pip install reactome2py
```

**注意：** reactome2py 包（版本 3.0.0，2021年1月发布）功能正常但未积极维护。为获得最新的功能，考虑直接使用 REST API 调用。

## 查询通路数据

### 使用内容服务 REST API

内容服务使用 REST 协议并以 JSON 或纯文本格式返回数据。

**获取数据库版本：**
```python
import requests

response = requests.get("https://reactome.org/ContentService/data/database/version")
version = response.text
print(f"Reactome 版本: {version}")
```

**查询特定实体：**
```python
import requests

entity_id = "R-HSA-69278"  # 示例通路 ID
response = requests.get(f"https://reactome.org/ContentService/data/query/{entity_id}")
data = response.json()
```

**获取通路中的参与分子：**
```python
import requests

event_id = "R-HSA-69278"
response = requests.get(
    f"https://reactome.org/ContentService/data/event/{event_id}/participatingPhysicalEntities"
)
molecules = response.json()
```

### 使用 reactome2py 包

```python
import reactome2py
from reactome2py import content

# 查询通路信息
pathway_info = content.query_by_id("R-HSA-69278")

# 获取数据库版本
version = content.get_database_version()
```

**有关详细的 API 端点和参数**，请参考此技能中的 `references/api_reference.md`。

## 执行通路分析

### 过表达分析

提交基因/蛋白质标识符列表以查找富集的通路。

**使用 REST API：**
```python
import requests

# 准备标识符列表
identifiers = ["TP53", "BRCA1", "EGFR", "MYC"]
data = "\n".join(identifiers)

# 提交分析
response = requests.post(
    "https://reactome.org/AnalysisService/identifiers/",
    headers={"Content-Type": "text/plain"},
    data=data
)

result = response.json()
token = result["summary"]["token"]  # 保存 token 以便稍后检索结果

# 访问通路
for pathway in result["pathways"]:
    print(f"{pathway['stId']}: {pathway['name']} (p-value: {pathway['entities']['pValue']})")
```

**按 token 检索分析：**
```python
# Token 有效期为 7 天
response = requests.get(f"https://reactome.org/AnalysisService/token/{token}")
results = response.json()
```

### 表达数据分析

使用定量值分析基因表达数据集。

**输入格式（以 # 开头的 TSV 格式）：**
```
#Gene	样本1	样本2	样本3
TP53	2.5	3.1	2.8
BRCA1	1.2	1.5	1.3
EGFR	4.5	4.2	4.8
```

**提交表达数据：**
```python
import requests

# 读取 TSV 文件
with open("expression_data.tsv", "r") as f:
    data = f.read()

response = requests.post(
    "https://reactome.org/AnalysisService/identifiers/",
    headers={"Content-Type": "text/plain"},
    data=data
)

result = response.json()
```

### 物种映射

使用 `/projection/` 端点将标识符专门映射到人类通路：

```python
response = requests.post(
    "https://reactome.org/AnalysisService/identifiers/projection/",
    headers={"Content-Type": "text/plain"},
    data=data
)
```

## 可视化结果

可以通过构造带有分析 token 的 URL 在 Reactome Pathway Browser 中可视化分析结果：

```python
token = result["summary"]["token"]
pathway_id = "R-HSA-69278"
url = f"https://reactome.org/PathwayBrowser/#{pathway_id}&TAB=ANALYSIS&ANALYSIS={token}"
print(f"查看结果: {url}")
```

## 使用分析 Token

- 分析 token 有效期为 **7 天**
- Token 允许检索以前计算的结果而无需重新提交
- 存储 token 以跨会话访问结果
- 使用 `GET /token/{TOKEN}` 端点检索结果

## 数据格式和标识符

### 支持的标识符类型

Reactome 接受各种标识符格式：
- UniProt 登录号（例如，P04637）
- 基因符号（例如，TP53）
- Ensembl ID（例如，ENSG00000141510）
- Entrez Gene ID（例如，7157）
- 小分子的 ChEBI ID

系统会自动检测标识符类型。

### 输入格式要求

**对于过表达分析：**
- 标识符的纯文本列表（每行一个）
- 或 TSV 格式的单列

**对于表达分析：**
- 以 "#" 开头的强制性标题行的 TSV 格式
- 第 1 列：标识符
- 第 2+ 列：数值表达值
- 使用句点 (.) 作为小数分隔符

### 输出格式

所有 API 响应返回包含以下内容的 JSON：
- `pathways`：具有统计指标的富集通路数组
- `summary`：分析元数据和 token
- `entities`：已匹配和未匹配的标识符
- 统计值：pValue、FDR（错误发现率）

## 辅助脚本

此技能包括 `scripts/reactome_query.py`，一个用于常见 Reactome 操作的辅助脚本：

```bash
# 查询通路信息
python scripts/reactome_query.py query R-HSA-69278

# 执行过表达分析
python scripts/reactome_query.py analyze gene_list.txt

# 获取数据库版本
python scripts/reactome_query.py version
```

## 其他资源

- **API 文档**：https://reactome.org/dev
- **用户指南**：https://reactome.org/userguide
- **文档门户**：https://reactome.org/documentation
- **数据下载**：https://reactome.org/download-data
- **reactome2py 文档**：https://reactome.github.io/reactome2py/

有关全面的 API 端点文档，请参见此技能中的 `references/api_reference.md`。

## 当前数据库统计（版本 94，2025年9月）

- 2,825 个人类通路
- 16,002 个反应
- 11,630 个蛋白质
- 2,176 个小分子
- 1,070 个药物
- 41,373 篇文献参考