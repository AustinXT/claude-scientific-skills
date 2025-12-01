<!-- 此文件由机器翻译自 README.md -->

# 克劳德的科学技能

[![许可证：麻省理工学院](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![技能](https://img.shields.io/badge/Skills-123-brightgreen.svg)](#whats-included)

由 K-Dense 团队为 Claude 创建的 **123 多项即用型科学技能**的综合集合。将 Claude 转变为您的人工智能研究助理，能够执行生物学、化学、医学等领域复杂的多步骤科学工作流程。

这些技能使克劳德能够与跨多个科学领域的专业科学图书馆、数据库和工具无缝合作：
- 🧬 生物信息学和基因组学 - 序列分析、单细胞 RNA-seq、基因调控网络、变异注释、系统发育分析
- 🧪 化学信息学和药物发现 - 分子特性预测、虚拟筛选、ADMET 分析、分子对接、先导化合物优化
- 🔬 蛋白质组学和质谱分析 - LC-MS/MS 处理、肽鉴定、光谱匹配、蛋白质定量
- 🏥 临床研究和精准医学 - 临床试验、药物基因组学、变异解释、药物安全性、精准治疗
- 🧠 医疗保健人工智能和临床机器学习 - EHR 分析、生理信号处理、医学成像、临床预测模型
- 🖼️ 医学成像和数字病理学 - DICOM 处理、全幻灯片图像分析、计算病理学、放射学工作流程
- 🤖 机器学习和人工智能 - 深度学习、强化学习、时间序列分析、模型可解释性、贝叶斯方法
- 🔮 材料科学与化学 - 晶体结构分析、相图、代谢建模、计算化学
- 🌌 物理与天文学 - 天文数据分析、坐标变换、宇宙学计算、符号数学、物理计算
- ⚙️ 工程与模拟 - 离散事件模拟、多目标优化、代谢工程、系统建模、过程优化
- 📊 数据分析和可视化 - 统计分析、网络分析、时间序列、出版质量的数据、大规模数据处理
- 🧪 实验室自动化 - 液体处理方案、实验室设备控制、工作流程自动化、LIMS 集成
- 📚 科学传播 - 文献综述、同行评审、科学写作、文档处理、出版工作流程
- 🔬 多组学和系统生物学 - 多模式数据集成、路径分析、网络生物学、系统级见解
- 🧬 蛋白质工程与设计 - 蛋白质语言模型、结构预测、序列设计、功能注释

**将 Claude Code 转变为桌面上的“人工智能科学家”！**

> 💼 如需更高级的功能、计算基础设施和企业级产品，请查看 [k-dense.ai](https://k-dense.ai/)。

> ⭐ **如果您发现此存储库有用**，请考虑给它一颗星！它可以帮助其他人发现这些工具，并鼓励我们继续维护和扩展这个集合。

---

## 📦 包含什么

该存储库提供**123+ 科学技能**，分为以下类别：

- **26+ 科学数据库** - 直接 API 访问 OpenAlex、PubMed、ChEMBL、UniProt、COSMIC、ClinicalTrials.gov 等
- **52+ Python 包** - RDKit、Scanpy、PyTorch Lightning、scikit-learn、BioPython、GeoPandas 等
- **15+ 科学集成** - Benchling、DNAnexus、LatchBio、OMERO、Protocols.io 等
- **20 多种分析和交流工具** - 文献综述、科学写作、同行评审、文档处理

每个技能包括：
- ✅ 综合文档 (`SKILL.md`)
- ✅ 实用的代码示例
- ✅ 使用案例和最佳实践
- ✅ 集成指南
- ✅ 参考资料

---

## 📋 目录

- [包含内容](#whats-included)
- [为什么使用这个？](#why-use-this)
- [入门](#getting-started)
  - [克劳德代码](#claude-code-推荐)
  - [光标IDE](#cursor-ide)
  - [任何 MCP 客户端](#any-mcp-client)
- [先决条件](#先决条件)
- [快速示例](#quick-examples)
- [用例](#use-cases)
- [可用技能](#available-skills)
- [贡献](#contributing)
- [疑难解答](#疑难解答)
- [常见问题解答](#faq)
- [支持](#support)
- [加入我们的社区](#join-our-community)
- [引文](#引文)
- [许可证](#license)

---

## 🚀 为什么使用这个？

### ⚡ **加速您的研究**
- **节省工作时间** - 跳过 API 文档研究和集成设置
- **生产就绪代码** - 遵循科学最佳实践的经过测试、验证的示例
- **多步骤工作流程** - 使用单个提示执行复杂的管道

### 🎯 **全面覆盖**
- **123+ 技能** - 广泛覆盖所有主要科学领域
- **26+ 数据库** - 直接访问 OpenAlex、PubMed、ChEMBL、UniProt、COSMIC 等
- **52+ Python 包** - RDKit、Scanpy、PyTorch Lightning、scikit-learn、GeoPandas 等

### 🔧 **轻松集成**
- **一键安装** - 通过 Claude Code 或 MCP 服务器安装
- **自动发现** - 克劳德自动发现并使用相关技能
- **有据可查** - 每项技能都包括示例、用例和最佳实践

### 🌟 **维护和支持**
- **定期更新** - 由 K-Dense 团队持续维护和扩展
- **社区驱动** - 具有积极社区贡献的开源
- **企业就绪** - 可满足高级需求的商业支持

---

## 🎯 开始使用

选择您喜欢的平台来开始：

### 🖥️克劳德代码（推荐）

> 📚 **Claude Code 新手？** 查看 [Claude Code 快速入门指南](https://docs.claude.com/en/docs/claude-code/quickstart) 开始使用。

**第 1 步：安装克劳德代码**

**苹果系统：**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows：**
<<<代码块_1>>>

**第 2 步：注册市场**

<<<代码块_2>>>

**第3步：安装技能**

1.打开克劳德代码
2. 选择**浏览并安装插件**
3. 选择**克劳德科学技能**
4. 选择**科学技能**
5. 单击“**立即安装**”

**就是这样！** 当您描述您的科学任务时，克劳德将自动使用适当的技能。确保保持技能最新！

---

### ⌨️ 光标 IDE

通过我们托管的 MCP 服务器进行一键安装：

<a href="https://cursor.com/en-US/install-mcp?name=claude-scientific-skills&config=eyJ1cmwiOiJodHRwczovL21jcC5rLWRlbnNlLmFpL2NsYXVkZS1zY2llbnRpZmljLXNraWxscy9tY3AifQ%3D%3D">
  <图片>
    <source srcset="https://cursor.com/deeplink/mcp-install-light.svg" media="(prefers-color-scheme: dark)">
    <source srcset="https://cursor.com/deeplink/mcp-install-dark.svg" media="(prefers-color-scheme: light)">
    <img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="安装 MCP 服务器" style="height:2.7em;"/>
  </图片>
</a>

---

### 🔌 任何 MCP 客户端

在任何 MCP 兼容客户端（ChatGPT、Google ADK、OpenAI Agent SDK 等）中通过我们的 MCP 服务器访问所有技能：

**选项 1：托管 MCP 服务器**（最简单）
<<<代码块_3>>>

**选项 2：自托管**（更多控制）
🔗 **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - 部署您自己的 MCP 服务器

---

## ⚙️ 先决条件

- **Python**：3.9+（建议使用 3.12+ 以获得最佳兼容性）
- **uv**：Python 包管理器（安装技能依赖项所需）
- **客户端**：Claude Code、Cursor 或任何 MCP 兼容客户端
- **系统**：带有 WSL2 的 macOS、Linux 或 Windows
- **依赖关系**：由个人技能自动处理（检查`SKILL.md`文件以了解具体要求）

### 安装 uv

这些技能使用 `uv` 作为安装 Python 依赖项的包管理器。按照适用于您的操作系统的说明进行安装：

**macOS 和 Linux：**
<<<代码块_4>>>

**Windows：**
<<<代码块_5>>>

**替代方案（通过点）：**
<<<代码块_6>>>

安装后，通过运行验证其是否有效：
```bash
uv --version
```

有关更多安装选项和详细信息，请访问[官方 uv 文档](https://docs.astral.sh/uv/)。

---

## 💡 简单示例

一旦您安装了技能，您就可以要求 Claude 执行复杂的多步骤科学工作流程。以下是一些提示示例：

### 🧪 药物发现管道
**目标**：寻找用于肺癌治疗的新型 EGFR 抑制剂

**提示**：
```
Use available skills you have access to whenever possible. Query ChEMBL for EGFR inhibitors (IC50 < 50nM), analyze structure-activity relationships 
with RDKit, generate improved analogs with datamol, perform virtual screening with DiffDock 
against AlphaFold EGFR structure, search PubMed for resistance mechanisms, check COSMIC for 
mutations, and create visualizations and a comprehensive report.
```

**使用的技能**：ChEMBL、RDKit、datamol、DiffDock、AlphaFold DB、PubMed、COSMIC、科学可视化

---

### 🔬 单细胞 RNA-seq 分析
**目标**：通过公共数据集成对 10X Genomics 数据进行全面分析

**提示**：
```
Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene 
Census data, identify cell types using NCBI Gene markers, run differential expression with 
PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG, 
and identify therapeutic targets with Open Targets.
```

**使用的技能**：Scanpy、Cellxgene Census、NCBI Gene、PyDESeq2、Arboreto、Reactome、KEGG、Open Targets

---

### 🧬 多组学生物标志物发现
**目标**：整合 RNA 测序、蛋白质组学和代谢组学来预测患者结果

**提示**：
```
Use available skills you have access to whenever possible. Analyze RNA-seq with PyDESeq2, process mass spec with pyOpenMS, integrate metabolites from 
HMDB/Metabolomics Workbench, map proteins to pathways (UniProt/KEGG), find interactions via 
STRING, correlate omics layers with statsmodels, build predictive model with scikit-learn, 
and search ClinicalTrials.gov for relevant trials.
```

**使用的技能**：PyDESeq2、pyOpenMS、HMDB、代谢组学工作台、UniProt、KEGG、STRING、statsmodels、scikit-learn、ClinicalTrials.gov

---

### 🎯 虚拟放映活动
**目标**：发现蛋白质-蛋白质相互作用的变构调节剂

**提示**：
```
Use available skills you have access to whenever possible. Retrieve AlphaFold structures, identify interaction interface with BioPython, search ZINC 
for allosteric candidates (MW 300-500, logP 2-4), filter with RDKit, dock with DiffDock, 
rank with DeepChem, check PubChem suppliers, search USPTO patents, and optimize leads with 
MedChem/molfeat.
```

**使用的技能**：AlphaFold DB、BioPython、ZINC、RDKit、DiffDock、DeepChem、PubChem、USPTO、MedChem、molfeat

---

### 🏥 临床变异解释
**目标**：分析 VCF 文件以进行遗传性癌症风险评估

**提示**：
```
Use available skills you have access to whenever possible. Parse VCF with pysam, annotate variants with Ensembl VEP, query ClinVar for pathogenicity, 
check COSMIC for cancer mutations, retrieve gene info from NCBI Gene, analyze protein impact 
with UniProt, search PubMed for case reports, check ClinPGx for pharmacogenomics, generate 
clinical report with ReportLab, and find matching trials on ClinicalTrials.gov.
```
**使用的技能**：pysam、Ensembl、ClinVar、COSMIC、NCBI Gene、UniProt、PubMed、ClinPGx、ReportLab、ClinicalTrials.gov

---

### 🌐 系统生物学网络分析
**目标**：从 RNA-seq 数据分析基因调控网络

**提示**：
```
Use available skills you have access to whenever possible. Query NCBI Gene for annotations, retrieve sequences from UniProt, identify interactions via 
STRING, map to Reactome/KEGG pathways, analyze topology with Torch Geometric, reconstruct 
GRNs with Arboreto, assess druggability with Open Targets, model with PyMC, visualize 
networks, and search GEO for similar patterns.
```

**使用的技能**：NCBI Gene、UniProt、STRING、Reactome、KEGG、Torch Geometric、Arboreto、Open Targets、PyMC、GEO

> 📖 **想要更多示例？** 查看 [docs/examples.md](docs/examples.md) 以获取跨所有科学领域的全面工作流程示例和详细用例。

---

## 🔬 用例

### 🧪 药物发现与药物化学
- **虚拟筛选**：针对蛋白质靶标筛选来自 PubChem/ZINC 的数百万种化合物
- **先导化合物优化**：使用 RDKit 分析结构-活性关系，使用 datamol 生成类似物
- **ADMET 预测**：使用 DeepChem 预测吸收、分布、代谢、排泄和毒性
- **分子对接**：使用 DiffDock 预测结合姿势和亲和力
- **生物活性挖掘**：查询 ChEMBL 中已知的抑制剂并分析 SAR 模式

### 🧬 生物信息学与基因组学
- **序列分析**：使用 BioPython 和 pysam 处理 DNA/RNA/蛋白质序列
- **单细胞分析**：使用 Scanpy 分析 10X 基因组数据，识别细胞类型，使用 Arboreto 推断 GRN
- **变异注释**：使用 Ensembl VEP 注释 VCF 文件，查询 ClinVar 的致病性
- **基因发现**：查询 NCBI Gene、UniProt 和 Ensembl 以获取全面的基因信息
- **网络分析**：通过 STRING 识别蛋白质-蛋白质相互作用，映射到路径（KEGG、Reactome）

### 🏥 临床研究与精准医学
- **临床试验**：搜索 ClinicalTrials.gov 查找相关研究，分析资格标准
- **变异解释**：使用 ClinVar、COSMIC 和 ClinPGx 注释药物基因组学变异
- **药物安全**：查询 FDA 数据库中的不良事件、药物相互作用和召回
- **精准治疗**：将患者变异与靶向治疗和临床试验相匹配

### 🔬 多组学和系统生物学
- **多组学集成**：结合 RNA 测序、蛋白质组学和代谢组学数据
- **通路分析**：富集KEGG/Reactome通路中的差异表达基因
- **网络生物学**：重建基因调控网络，识别枢纽基因
- **生物标志物发现**：整合多组学层来预测患者结果

### 📊 数据分析与可视化
- **统计分析**：执行假设检验、功效分析和实验设计
- **出版数据**：使用 matplotlib 和 seaborn 创建出版质量的可视化
- **网络可视化**：使用 NetworkX 可视化生物网络
- **报告生成**：使用 ReportLab 生成全面的 PDF 报告

### 🧪 实验室自动化
- **协议设计**：创建用于自动液体处理的 Opentrons 协议
- **LIMS 集成**：与 Benchling 和 LabArchives 集成以进行数据管理
- **工作流程自动化**：自动化多步骤实验室工作流程

---

## 📚 可用技能

该存储库包含跨多个领域组织的 **121 多项科学技能**。每项技能都提供了全面的文档、代码示例以及使用科学库、数据库和工具的最佳实践。

### 技能类别

#### 🧬 **生物信息学和基因组学**（15 种以上技能）
- 序列分析：BioPython、pysam、scikit-bio
- 单细胞分析：Scanpy、AnnData、scvi-tools、Arboreto、Cellxgene Census
- 基因组工具：gget、geniml、gtars、deepTools、FlowIO、Zarr
- 系统发育学：ETE 工具包

#### 🧪 **化学信息学和药物发现**（10 多种技能）
- 分子操作：RDKit、Datamol、Molfeat
- 深度学习：DeepChem、TorchDrug
- 对接和筛选：DiffDock
- 药物相似性：MedChem
- 基准：PyTDC

#### 🔬 **蛋白质组学和质谱分析**（2 项技能）
- 光谱处理：matchms、pyOpenMS

#### 🏥 **临床研究与精准医学**（8+技能）
- 临床数据库：ClinicalTrials.gov、ClinVar、ClinPGx、COSMIC、FDA 数据库
- 医疗保健人工智能：PyHealth、NeuroKit2
- 变异分析：Ensembl、NCBI Gene

#### 🖼️ **医学成像和数字病理学**（3 项技能）
- DICOM处理：pydicom
- 整个载玻片成像：histolab、PathML

#### 🤖 **机器学习和人工智能**（15 种以上技能）
- 深度学习：PyTorch Lightning、Transformers、Stable Baselines3、PufferLib
- 经典机器学习：scikit-learn、scikit-survival、SHAP
- 时间序列：万古
- 贝叶斯方法：PyMC
- 优化：PyMOO
- Graph ML：火炬几何
- 降维：UMAP-learn
- 统计建模：statsmodels

#### 🔮 **材料科学与化学**（3 项技能）
- 材料：皮马特根
- 代谢建模：COBRApy
- 天文学：天文学

#### ⚙️ **工程与模拟**（3 项技能）
- 计算流体动力学：FluidSim
- 离散事件模拟：SimPy
- 数据处理：Dask、Polars、Vaex

#### 📊 **数据分析和可视化**（10+ 技能）
- 可视化：Matplotlib、Seaborn、Plotly
- 地理空间分析：GeoPandas
- 网络分析：NetworkX
- 符号数学：SymPy
- PDF 生成：ReportLab
- 数据访问：数据共享

#### 🧪 **实验室自动化**（3 项技能）
- 液体处理：PyLabRobot
- 协议管理：Protocols.io
- LIMS 集成：基准测试、LabArchives

#### 🔬 **多组学和系统生物学**（5 个以上技能）
- 通路分析：KEGG、Reactome、STRING
- 多组学：BIOMNI、Denario、HypoGeniC
- 数据管理：LaminDB

#### 🧬 **蛋白质工程与设计**（2 项技能）
- 蛋白质语言模型：ESM
- 云实验室平台：Adaptyv（自动化蛋白质测试和验证）

#### 📚 **科学沟通**（9 个以上技能）
- 文献：OpenAlex、PubMed、文献综述
- 网页搜索：Perplexity Search（人工智能驱动的实时信息搜索）
- 写作：科学写作、同行评审
- 文档处理：DOCX、PDF、PPTX、XLSX、MarkItDown
- 出版：Paper-2-Web

#### 🔬 **科学数据库**（26+ 技能）
- 蛋白质：UniProt、PDB、AlphaFold DB
- 化学：PubChem、ChEMBL、DrugBank、ZINC、HMDB
- 基因组：Ensembl、NCBI 基因、GEO、ENA、GWAS 目录
- 临床：ClinVar、COSMIC、ClinicalTrials.gov、ClinPGx、FDA 数据库
- 途径：KEGG、Reactome、STRING
- 目标：开放目标
- 代谢组学：代谢组学工作台
- 专利：美国专利商标局

#### 🔧 **基础设施和平台**（5 个以上技能）
- 云计算：模态
- 基因组学平台：DNAnexus、LatchBio
- 显微镜：OMERO
- 自动化：Opentrons
- 工具发现：ToolUniverse

> 📖 **有关所有技能的完整详细信息**，请参阅 [docs/scientific-skills.md](docs/scientific-skills.md)

> 💡 **寻找实际示例？** 查看 [docs/examples.md](docs/examples.md) 以获取跨所有科学领域的综合工作流程示例。

---

## 🤝 贡献

我们欢迎为扩展和改进这个科学技能库做出贡献！

### 贡献方式

✨ **添加新技能**
- 为其他科学包或数据库创建技能
- 添加科学平台和工具的集成

📚 **提高现有技能**
- 通过更多示例和用例增强文档
- 添加新的工作流程和参考资料
- 改进代码示例和脚本
- 修复错误或更新过时的信息

🐛 **报告问题**
- 提交包含详细重现步骤的错误报告
- 建议改进或新功能

### 如何贡献

1.**分叉**存储库
2. **创建**一个功能分支 (`git checkout -b feature/amazing-skill`)
3. **遵循**现有的目录结构和文档模式
4. **确保**所有新技能都包含全面的 `SKILL.md` 文件
5. **彻底测试**您的示例和工作流程
6. **提交**您的更改 (`git commit -m 'Add amazing skill'`)
7. **推送**到您的分支 (`git push origin feature/amazing-skill`)
8. **提交** 拉取请求，并明确描述您的更改

### 贡献指南

✅ 与现有技能文档格式保持一致  
✅ 在所有贡献中包含实用的、可行的示例  
✅ 确保所有代码示例都经过测试且功能正常  
✅ 遵循示例和工作流程中的科学最佳实践  
✅ 添加新功能时更新相关文档  
✅ 在代码中提供清晰的注释和文档字符串  
✅ 包含对官方文档的引用

### 认可

贡献者在我们的社区中得到认可，并且可能具有以下特点：
- 存储库贡献者列表
- 发行说明中特别提及
- K-Dense 社区亮点

您的贡献有助于使科学计算变得更容易实现，并使研究人员能够更有效地利用人工智能工具！

---

## 🔧 故障排除

### 常见问题

**问题：克劳德代码中未加载技能**
- 解决方案：确保您已安装最新版本的 Claude Code
- 尝试重新安装插件：`/plugin marketplace add K-Dense-AI/claude-scientific-skills`

**问题：缺少 Python 依赖项**
- 解决方案：检查特定的`SKILL.md`文件中是否有所需的包
- 安装依赖项：`uv pip install package-name`

**问题：API 速率限制**
- 解决方案：许多数据库都有速率限制。查看具体数据库文档
- 考虑实施缓存或批量请求

**问题：身份验证错误**
- 解决方案：某些服务需要 API 密钥。检查 `SKILL.md` 进行身份验证设置
- 验证您的凭据和权限

**问题：过时的示例**
- 解决方案：通过 GitHub Issues 报告问题
- 检查官方包文档以获取更新的语法

---

## ❓ 常见问题解答

### 一般问题

**问：可以免费使用吗？**  
答：是的！该项目已获得麻省理工学院许可，允许免费用于任何目的，包括商业项目。

**问：为什么所有技能都分组到一个插件而不是单独的插件中？**  
答：我们相信人工智能时代的优秀科学本质上是跨学科的。将所有技能捆绑到一个插件中，使您（和 Claude）可以轻松地跨越各个领域，例如，将基因组学、化学信息学、临床数据和机器学习结合在一个工作流程中，而无需担心要安装或连接哪些个人技能。

**问：我可以将其用于商业项目吗？**  
答：当然！麻省理工学院许可证允许商业和非商业使用，不受限制。

**问：多久更新一次？**  
答：我们定期更新技能以反映最新版本的软件包和 API。主要更新在发行说明中公布。

**问：我可以将其与其他人工智能模型一起使用吗？**  
答：这些技能针对 Claude 进行了优化，但也可以在 MCP 支持下适用于其他模型。 MCP 服务器可与任何 MCP 兼容的客户端配合使用。

### 安装和设置

**问：我需要安装所有 Python 包吗？**  
答：不！仅安装您需要的软件包。每个技能在其 `SKILL.md` 文件中指定其要求。

**问：如果某项技能不起作用怎么办？**  
答：首先检查[疑难解答](#troubleshooting) 部分。如果问题仍然存在，请在 GitHub 上提交问题并提供详细的重现步骤。

**问：这些技能可以离线使用吗？**  
答：数据库技能需要能够访问互联网来查询 API。安装 Python 依赖项后，包技能可以离线使用。

### 贡献

**问：我可以贡献自己的技能吗？**  
答：当然！我们欢迎贡献。有关指南和最佳实践，请参阅[贡献](#contributing) 部分。

**问：如何报告错误或建议功能？**  
答：在 GitHub 上打开一个问题并提供清晰的描述。对于错误，包括重现步骤以及预期行为与实际行为。

---

## 💬 支持

需要帮助吗？以下是如何获得支持：

- 📖 **文档**：检查相关的 `SKILL.md` 和 `references/` 文件夹
- 🐛 **错误报告**：[打开问题](https://github.com/K-Dense-AI/claude-scientific-skills/issues)
- 💡 **功能请求**：[提交功能请求](https://github.com/K-Dense-AI/claude-scientific-skills/issues/new)
- 💼 **企业支持**：联系 [K-Dense](https://k-dense.ai/) 获取商业支持
- 🌐 **MCP 支持**：访问 [claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp) 存储库或使用我们托管的 MCP 服务器

---

## 🎉 加入我们的社区！

**我们很高兴您加入我们！** 🚀

使用 Claude 进行科学计算，与其他科学家、研究人员和人工智能爱好者联系。分享您的发现、提出问题、获得项目帮助并与社区合作！

🌟 **[加入我们的 Slack 社区](https://join.slack.com/t/k-densecommunity/shared_invite/zt-3iajtyls1-EwmkwIZk0g_o74311Tkf5g)** 🌟

无论您是新手还是高级用户，我们的社区都会为您提供支持。我们分享技巧，共同解决问题，展示酷炫的项目，并讨论人工智能科学研究的最新进展。

**再见！** 💬

---

## 📖 引文

如果您在您的研究或项目中使用克劳德科学技能，请将其引用为：

### BibTeX
```bibtex
@software{claude_scientific_skills_2025,
  author = {{K-Dense Inc.}},
  title = {Claude Scientific Skills: A Comprehensive Collection of Scientific Tools for Claude AI},
  year = {2025},
  url = {https://github.com/K-Dense-AI/claude-scientific-skills},
  note = {skills covering databases, packages, integrations, and analysis tools}
}
```

### APA
```
K-Dense Inc. (2025). Claude Scientific Skills: A comprehensive collection of scientific tools for Claude AI [Computer software]. https://github.com/K-Dense-AI/claude-scientific-skills
```

### 司法协助
```
K-Dense Inc. Claude Scientific Skills: A Comprehensive Collection of Scientific Tools for Claude AI. 2025, github.com/K-Dense-AI/claude-scientific-skills.
```

### 纯文本
```
Claude Scientific Skills by K-Dense Inc. (2025)
Available at: https://github.com/K-Dense-AI/claude-scientific-skills
```

我们感谢对受益于这些技能的出版物、演示或项目的认可！

---

## 📄 许可证

该项目根据 **MIT 许可证** 获得许可。

**版权所有 © 2025 K-Dense Inc.** ([k-dense.ai](https://k-dense.ai/))

### 要点：
- ✅ **免费用于任何用途**（商业和非商业）
- ✅ **开源** - 自由修改、分发和使用
- ✅ **宽容** - 对重复使用的最小限制
- ⚠️ **无保修** - “按原样”提供，无任何形式的保修

请参阅 [LICENSE.md](LICENSE.md) 了解完整条款。

## 明星历史

[![明星历史图](https://api.star-history.com/svg?repos=K-Dense-AI/claude-scientific-skills&type=date&legend=top-left)](https://www.star-history.com/#K-Dense-AI/claude-scientific-skills&type=date&legend=top-left)