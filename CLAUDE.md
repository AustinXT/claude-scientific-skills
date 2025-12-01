# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 项目环境信息

- **Git代码托管平台**：github.com
- **版本管理**：采用语义版本号管理方法，当前为 v0.0.1

## 常用命令

### 技能开发和管理
- 技能文档位于 `scientific-skills/` 目录下的各个子目录
- 每个技能包含 `SKILL.md` 文档和相关示例代码
- 技能测试和验证通过 Claude Code 自动进行

### 依赖管理
- 使用 `uv` 管理 Python 环境
- 安装新的技能依赖：`uv pip install package-name`
- 验证 uv 安装：`uv --version`

### 文档生成
- 主要文档：`README.zh.md`（中文版）和 `README.md`（英文版）
- 技能参考文档：`docs/scientific-skills.md`
- 示例文档：`docs/examples.md`

## 项目架构

### 核心目录结构

- **scientific-skills/**: 包含 123+ 个科学技能，按领域分类
  - **document-skills/**: 文档处理技能（PDF、PPTX、DOCX、XLSX）
  - **metabolomics-workbench-database/**: 代谢组学数据库访问技能
  - **biopython/**: 生物信息学序列分析
  - **rdkit/**: 化学信息学和分子操作
  - **scanpy/**: 单细胞 RNA 序列数据分析
  - **torchdrug/**: 药物发现和深度学习
  - 以及 120+ 其他专业技能

### 技能分类

#### 🧬 生物信息学和基因组学（15+ 技能）
- 序列分析：BioPython、pysam、scikit-bio
- 单细胞分析：Scanpy、AnnData、scvi-tools、Arboreto
- 基因组工具：gget、geniml、gtars、deepTools

#### 🧪 化学信息学和药物发现（10+ 技能）
- 分子操作：RDKit、Datamol、Molfeat
- 深度学习：DeepChem、TorchDrug
- 对接和筛选：DiffDock

#### 🏥 临床研究与精准医学（8+ 技能）
- 临床数据库：ClinicalTrials.gov、ClinVar、ClinPGx、COSMIC
- 医疗保健人工智能：PyHealth、NeuroKit2

#### 🤖 机器学习和人工智能（15+ 技能）
- 深度学习：PyTorch Lightning、Transformers、Stable Baselines3
- 经典机器学习：scikit-learn、scikit-survival、SHAP
- 贝叶斯方法：PyMC

#### 📊 数据分析和可视化（10+ 技能）
- 可视化：Matplotlib、Seaborn、Plotly
- 网络分析：NetworkX
- PDF 生成：ReportLab

## 开发指南

### 技能开发标准
每个技能必须包含：
- `SKILL.md` 文件：完整的技能文档，包含：
  - YAML 前置元数据（name, description）
  - 概述和使用场景
  - 核心功能和示例代码
  - 常见工作流程
  - 最佳实践和资源
- 实用的代码示例和用例
- 集成指南和最佳实践
- 相关参考资料

### 新技能开发流程
1. 在适当的分类目录下创建新技能目录
2. 编写完整的 `SKILL.md` 文档
3. 提供实用的代码示例
4. 确保遵循现有文档格式和模式
5. 测试所有示例和工作流程
6. 提交 PR 并明确描述变更

### 技能使用示例

#### 药物发现工作流
```
Use available skills you have access to whenever possible. Query ChEMBL for EGFR inhibitors (IC50 < 50nM), analyze structure-activity relationships
with RDKit, generate improved analogs with datamol, perform virtual screening with DiffDock
against AlphaFold EGFR structure, search PubMed for resistance mechanisms, check COSMIC for
mutations, and create visualizations and a comprehensive report.
```

#### 单细胞 RNA-seq 分析
```
Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene
Census data, identify cell types using NCBI Gene markers, run differential expression with
PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG,
and identify therapeutic targets with Open Targets.
```

### 环境配置
- Python 技能需要安装相应的依赖包
- 使用 `uv` 进行依赖管理：`uv pip install package-name`
- 数据库技能需要网络连接访问 API
- 部分 API 可能需要身份验证密钥

### 版本管理策略
- 首次版本：v0.0.1
- 重大功能变更时创建新 tag
- 所有重要变动需要创建 tag
- 语义版本号管理

### 技能维护
- 定期更新技能以反映最新版本的软件包和 API
- 检查和更新过时的示例和文档
- 确保所有代码示例经过测试且功能正常
- 遵循科学最佳实践

## 语言设置
- 所有沟通和回复使用中文
- 文档和注释优先使用中文
- 技能文档提供中英双语版本（如适用）
