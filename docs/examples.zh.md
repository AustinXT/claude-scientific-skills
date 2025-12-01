<!-- 此文件由机器翻译自 examples.md -->

# 真实世界的科学例子

本文档提供了全面、实用的示例，展示了如何结合克劳德的科学技能来解决跨多个领域的实际科学问题。

---

## 📋 目录

1. [药物发现与药物化学](#drug-discovery--medicinal-chemistry)
2.【癌症基因组学与精准医学】(#cancer-genomics--精准医学)
3. [单细胞转录组学](#single-cell-transcriptomics)
4. [蛋白质结构与功能](#蛋白质-结构--功能)
5. [化学安全与毒理学](#chemical-safety--毒理学)
6. [临床试验分析](#clinical-tri-analysis)
7. [代谢组学与系统生物学](#metabolomics--systems-biology)
8.[材料科学与化学](#materials-science--chemistry)
9.[数字病理学](#digital-pathology)
10. [实验室自动化和协议设计](#lab-automation--protocol-design)
11.[农业基因组学](#agriculture-genomics)
12. [神经科学与脑成像](#neuroscience--brain-imaging)
13.[环境微生物学](#environmental-microbiology)
14. [传染病研究](#infectious-disease-research)
15. [多组学整合](#multi-omics-integration)
16.[计算化学与合成](#computational-chemistry--synthesis)
17. [临床研究与现实世界证据](#clinical-research--real-world-evidence)
18.[实验物理与数据分析](#experimental-physicals--data-analysis)
19. [化学工程与工艺优化](#chemical-engineering--process-optimization)

---

## 药物发现和药物化学

### 示例 1：发现新型肺癌 EGFR 抑制剂

**目标**：确定与现有药物相比具有改进特性的新型 EGFR 小分子抑制剂。

**使用的技能**：
- `chembl-database` - 查询生物活性数据
- `pubchem-database` - 搜索化合物库
- `rdkit` - 分析分子特性
- `datamol` - 生成类似物
- `diffdock` - 分子对接
- `alphafold-database` - 检索蛋白质结构
- `pubmed-database` - 文献综述
- `cosmic-database` - 查询突变
- `deepchem` - 属性预测
- `scientific-visualization` - 创建图形

**工作流程**：

```bash
# Always use available 'skills' when possible. Keep the output organized.

Step 1: Query ChEMBL for known EGFR inhibitors with high potency
- Search for compounds targeting EGFR (CHEMBL203)
- Filter: IC50 < 50 nM, pChEMBL value > 7
- Extract SMILES strings and activity data
- Export to DataFrame for analysis

Step 2: Analyze structure-activity relationships
- Load compounds into RDKit
- Calculate molecular descriptors (MW, LogP, TPSA, HBD, HBA)
- Generate Morgan fingerprints (radius=2, 2048 bits)
- Perform hierarchical clustering to identify scaffolds
- Visualize top scaffolds with activity annotations

Step 3: Identify resistance mutations from COSMIC
- Query COSMIC for EGFR mutations in lung cancer
- Focus on gatekeeper mutations (T790M, C797S)
- Extract mutation frequencies and clinical significance
- Cross-reference with literature in PubMed

Step 4: Retrieve EGFR structure from AlphaFold
- Download AlphaFold prediction for EGFR kinase domain
- Alternatively, use experimental structure from PDB (if available)
- Prepare structure for docking (add hydrogens, optimize)

Step 5: Generate novel analogs using datamol
- Select top 5 scaffolds from ChEMBL analysis
- Use scaffold decoration to generate 100 analogs per scaffold
- Apply Lipinski's Rule of Five filtering
- Ensure synthetic accessibility (SA score < 4)
- Check for PAINS and unwanted substructures

Step 6: Predict properties with DeepChem
- Train graph convolutional model on ChEMBL EGFR data
- Predict pIC50 for generated analogs
- Predict ADMET properties (solubility, permeability, hERG)
- Rank candidates by predicted potency and drug-likeness

Step 7: Virtual screening with DiffDock
- Perform molecular docking on top 50 candidates
- Dock into wild-type EGFR and T790M mutant
- Calculate binding energies and interaction patterns
- Identify compounds with favorable binding to both forms

Step 8: Search PubChem for commercial availability
- Query PubChem for top 10 candidates by InChI key
- Check supplier information and purchasing options
- Identify close analogs if exact matches unavailable

Step 9: Literature validation with PubMed
- Search for any prior art on top scaffolds
- Query: "[scaffold_name] AND EGFR AND inhibitor"
- Summarize relevant findings and potential liabilities

Step 10: Create comprehensive report
- Generate 2D structure visualizations of top hits
- Create scatter plots: MW vs LogP, TPSA vs potency
- Produce binding pose figures for top 3 compounds
- Generate table comparing properties to approved drugs (gefitinib, erlotinib)
- Write scientific summary with methodology, results, and recommendations
- Export to PDF with proper citations

Expected Output: 
- Ranked list of 10-20 novel EGFR inhibitor candidates
- Predicted activity and ADMET properties
- Docking poses and binding analysis
- Comprehensive scientific report with publication-quality figures
```

---

### 示例 2：罕见疾病的药物再利用

**目标**：确定 FDA 批准的可重新用于治疗罕见代谢性疾病的药物。

**使用的技能**：
- `drugbank-database` - 查询批准的药物
- `opentargets-database` - 目标疾病关联
- `string-database` - 蛋白质相互作用
- `kegg-database` - 路径分析
- `reactome-database` - 通路富集
- `clinicaltrials-database` - 检查正在进行的试验
- `fda-database` - 药品审批和安全
- `networkx` - 网络分析
- `literature-review` - 系统审核

**工作流程**：

<<<代码块_1>>>

---

## 癌症基因组学与精准医学

### 示例 3：临床变异解释流程

**目标**：分析患者的肿瘤测序数据，以确定可行的突变和治疗建议。

**使用的技能**：
- `pysam` - 解析 VCF 文件
- `ensembl-database` - 变体注释
- `clinvar-database` - 临床意义
- `cosmic-database` - 体细胞突变
- `gene-database` - 基因信息
- `uniprot-database` - 蛋白质影响
- `drugbank-database` - 药物基因关联
- `clinicaltrials-database` - 匹配试验
- `opentargets-database` - 目标验证
- `pubmed-database` - 文献证据
- `reportlab` - 生成临床报告

**工作流程**：

<<<代码块_2>>>

---

### 示例 4：根据基因表达进行癌症亚型分类

**目标**：使用 RNA-seq 数据对乳腺癌亚型进行分类，并确定亚型特异性的治疗漏洞。

**使用的技能**：
- `pydeseq2` - 差分表达式
- `scanpy` - 聚类和可视化
- `scikit-learn` - 机器学习分类
- `gene-database` - 基因注释
- `reactome-database` - 路径分析
- `opentargets-database` - 药物靶点
- `pubmed-database` - 文献验证
- `matplotlib` - 可视化
- `seaborn` - 热图

**工作流程**：

<<<代码块_3>>>

---

## 单细胞转录组学

### 示例 5：肿瘤微环境的单细胞图谱
**目标**：表征肿瘤微环境中的免疫细胞群并识别免疫治疗生物标志物。

**使用的技能**：
- `scanpy` - 单细胞分析
- `scvi-tools` - 批量校正和集成
- `cellxgene-census` - 参考数据
- `gene-database` - 细胞类型标记
- `anndata` - 数据结构
- `arboreto` - 基因调控网络
- `pytorch-lightning` - 深度学习
- `matplotlib` - 可视化
- `statistical-analysis` - 假设检验

**工作流程**：

<<<代码块_4>>>

---

## 蛋白质结构与功能

### 实施例 6：基于结构的蛋白质-蛋白质相互作用抑制剂设计

**目标**：设计小分子来破坏治疗相关的蛋白质-蛋白质相互作用。

**使用的技能**：
- `alphafold-database` - 蛋白质结构
- `pdb-database` - 实验结构
- `uniprot-database` - 蛋白质信息
- `biopython` - 结构分析
- `pyrosetta` - 蛋白质设计（如果有）
- `rdkit` - 化学库生成
- `diffdock` - 分子对接
- `zinc-database` - 筛选库
- `deepchem` - 属性预测
- `pymol` - 可视化（外部）

**工作流程**：

<<<代码块_5>>>

---

## 化学品安全与毒理学

### 示例 7：预测毒理学评估

**目标**：在合成前评估候选药物的潜在毒性和安全性。

**使用的技能**：
- `rdkit` - 分子描述符
- `deepchem` - 毒性预测
- `chembl-database` - 毒性数据
- `pubchem-database` - 生物测定数据
- `drugbank-database` - 已知药物毒性
- `fda-database` - 不良事件
- `hmdb-database` - 代谢物预测
- `scikit-learn` - 分类模型
- `shap` - 模型可解释性

**工作流程**：

<<<代码块_6>>>

---

## 临床试验分析

### 示例 8：新适应症的竞争格局分析

**目标**：分析特定适应症的临床试验情况，为开发策略提供信息。

**使用的技能**：
- `clinicaltrials-database` - 试用注册表
- `fda-database` - 药品批准
- `pubmed-database` - 已发布结果
- `drugbank-database` - 批准的药物
- `opentargets-database` - 目标验证
- `polars` - 数据操作
- `matplotlib` - 可视化
- `seaborn` - 统计图
- `reportlab` - 报告生成

**工作流程**：

```bash
Step 1: Search ClinicalTrials.gov for all trials in indication
- Query: "[disease/indication]"
- Filter: All phases, all statuses
- Extract fields:
  * NCT ID, title, phase, status
  * Start date, completion date, enrollment
  * Intervention/drug names
  * Primary/secondary outcomes
  * Sponsor and collaborators
- Export to structured JSON/CSV

Step 2: Categorize trials by mechanism of action
- Extract drug names and intervention types
- Query DrugBank for mechanism of action
- Query Open Targets for target information
- Classify into categories:
  * Small molecules vs biologics
  * Target class (kinase inhibitor, antibody, etc.)
  * Novel vs repurposing

Step 3: Analyze trial phase progression
- Calculate success rates by phase (I → II, II → III)
- Identify terminated trials and reasons for termination
- Track time from phase I start to NDA submission
- Calculate median development timelines

Step 4: Search FDA database for recent approvals
- Query FDA drug approvals in the indication (last 10 years)
- Extract approval dates, indications, priority review status
- Note any accelerated approvals or breakthroughs
- Review FDA drug labels for safety information

Step 5: Extract outcome measures
- Compile all primary endpoints used
- Identify most common endpoints:
  * Survival (OS, PFS, DFS)
  * Response rates (ORR, CR, PR)
  * Biomarker endpoints
  * Patient-reported outcomes
- Note emerging or novel endpoints

Step 6: Analyze competitive dynamics
- Identify leading companies and their pipelines
- Map trials by phase for each major competitor
- Note partnership and licensing deals
- Assess crowded vs underserved patient segments

Step 7: Search PubMed for published trial results
- Query: "[NCT ID]" for each completed trial
- Extract published outcomes and conclusions
- Identify trends in efficacy and safety
- Note any unmet needs highlighted in discussions

Step 8: Analyze target validation evidence
- Query Open Targets for target-disease associations
- Extract genetic evidence scores
- Review tractability assessments
- Compare targets being pursued across trials

Step 9: Identify unmet needs and opportunities
- Analyze trial failures for common patterns
- Identify patient populations excluded from trials
- Note resistance mechanisms or limitations mentioned
- Assess gaps in current therapeutic approaches

Step 10: Perform temporal trend analysis
- Plot trial starts over time (by phase, mechanism)
- Identify increasing or decreasing interest in targets
- Correlate with publication trends and scientific advances
- Predict future trends in the space

Step 11: Create comprehensive visualizations
- Timeline of all trials (Gantt chart style)
- Phase distribution pie chart
- Mechanism of action breakdown
- Geographic distribution of trials
- Enrollment trends over time
- Success rate funnels (Phase I → II → III → Approval)
- Sponsor/company market share

Step 12: Generate competitive intelligence report
- Executive summary of competitive landscape
- Total number of active programs by phase
- Key players and their development stage
- Standard of care and approved therapies
- Emerging approaches and novel targets
- Identified opportunities and white space
- Risk analysis (crowded targets, high failure rates)
- Strategic recommendations:
  * Patient population to target
  * Differentiation strategies
  * Partnership opportunities
  * Regulatory pathway considerations
- Export as professional PDF with citations and data tables

Expected Output:
- Comprehensive trial database for indication
- Success rate and timeline statistics
- Competitive landscape mapping
- Unmet need analysis
- Strategic recommendations
- Publication-ready report with visualizations
```

---

## 代谢组学和系统生物学

### 示例 9：代谢疾病的多组学整合

**目标**：整合转录组学、蛋白质组学和代谢组学，以确定代谢疾病中失调的途径。

**使用的技能**：
- `pydeseq2` - RNA-seq 分析
- `pyopenms` - 质谱分析
- `hmdb-database` - 代谢物鉴定
- `metabolomics-workbench-database` - 公共数据集
- `kegg-database` - 路径映射
- `reactome-database` - 路径分析
- `string-database` - 蛋白质相互作用
- `statsmodels` - 多组学相关性
- `networkx` - 网络分析
- `pymc` - 贝叶斯建模

**工作流程**：

```bash
Step 1: Process RNA-seq data
- Load gene count matrix
- Run differential expression with PyDESeq2
- Compare disease vs control (adjusted p < 0.05, |LFC| > 1)
- Extract gene symbols and fold changes
- Map to KEGG gene IDs

Step 2: Process proteomics data
- Load LC-MS/MS results with PyOpenMS
- Perform peptide identification and quantification
- Normalize protein abundances
- Run statistical testing (t-test or limma)
- Extract significant proteins (p < 0.05, |FC| > 1.5)

Step 3: Process metabolomics data
- Load untargeted metabolomics data (mzML format) with PyOpenMS
- Perform peak detection and alignment
- Match features to HMDB database by accurate mass
- Annotate metabolites with MS/MS fragmentation
- Extract putative identifications (Level 2/3)
- Perform statistical analysis (FDR < 0.05, |FC| > 2)

Step 4: Search Metabolomics Workbench for public data
- Query for same disease or tissue type
- Download relevant studies
- Reprocess for consistency with own data
- Use as validation cohort

Step 5: Map all features to KEGG pathways
- Map genes to KEGG orthology (KO) terms
- Map proteins to KEGG identifiers
- Map metabolites to KEGG compound IDs
- Identify pathways with multi-omics coverage

Step 6: Perform pathway enrichment analysis
- Test for enrichment in KEGG pathways
- Test for enrichment in Reactome pathways
- Apply Fisher's exact test with multiple testing correction
- Focus on pathways with hits in ≥2 omics layers

Step 7: Build protein-metabolite networks
- Query STRING for protein-protein interactions
- Map proteins to KEGG reactions
- Connect enzymes to their substrates/products
- Build integrated network with genes → proteins → metabolites

Step 8: Network topology analysis with NetworkX
- Calculate node centrality (degree, betweenness)
- Identify hub metabolites and key enzymes
- Find bottleneck reactions
- Detect network modules with community detection
- Identify dysregulated subnetworks

Step 9: Correlation analysis across omics layers
- Calculate Spearman correlations between:
  * Gene expression and protein abundance
  * Protein abundance and metabolite levels
  * Gene expression and metabolites (for enzyme-product pairs)
- Use statsmodels for significance testing
- Focus on enzyme-metabolite pairs with expected relationships

Step 10: Bayesian network modeling with PyMC
- Build probabilistic graphical model of pathway
- Model causal relationships: gene → protein → metabolite
- Incorporate prior knowledge from KEGG/Reactome
- Perform inference to identify key regulatory nodes
- Estimate effect sizes and uncertainties

Step 11: Identify therapeutic targets
- Prioritize enzymes with:
  * Significant changes in all three omics layers
  * High network centrality
  * Druggable target class (kinases, transporters, etc.)
- Query DrugBank for existing inhibitors
- Search PubMed for validation in disease models

Step 12: Create comprehensive multi-omics report
- Summary statistics for each omics layer
- Venn diagram of overlapping pathway hits
- Pathway enrichment dot plots
- Integrated network visualization (color by fold change)
- Correlation heatmaps (enzyme-metabolite pairs)
- Bayesian network structure
- Table of prioritized therapeutic targets
- Biological interpretation and mechanistic insights
- Generate publication-quality figures
- Export PDF report with all results

Expected Output:
- Integrated multi-omics dataset
- Dysregulated pathway identification
- Multi-omics network model
- Prioritized list of therapeutic targets
- Comprehensive systems biology report
```

---

## 材料科学与化学

### 示例 10：电池应用的高通量材料发现

**目标**：通过计算筛选发现用于锂离子电池的新型固体电解质材料。

**使用的技能**：
- `pymatgen` - 材料分析
- `matminer` - 特征工程
- `scikit-learn` - 机器学习
- `pymoo` - 多目标优化
- `ase` - 原子模拟
- `sympy` - 符号数学
- `vaex` - 大型数据集处理
- `matplotlib` - 可视化
- `scientific-writing` - 报告生成

**工作流程**：

```bash
Step 1: Generate candidate materials library
- Use Pymatgen to enumerate compositions:
  * Li-containing compounds (Li₁₋ₓM₁₊ₓX₂)
  * M = transition metals (Zr, Ti, Ta, Nb)
  * X = O, S, Se
- Generate ~10,000 candidate compositions
- Apply charge neutrality constraints

Step 2: Filter by thermodynamic stability
- Query Materials Project database via Pymatgen
- Calculate formation energy from elements
- Calculate energy above convex hull (E_hull)
- Filter: E_hull < 50 meV/atom (likely stable)
- Retain ~2,000 thermodynamically plausible compounds

Step 3: Predict crystal structures
- Use Pymatgen structure predictor
- Generate most likely crystal structures for each composition
- Consider common structure types: LISICON, NASICON, garnet, perovskite
- Calculate structural descriptors

Step 4: Calculate material properties with Pymatgen
- Lattice parameters and volume
- Density
- Packing fraction
- Ionic radii and bond lengths
- Coordination environments

Step 5: Feature engineering with matminer
- Calculate compositional features:
  * Elemental property statistics (electronegativity, ionic radius)
  * Valence electron concentrations
  * Stoichiometric attributes
- Calculate structural features:
  * Pore size distribution
  * Site disorder parameters
  * Partial radial distribution functions

Step 6: Build ML models for Li⁺ conductivity prediction
- Collect training data from literature (experimental conductivities)
- Train ensemble models with scikit-learn:
  * Random Forest
  * Gradient Boosting
  * Neural Network
- Use 5-fold cross-validation
- Predict ionic conductivity for all candidates

Step 7: Predict additional properties
- Electrochemical stability window (ML model)
- Mechanical properties (bulk modulus, shear modulus)
- Interfacial resistance (estimate from structure)
- Synthesis temperature (ML prediction from similar compounds)

Step 8: Multi-objective optimization with PyMOO
Define optimization objectives:
- Maximize: ionic conductivity (>10⁻³ S/cm target)
- Maximize: electrochemical window (>4.5V target)
- Minimize: synthesis temperature (<800°C preferred)
- Minimize: cost (based on elemental abundance)

Run NSGA-II to find Pareto optimal solutions
Extract top 50 candidates from Pareto front

Step 9: Analyze Pareto optimal materials
- Identify composition trends (which elements appear frequently)
- Analyze structure-property relationships
- Calculate trade-offs between objectives
- Identify "sweet spot" compositions

Step 10: Validate predictions with DFT calculations
- Select top 10 candidates for detailed study
- Set up DFT calculations (VASP-like, if available via ASE)
- Calculate:
  * Accurate formation energies
  * Li⁺ migration barriers (NEB calculations)
  * Electronic band gap
  * Elastic constants
- Compare DFT results with ML predictions

Step 11: Literature and patent search
- Search for prior art on top candidates
- PubMed and Google Scholar: "[composition] AND electrolyte"
- USPTO: Check for existing patents on similar compositions
- Identify any experimental reports on related materials

Step 12: Generate materials discovery report
- Summary of screening workflow and statistics
- Pareto front visualization (conductivity vs stability vs cost)
- Structure visualization of top candidates
- Property comparison table
- Composition-property trend analysis
- DFT validation results
- Predicted performance vs state-of-art materials
- Synthesis recommendations
- IP landscape summary
- Prioritized list of 5-10 materials for experimental validation
- Export as publication-ready PDF

Expected Output:
- Screened library of 10,000+ materials
- ML models for property prediction
- Pareto-optimal set of 50 candidates
- Detailed analysis of top 10 materials
- DFT validation results
- Comprehensive materials discovery report
```

---

## 数字病理学

### 示例 11：整个载玻片图像中的自动肿瘤检测

**目标**：开发并验证用于组织病理学图像中自动肿瘤检测的深度学习模型。

**使用的技能**：
- `histolab` - 整个幻灯片图像处理
- `pathml` - 计算病理学
- `pytorch-lightning` - 深度学习
- `torchvision` - 图像模型
- `scikit-learn` - 模型评估
- `pydicom` - DICOM 处理
- `omero-integration` - 图像管理
- `matplotlib` - 可视化
- `shap` - 模型可解释性

**工作流程**：

```bash
Step 1: Load whole slide images with HistoLab
- Load WSI files (SVS, TIFF formats)
- Extract slide metadata and magnification levels
- Visualize slide thumbnails
- Inspect tissue area vs background

Step 2: Tile extraction and preprocessing
- Use HistoLab to extract tiles (256×256 pixels at 20× magnification)
- Filter tiles:
  * Remove background (tissue percentage > 80%)
  * Apply color normalization (Macenko or Reinhard method)
  * Filter out artifacts and bubbles
- Extract ~100,000 tiles per slide across all slides

Step 3: Create annotations (if training from scratch)
- Load pathologist annotations (if available via OMERO)
- Convert annotations to tile-level labels
- Categories: tumor, stroma, necrosis, normal
- Balance classes through stratified sampling

Step 4: Set up PathML pipeline
- Create PathML SlideData objects
- Define preprocessing pipeline:
  * Stain normalization
  * Color augmentation (HSV jitter)
  * Rotation and flipping
- Split data: 70% train, 15% validation, 15% test

Step 5: Build deep learning model with PyTorch Lightning
- Architecture: ResNet50 or EfficientNet backbone
- Add custom classification head for tissue types
- Define training pipeline:
  * Loss function: Cross-entropy or Focal loss
  * Optimizer: Adam with learning rate scheduling
  * Augmentations: rotation, flip, color jitter, elastic deformation
  * Batch size: 32
  * Mixed precision training

Step 6: Train model
- Train on tile-level labels
- Monitor metrics: accuracy, F1 score, AUC
- Use early stopping on validation loss
- Save best model checkpoint
- Training time: ~6-12 hours on GPU

Step 7: Evaluate model performance
- Test on held-out test set
- Calculate metrics with scikit-learn:
  * Accuracy, precision, recall, F1 per class
  * Confusion matrix
  * ROC curves and AUC
- Compute confidence intervals with bootstrapping

Step 8: Slide-level aggregation
- Apply model to all tiles in each test slide
- Aggregate predictions:
  * Majority voting
  * Weighted average by confidence
  * Spatial smoothing with convolution
- Generate probability heatmaps overlaid on WSI

Step 9: Model interpretability with SHAP
- Apply GradCAM or SHAP to explain predictions
- Visualize which regions contribute to tumor classification
- Generate attention maps showing model focus
- Validate that model attends to relevant histological features

Step 10: Clinical validation
- Compare model predictions with pathologist diagnosis
- Calculate inter-rater agreement (kappa score)
- Identify discordant cases for review
- Analyze error types: false positives, false negatives

Step 11: Integration with OMERO
- Upload processed slides and heatmaps to OMERO server
- Attach model predictions as slide metadata
- Enable pathologist review interface
- Store annotations and corrections for model retraining

Step 12: Generate clinical validation report
- Model architecture and training details
- Performance metrics with confidence intervals
- Slide-level accuracy vs pathologist ground truth
- Heatmap visualizations for representative cases
- Analysis of failure modes
- Comparison with published methods
- Discussion of clinical applicability
- Recommendations for deployment and monitoring
- Export PDF report for regulatory submission (if needed)

Expected Output:
- Trained deep learning model for tumor detection
- Tile-level and slide-level predictions
- Probability heatmaps for visualization
- Performance metrics and validation results
- Model interpretation visualizations
- Clinical validation report
```

---

## 实验室自动化和协议设计

### 示例 12：自动高通量筛选方案

**目标**：使用液体处理机器人设计并执行自动化化合物筛选工作流程。

**使用的技能**：
- `pylabrobot` - 实验室自动化
- `opentrons-integration` - Opentrons 协议
- `benchling-integration` - 样本跟踪
- `protocolsio-integration` - 协议文档
- `simpy` - 过程模拟
- `polars` - 数据处理
- `matplotlib` - 板可视化
- `reportlab` - 报告生成

**工作流程**：

```bash
Step 1: Define screening campaign in Benchling
- Create compound library in Benchling registry
- Register all compounds with structure, concentration, location
- Define plate layouts (384-well format)
- Track compound source plates in inventory
- Set up ELN entry for campaign documentation

Step 2: Design assay protocol
- Define assay steps:
  * Dispense cells (5000 cells/well)
  * Add compounds (dose-response curve, 10 concentrations)
  * Incubate 48 hours at 37°C
  * Add detection reagent (cell viability assay)
  * Read luminescence signal
- Calculate required reagent volumes
- Document protocol in Protocols.io
- Share with team for review

Step 3: Simulate workflow with SimPy
- Model liquid handler, incubator, plate reader as resources
- Simulate timing for 20 plates (7,680 wells)
- Identify bottlenecks (plate reader reads take 5 min/plate)
- Optimize scheduling: stagger plate processing
- Validate that throughput goal is achievable (20 plates/day)

Step 4: Design plate layout
- Use PyLabRobot to generate plate maps:
  * Columns 1-2: positive controls (DMSO)
  * Columns 3-22: compound titrations (10 concentrations in duplicate)
  * Columns 23-24: negative controls (cytotoxic control)
- Randomize compound positions across plates
- Account for edge effects (avoid outer wells for samples)
- Export plate maps to CSV

Step 5: Create Opentrons protocol for cell seeding
- Write Python protocol using Opentrons API 2.0
- Steps:
  * Aspirate cells from reservoir
  * Dispense 40 μL cell suspension per well
  * Tips: use P300 multi-channel for speed
  * Include mixing steps to prevent settling
- Simulate protocol in Opentrons app
- Test on one plate before full run

Step 6: Create Opentrons protocol for compound addition
- Acoustic liquid handler (Echo) or pin tool for nanoliter transfers
- If using Opentrons:
  * Source: 384-well compound plates
  * Transfer 100 nL compound (in DMSO) to assay plates
  * Use P20 for precision
  * Prepare serial dilutions on deck if needed
- Account for DMSO normalization (1% final)

Step 7: Integrate with Benchling for sample tracking
- Use Benchling API to:
  * Retrieve compound information (structure, batch, concentration)
  * Log plate creation in inventory
  * Create transfer records for audit trail
  * Link assay plates to ELN entry

Step 8: Execute automated workflow
- Day 1: Seed cells with Opentrons
- Day 1 (4h later): Add compounds with Opentrons
- Day 3: Add detection reagent (manual or automated)
- Day 3 (2h later): Read plates on plate reader
- Store plates at 4°C between steps

Step 9: Collect and process data
- Export raw luminescence data from plate reader
- Load data with Polars for fast processing
- Normalize data:
  * Subtract background (media-only wells)
  * Calculate % viability relative to DMSO control
  * Apply plate-wise normalization to correct systematic effects
- Quality control:
  * Z' factor calculation (> 0.5 for acceptable assay)
  * Coefficient of variation for controls (< 10%)
  * Flag plates with poor QC metrics

Step 10: Dose-response curve fitting
- Fit 4-parameter logistic curves for each compound
- Calculate IC50, Hill slope, max/min response
- Use scikit-learn or scipy for curve fitting
- Compute 95% confidence intervals
- Flag compounds with poor curve fits (R² < 0.8)

Step 11: Hit identification and triage
- Define hit criteria:
  * IC50 < 10 μM
  * Max inhibition > 50%
  * Curve quality: R² > 0.8
- Prioritize hits by potency
- Check for PAINS patterns with RDKit
- Cross-reference with known aggregators/frequent hitters

Step 12: Visualize results and generate report
- Create plate heatmaps showing % viability
- Dose-response curve plots for hits
- Scatter plot: potency vs max effect
- QC metric summary across plates
- Structure visualization of top 20 hits
- Generate campaign summary report:
  * Screening statistics (compounds tested, hit rate)
  * QC metrics and data quality assessment
  * Hit list with structures and IC50 values
  * Protocol documentation from Protocols.io
  * Raw data files and analysis code
  * Recommendations for confirmation assays
- Update Benchling ELN with results
- Export PDF report for stakeholders

Expected Output:
- Automated screening protocols (Opentrons Python files)
- Executed screen of 384-well plates
- Quality-controlled dose-response data
- Hit list with IC50 values
- Comprehensive screening report
```

---

## 农业基因组学

### 示例 13：GWAS 用于提高作物产量

**目标**：确定与作物品种的耐旱性和产量相关的遗传标记。

**使用的技能**：
- `biopython` - 序列分析
- `pysam` - VCF 处理
- `gwas-database` - 公共 GWAS 数据
- `ensembl-database` - 植物基因组学
- `gene-database` - 基因注释
- `scanpy` - 群体结构（适用于遗传数据）
- `scikit-learn` - PCA 和聚类
- `statsmodels` - 关联测试
- `matplotlib` - 曼哈顿地块
- `seaborn` - 可视化

**工作流程**：

```bash
Step 1: Load and QC genotype data
- Load VCF file with pysam
- Filter variants:
  * Call rate > 95%
  * Minor allele frequency (MAF) > 5%
  * Hardy-Weinberg equilibrium p > 1e-6
- Convert to numeric genotype matrix (0, 1, 2)
- Retain ~500,000 SNPs after QC

Step 2: Assess population structure
- Calculate genetic relationship matrix
- Perform PCA with scikit-learn (use top 10 PCs)
- Visualize population structure (PC1 vs PC2)
- Identify distinct subpopulations or admixture
- Note: will use PCs as covariates in GWAS

Step 3: Load and process phenotype data
- Drought tolerance score (1-10 scale, measured under stress)
- Grain yield (kg/hectare)
- Days to flowering
- Plant height
- Quality control:
  * Remove outliers (> 3 SD from mean)
  * Transform if needed (log or rank-based for skewed traits)
  * Adjust for environmental covariates (field, year)

Step 4: Calculate kinship matrix
- Compute genetic relatedness matrix
- Account for population structure and relatedness
- Will use in mixed linear model to control for confounding

Step 5: Run genome-wide association study
- For each phenotype, test association with each SNP
- Use mixed linear model (MLM) in statsmodels:
  * Fixed effects: SNP genotype, PCs (top 10)
  * Random effects: kinship matrix
  * Bonferroni threshold: p < 5e-8 (genome-wide significance)
- Multiple testing correction: Bonferroni or FDR
- Calculate genomic inflation factor (λ) to check for inflation

Step 6: Identify significant associations
- Extract SNPs passing significance threshold
- Determine lead SNPs (most significant in each locus)
- Define loci: extend ±500 kb around lead SNP
- Identify independent associations via conditional analysis

Step 7: Annotate significant loci
- Map SNPs to genes using Ensembl Plants API
- Identify genic vs intergenic SNPs
- For genic SNPs:
  * Determine consequence (missense, synonymous, intronic, UTR)
  * Extract gene names and descriptions
- Query NCBI Gene for gene function
- Prioritize genes with known roles in stress response or development

Step 8: Search GWAS Catalog for prior reports
- Query GWAS Catalog for similar traits in same or related species
- Check for replication of known loci
- Identify novel vs known associations

Step 9: Functional enrichment analysis
- Extract all genes within significant loci
- Perform GO enrichment analysis
- Test for enrichment in KEGG pathways
- Focus on pathways related to:
  * Drought stress response (ABA signaling, osmotic adjustment)
  * Photosynthesis and carbon fixation
  * Root development

Step 10: Estimate SNP heritability and genetic architecture
- Calculate variance explained by significant SNPs
- Estimate SNP-based heritability (proportion of variance explained)
- Assess genetic architecture: few large-effect vs many small-effect loci

Step 11: Build genomic prediction model
- Train genomic selection model with scikit-learn:
  * Ridge regression (GBLUP equivalent)
  * Elastic net
  * Random Forest
- Use all SNPs (not just significant ones)
- Cross-validate to predict breeding values
- Assess prediction accuracy

Step 12: Generate GWAS report
- Manhattan plots for each trait
- QQ plots to assess test calibration
- Regional association plots for significant loci
- Gene models overlaid on loci
- Table of significant SNPs with annotations
- Functional enrichment results
- Genomic prediction accuracy
- Biological interpretation:
  * Candidate genes for drought tolerance
  * Potential molecular mechanisms
  * Implications for breeding programs
- Recommendations:
  * SNPs to use for marker-assisted selection
  * Genes for functional validation
  * Crosses to generate mapping populations
- Export publication-quality PDF with all results

Expected Output:
- Significant SNP-trait associations
- Annotated candidate genes
- Functional enrichment analysis
- Genomic prediction models
- Comprehensive GWAS report
- Recommendations for breeding programs
```

---

## 神经科学与脑成像

### 示例 14：fMRI 数据的大脑连接性分析

**目标**：分析静息态功能磁共振成像数据，以确定疾病中改变的大脑连接模式。

**使用的技能**：
- `neurokit2` - 神经生理信号处理
- `nilearn`（外部）- 神经影像分析
- `scikit-learn` - 分类和聚类
- `networkx` - 图论分析
- `statsmodels` - 统计测试
- `torch_geometric` - 图神经网络
- `pymc` - 贝叶斯建模
- `matplotlib` - 大脑可视化
- `seaborn` - 连接矩阵

**工作流程**：

```bash
Step 1: Load and preprocess fMRI data
# Note: Use nilearn or similar for fMRI-specific preprocessing
- Load 4D fMRI images (BOLD signal)
- Preprocessing:
  * Motion correction (realignment)
  * Slice timing correction
  * Spatial normalization to MNI space
  * Smoothing (6mm FWHM Gaussian kernel)
  * Temporal filtering (0.01-0.1 Hz bandpass)
  * Nuisance regression (motion, CSF, white matter)

Step 2: Define brain regions (parcellation)
- Apply brain atlas (e.g., AAL, Schaefer 200-region atlas)
- Extract average time series for each region
- Result: 200 time series per subject (one per brain region)

Step 3: Signal cleaning with NeuroKit2
- Denoise time series
- Remove physiological artifacts
- Apply additional bandpass filtering if needed
- Identify and handle outlier time points

Step 4: Calculate functional connectivity
- Compute pairwise Pearson correlations between all regions
- Result: 200×200 connectivity matrix per subject
- Fisher z-transform correlations for group statistics
- Threshold weak connections (|r| < 0.2)

Step 5: Graph theory analysis with NetworkX
- Convert connectivity matrices to graphs
- Calculate global network metrics:
  * Clustering coefficient (local connectivity)
  * Path length (integration)
  * Small-worldness (balance of segregation and integration)
  * Modularity (community structure)
- Calculate node-level metrics:
  * Degree centrality
  * Betweenness centrality
  * Eigenvector centrality
  * Participation coefficient (inter-module connectivity)

Step 6: Statistical comparison between groups
- Compare patients vs healthy controls
- Use statsmodels for group comparisons:
  * Paired or unpaired t-tests for connectivity edges
  * FDR correction for multiple comparisons across all edges
  * Identify edges with significantly different connectivity
- Compare global and node-level network metrics
- Calculate effect sizes (Cohen's d)

Step 7: Identify altered subnetworks
- Threshold statistical maps (FDR < 0.05)
- Identify clusters of altered connectivity
- Map to functional brain networks:
  * Default mode network (DMN)
  * Salience network (SN)
  * Central executive network (CEN)
  * Sensorimotor network
- Visualize altered connections on brain surfaces

Step 8: Machine learning classification
- Train classifier to distinguish patients from controls
- Use scikit-learn Random Forest or SVM
- Features: connectivity values or network metrics
- Cross-validation (10-fold)
- Calculate accuracy, sensitivity, specificity, AUC
- Identify most discriminative features (connectivity edges)

Step 9: Graph neural network analysis with Torch Geometric
- Build graph neural network (GCN or GAT)
- Input: connectivity matrices as adjacency matrices
- Train to predict diagnosis
- Extract learned representations
- Visualize latent space (UMAP)
- Interpret which brain regions are most important

Step 10: Bayesian network modeling with PyMC
- Build directed graphical model of brain networks
- Estimate effective connectivity (directional influence)
- Incorporate prior knowledge about anatomical connections
- Perform posterior inference
- Identify key driver regions in disease

Step 11: Clinical correlation analysis
- Correlate network metrics with clinical scores:
  * Symptom severity
  * Cognitive performance
  * Treatment response
- Use Spearman or Pearson correlation
- Identify brain-behavior relationships

Step 12: Generate comprehensive neuroimaging report
- Brain connectivity matrices (patients vs controls)
- Statistical comparison maps on brain surface
- Network metric comparison bar plots
- Graph visualizations (circular or force-directed layout)
- Machine learning ROC curves
- Brain-behavior correlation plots
- Clinical interpretation:
  * Which networks are disrupted?
  * Relationship to symptoms
  * Potential biomarker utility
- Recommendations:
  * Brain regions for therapeutic targeting (TMS, DBS)
  * Network metrics as treatment response predictors
- Export publication-ready PDF with brain visualizations

Expected Output:
- Functional connectivity matrices for all subjects
- Statistical maps of altered connectivity
- Graph theory metrics
- Machine learning classification model
- Brain-behavior correlations
- Comprehensive neuroimaging report
```

---

## 环境微生物学

### 示例 15：环境样本的宏基因组分析

**目标**：表征环境 DNA 样本中的微生物群落组成和功能潜力。

**使用的技能**：
- `biopython` - 序列处理
- `pysam` - BAM 文件处理
- `ena-database` - 序列数据
- `uniprot-database` - 蛋白质注释
- `kegg-database` - 路径分析
- `etetoolkit` - 系统发育树
- `scikit-bio` - 微生物生态学
- `networkx` - 共现网络
- `statsmodels` - 多样性统计
- `matplotlib` - 可视化

**工作流程**：

```bash
Step 1: Load and QC metagenomic reads
- Load FASTQ files with BioPython
- Quality control with FastQC-equivalent:
  * Remove adapters and low-quality bases (Q < 20)
  * Filter short reads (< 50 bp)
  * Remove host contamination (if applicable)
- Subsample to even depth if comparing samples

Step 2: Taxonomic classification
- Use Kraken2-like approach or query ENA database
- Classify reads to taxonomic lineages
- Generate abundance table:
  * Rows: taxa (species or OTUs)
  * Columns: samples
  * Values: read counts or relative abundance
- Summarize at different levels: phylum, class, order, family, genus, species

Step 3: Calculate diversity metrics with scikit-bio
- Alpha diversity (within-sample):
  * Richness (number of species)
  * Shannon entropy
  * Simpson diversity
  * Chao1 estimated richness
- Beta diversity (between-sample):
  * Bray-Curtis dissimilarity
  * Weighted/unweighted UniFrac distance
  * Jaccard distance
- Rarefaction curves to assess sampling completeness

Step 4: Statistical comparison of communities
- Compare diversity between groups (e.g., polluted vs pristine)
- Use statsmodels for:
  * Mann-Whitney or Kruskal-Wallis tests (alpha diversity)
  * PERMANOVA for beta diversity (adonis test)
  * LEfSe for differential abundance testing
- Identify taxa enriched or depleted in each condition

Step 5: Build phylogenetic tree with ETE Toolkit
- Extract 16S rRNA sequences (or marker genes)
- Align sequences (MUSCLE/MAFFT equivalent)
- Build phylogenetic tree (neighbor-joining or maximum likelihood)
- Visualize tree colored by sample or environment
- Root tree with outgroup

Step 6: Co-occurrence network analysis
- Calculate pairwise correlations between taxa
- Use Spearman correlation to identify co-occurrence patterns
- Filter significant correlations (p < 0.01, |r| > 0.6)
- Build co-occurrence network with NetworkX
- Identify modules (communities of co-occurring taxa)
- Calculate network topology metrics
- Visualize network (nodes = taxa, edges = correlations)

Step 7: Functional annotation
- Assemble contigs from reads (if performing assembly)
- Predict genes with Prodigal-like tools
- Annotate genes using UniProt and KEGG
- Map proteins to KEGG pathways
- Generate functional profile:
  * Abundance of metabolic pathways
  * Key enzymes (nitrification, denitrification, methanogenesis)
  * Antibiotic resistance genes
  * Virulence factors

Step 8: Functional diversity analysis
- Compare functional profiles between samples
- Calculate pathway richness and evenness
- Identify enriched pathways with statistical testing
- Link taxonomy to function:
  * Which taxa contribute to which functions?
  * Use shotgun data to assign functions to taxa

Step 9: Search ENA for related environmental samples
- Query ENA for metagenomic studies from similar environments
- Download and compare to own samples
- Place samples in context of global microbiome diversity
- Identify unique vs ubiquitous taxa

Step 10: Environmental parameter correlation
- Correlate community composition with metadata:
  * Temperature, pH, salinity
  * Nutrient concentrations (N, P)
  * Pollutant levels (heavy metals, hydrocarbons)
- Use Mantel test to correlate distance matrices
- Identify environmental drivers of community structure

Step 11: Biomarker discovery
- Identify taxa or pathways that correlate with environmental condition
- Use Random Forest to find predictive features
- Validate biomarkers:
  * Sensitivity and specificity
  * Cross-validation across samples
- Propose taxa as bioindicators of environmental health

Step 12: Generate environmental microbiome report
- Taxonomic composition bar charts (stacked by phylum/class)
- Alpha and beta diversity plots (boxplots, PCoA)
- Phylogenetic tree with environmental context
- Co-occurrence network visualization
- Functional pathway heatmaps
- Environmental correlation plots
- Statistical comparison tables
- Biological interpretation:
  * Dominant taxa and their ecological roles
  * Functional potential of the community
  * Environmental factors shaping the microbiome
  * Biomarker taxa for monitoring
- Recommendations:
  * Biomarkers for environmental monitoring
  * Functional guilds for restoration
  * Further sampling or sequencing strategies
- Export comprehensive PDF report

Expected Output:
- Taxonomic profiles for all samples
- Diversity metrics and statistical comparisons
- Phylogenetic tree
- Co-occurrence network
- Functional annotation and pathway analysis
- Comprehensive microbiome report
```

---

## 传染病研究

### 示例 16：抗菌药物耐药性监测和预测

**目标**：跟踪抗菌药物耐药性趋势并根据基因组数据预测耐药表型。

**使用的技能**：
- `biopython` - 序列分析
- `pysam` - 基因组组装分析
- `ena-database` - 公共基因组数据
- `uniprot-database` - 抗性蛋白注释
- `gene-database` - 抗性基因目录
- `etetoolkit` - 系统发育分析
- `scikit-learn` - 阻力预测
- `networkx` - 传输网络
- `statsmodels` - 趋势分析
- `matplotlib` - 流行病学图

**工作流程**：

```bash
Step 1: Collect bacterial genome sequences
- Isolates from hospital surveillance program
- Load FASTA assemblies with BioPython
- Basic QC:
  * Assess assembly quality (N50, completeness)
  * Estimate genome size and coverage
  * Remove contaminated assemblies

Step 2: Species identification and MLST typing
- Perform in silico MLST (multi-locus sequence typing)
- Extract housekeeping gene sequences
- Assign sequence types (ST)
- Classify isolates into clonal complexes
- Identify high-risk clones (e.g., ST131 E. coli, ST258 K. pneumoniae)

Step 3: Antimicrobial resistance (AMR) gene detection
- Query NCBI Gene and UniProt for AMR gene databases
- Screen assemblies for resistance genes:
  * Beta-lactamases (blaTEM, blaCTX-M, blaKPC, blaNDM)
  * Aminoglycoside resistance (aac, aph, ant)
  * Fluoroquinolone resistance (gyrA, parC mutations)
  * Colistin resistance (mcr-1 to mcr-10)
  * Efflux pumps
- Calculate gene presence/absence matrix

Step 4: Resistance mechanism annotation
- Map detected genes to resistance classes:
  * Enzymatic modification (e.g., beta-lactamases)
  * Target modification (e.g., ribosomal methylation)
  * Target mutation (e.g., fluoroquinolone resistance)
  * Efflux pumps
- Query UniProt for detailed mechanism descriptions
- Link genes to antibiotic classes affected

Step 5: Build phylogenetic tree with ETE Toolkit
- Extract core genome SNPs
- Concatenate SNP alignments
- Build maximum likelihood tree
- Root with outgroup or midpoint rooting
- Annotate tree with:
  * Resistance profiles
  * Sequence types
  * Collection date and location

Step 6: Genotype-phenotype correlation
- Match genomic data with phenotypic susceptibility testing
- For each antibiotic, correlate:
  * Presence of resistance genes with MIC values
  * Target mutations with resistance phenotype
- Calculate sensitivity/specificity of genetic markers
- Identify discordant cases (false positives/negatives)

Step 7: Machine learning resistance prediction
- Train classification models with scikit-learn:
  * Features: presence/absence of resistance genes + mutations
  * Target: resistance phenotype (susceptible/intermediate/resistant)
  * Models: Logistic Regression, Random Forest, Gradient Boosting
- Train separate models for each antibiotic
- Cross-validate (stratified 5-fold)
- Calculate accuracy, precision, recall, F1 score
- Feature importance: which genes are most predictive?

Step 8: Temporal trend analysis
- Track resistance rates over time
- Use statsmodels for:
  * Mann-Kendall trend test
  * Joinpoint regression (identify change points)
  * Forecast future resistance rates (ARIMA)
- Analyze trends for each antibiotic class
- Identify emerging resistance mechanisms

Step 9: Transmission network inference
- Identify closely related isolates (< 10 SNPs difference)
- Build transmission network with NetworkX:
  * Nodes: isolates
  * Edges: putative transmission links
- Incorporate temporal and spatial data
- Identify outbreak clusters
- Detect super-spreaders (high degree nodes)
- Analyze network topology

Step 10: Search ENA for global context
- Query ENA for same species from other regions/countries
- Download representative genomes
- Integrate into phylogenetic analysis
- Assess whether local isolates are globally distributed clones
- Identify region-specific vs international resistance genes

Step 11: Plasmid and mobile element analysis
- Identify plasmid contigs
- Detect insertion sequences and transposons
- Track mobile genetic elements carrying resistance genes
- Identify conjugative plasmids facilitating horizontal gene transfer
- Build plasmid similarity networks

Step 12: Generate AMR surveillance report
- Summary statistics:
  * Number of isolates by species, ST, location
  * Resistance rates for each antibiotic
- Phylogenetic tree annotated with resistance profiles
- Temporal trend plots (resistance % over time)
- Transmission network visualizations
- Prediction model performance metrics
- Heatmap: resistance genes by isolate
- Geographic distribution map (if spatial data available)
- Interpretation:
  * Predominant resistance mechanisms
  * High-risk clones circulating
  * Temporal trends and emerging threats
  * Transmission clusters and outbreaks
- Recommendations:
  * Infection control measures for clusters
  * Antibiotic stewardship priorities
  * Resistance genes to monitor
  * Laboratories to perform confirmatory testing
- Export comprehensive PDF for public health reporting

Expected Output:
- AMR gene profiles for all isolates
- Phylogenetic tree with resistance annotations
- Temporal trends in resistance rates
- ML models for resistance prediction from genomes
- Transmission networks
- Comprehensive AMR surveillance report for public health
```

---

## 多组学整合

### 示例 17：癌症多组学数据的综合分析

**目标**：整合基因组学、转录组学、蛋白质组学和临床数据来确定癌症亚型和治疗策略。

**使用的技能**：
- `pydeseq2` - RNA-seq DE 分析
- `pysam` - 变体调用
- `ensembl-database` - 基因注释
- `cosmic-database` - 癌症突变
- `string-database` - 蛋白质相互作用
- `reactome-database` - 路径分析
- `opentargets-database` - 药物靶点
- `scikit-learn` - 聚类和分类
- `torch_geometric` - 图神经网络
- `umap-learn` - 降维
- `statsmodels` - 生存分析
- `pymoo` - 多目标优化

**工作流程**：
```bash
Step 1: Load and preprocess genomic data (WES/WGS)
- Parse VCF files with pysam
- Filter high-quality variants (QUAL > 30, DP > 20)
- Annotate with Ensembl VEP (missense, nonsense, frameshift)
- Query COSMIC for known cancer mutations
- Create mutation matrix: samples × genes (binary: mutated or not)
- Focus on cancer genes from COSMIC Cancer Gene Census

Step 2: Process transcriptomic data (RNA-seq)
- Load gene count matrix
- Run differential expression with PyDESeq2
- Compare tumor vs normal (if paired samples available)
- Normalize counts (TPM or FPKM)
- Identify highly variable genes
- Create expression matrix: samples × genes (log2 TPM)

Step 3: Load proteomic data (Mass spec)
- Protein abundance matrix from LC-MS/MS
- Normalize protein abundances (median normalization)
- Log2-transform
- Filter proteins detected in < 50% of samples
- Create protein matrix: samples × proteins

Step 4: Load clinical data
- Demographics: age, sex, race
- Tumor characteristics: stage, grade, histology
- Treatment: surgery, chemo, radiation, targeted therapy
- Outcome: overall survival (OS), progression-free survival (PFS)
- Response: complete/partial response, stable/progressive disease

Step 5: Data integration and harmonization
- Match sample IDs across omics layers
- Ensure consistent gene/protein identifiers
- Handle missing data:
  * Impute with KNN or median (for moderate missingness)
  * Remove features with > 50% missing
- Create multi-omics data structure (dictionary of matrices)

Step 6: Multi-omics dimensionality reduction
- Concatenate all omics features (genes + proteins + mutations)
- Apply UMAP with umap-learn for visualization
- Alternative: PCA or t-SNE
- Visualize samples in 2D space colored by:
  * Histological subtype
  * Stage
  * Survival (high vs low)
- Identify patterns or clusters

Step 7: Unsupervised clustering to identify subtypes
- Perform consensus clustering with scikit-learn
- Test k = 2 to 10 clusters
- Evaluate cluster stability and optimal k
- Assign samples to clusters (subtypes)
- Visualize clustering in UMAP space

Step 8: Characterize molecular subtypes
For each subtype:
- Differential expression analysis:
  * Compare subtype vs all others with PyDESeq2
  * Extract top differentially expressed genes and proteins
- Mutation enrichment:
  * Fisher's exact test for each gene
  * Identify subtype-specific mutations
- Pathway enrichment:
  * Query Reactome for enriched pathways
  * Query KEGG for metabolic pathway differences
  * Identify hallmark biological processes

Step 9: Build protein-protein interaction networks
- Query STRING database for interactions among:
  * Differentially expressed proteins
  * Products of mutated genes
- Construct PPI network with NetworkX
- Identify network modules (community detection)
- Calculate centrality metrics to find hub proteins
- Overlay fold changes on network for visualization

Step 10: Survival analysis by subtype
- Use statsmodels or lifelines for survival analysis
- Kaplan-Meier curves for each subtype
- Log-rank test for significance
- Cox proportional hazards model:
  * Covariates: subtype, stage, age, treatment
  * Estimate hazard ratios
- Identify prognostic subtypes

Step 11: Predict therapeutic response
- Train machine learning models with scikit-learn:
  * Features: multi-omics data
  * Target: response to specific therapy (responder/non-responder)
  * Models: Random Forest, XGBoost, SVM
- Cross-validation to assess performance
- Identify features predictive of response
- Calculate AUC and feature importance

Step 12: Graph neural network for integrated prediction
- Build heterogeneous graph with Torch Geometric:
  * Nodes: samples, genes, proteins, pathways
  * Edges: gene-protein, protein-protein, gene-pathway
  * Node features: expression, mutation status
- Train GNN to predict:
  * Subtype classification
  * Survival risk
  * Treatment response
- Extract learned embeddings for interpretation

Step 13: Identify therapeutic targets with Open Targets
- For each subtype, query Open Targets:
  * Input: upregulated genes/proteins
  * Extract target-disease associations
  * Prioritize by tractability score
- Search for FDA-approved drugs targeting identified proteins
- Identify clinical trials for relevant targets
- Propose subtype-specific therapeutic strategies

Step 14: Multi-objective optimization of treatment strategies
- Use PyMOO to optimize treatment selection:
  * Objectives:
    1. Maximize predicted response probability
    2. Minimize predicted toxicity
    3. Minimize cost
  * Constraints: patient eligibility, drug availability
- Generate Pareto-optimal treatment strategies
- Personalized treatment recommendations per patient

Step 15: Generate comprehensive multi-omics report
- Sample clustering and subtype assignments
- UMAP visualization colored by subtype, survival, mutations
- Subtype characterization:
  * Molecular signatures (genes, proteins, mutations)
  * Enriched pathways
  * PPI networks
- Kaplan-Meier survival curves by subtype
- ML model performance (AUC, confusion matrices)
- Feature importance plots
- Therapeutic target tables with supporting evidence
- Personalized treatment recommendations
- Clinical implications:
  * Prognostic biomarkers
  * Predictive biomarkers for therapy selection
  * Novel drug targets
- Export publication-quality PDF with all figures and tables

Expected Output:
- Integrated multi-omics dataset
- Cancer subtype classification
- Molecular characterization of subtypes
- Survival analysis and prognostic markers
- Predictive models for treatment response
- Therapeutic target identification
- Personalized treatment strategies
- Comprehensive integrative genomics report
```

---

## 实验物理与数据分析

### 示例 18：粒子物理探测器数据分析

**目标**：分析粒子探测器的实验数据以识别信号事件并测量物理常数。

**使用的技能**：
- `astropy` - 单位和常数
- `sympy` - 符号数学
- `scipy` - 统计分析
- `scikit-learn` - 分类
- `stable-baselines3` - 用于优化的强化学习
- `matplotlib` - 可视化
- `seaborn` - 统计图
- `statsmodels` - 假设检验
- `dask` - 大规模数据处理
- `vaex` - 核心外数据帧

**工作流程**：

```bash
Step 1: Load and inspect detector data
- Load ROOT files or HDF5 with raw detector signals
- Use Vaex for out-of-core processing (TBs of data)
- Inspect data structure: event IDs, timestamps, detector channels
- Extract key observables:
  * Energy deposits in calorimeters
  * Particle trajectories from tracking detectors
  * Time-of-flight measurements
  * Trigger information

Step 2: Apply detector calibration and corrections
- Load calibration constants
- Apply energy calibrations to convert ADC to physical units
- Correct for detector efficiency variations
- Apply geometric corrections (alignment)
- Use Astropy units for unit conversions (eV, GeV, MeV)
- Account for dead time and detector acceptance

Step 3: Event reconstruction
- Cluster energy deposits to form particle candidates
- Reconstruct particle trajectories (tracks)
- Match tracks to calorimeter clusters
- Calculate invariant masses for particle identification
- Compute momentum and energy for each particle
- Use Dask for parallel processing across events

Step 4: Event selection and filtering
- Define signal region based on physics hypothesis
- Apply quality cuts:
  * Track quality (chi-squared, number of hits)
  * Fiducial volume cuts
  * Timing cuts (beam window)
  * Particle identification cuts
- Estimate trigger efficiency
- Calculate event weights for corrections

Step 5: Background estimation
- Identify background sources:
  * Cosmic rays
  * Beam-related backgrounds
  * Detector noise
  * Physics backgrounds (non-signal processes)
- Simulate backgrounds using Monte Carlo (if available)
- Estimate background from data in control regions
- Use sideband subtraction method

Step 6: Signal extraction
- Fit invariant mass distributions to extract signal
- Use scipy for likelihood fitting:
  * Signal model: Gaussian or Breit-Wigner
  * Background model: polynomial or exponential
  * Combined fit with maximum likelihood
- Calculate signal significance (S/√B or Z-score)
- Estimate systematic uncertainties

Step 7: Machine learning event classification
- Train classifier with scikit-learn to separate signal from background
- Features: kinematic variables, topology, detector response
- Models: Boosted Decision Trees (XGBoost), Neural Networks
- Cross-validate with k-fold CV
- Optimize selection criteria using ROC curves
- Calculate signal efficiency and background rejection

Step 8: Reinforcement learning for trigger optimization
- Use Stable-Baselines3 to optimize trigger thresholds
- Environment: detector simulator
- Action: adjust trigger thresholds
- Reward: maximize signal efficiency while controlling rate
- Train PPO or SAC agent
- Validate on real data

Step 9: Calculate physical observables
- Measure cross-sections:
  * σ = N_signal / (ε × L × BR)
  * N_signal: number of signal events
  * ε: detection efficiency
  * L: integrated luminosity
  * BR: branching ratio
- Use Sympy for symbolic error propagation
- Calculate with Astropy for proper unit handling

Step 10: Statistical analysis and hypothesis testing
- Perform hypothesis tests with statsmodels:
  * Likelihood ratio test for signal vs background-only
  * Calculate p-values and significance levels
  * Set confidence limits (CLs method)
- Bayesian analysis for parameter estimation
- Calculate confidence intervals and error bands

Step 11: Systematic uncertainty evaluation
- Identify sources of systematic uncertainty:
  * Detector calibration uncertainties
  * Background estimation uncertainties
  * Theoretical uncertainties (cross-sections, PDFs)
  * Monte Carlo modeling uncertainties
- Propagate uncertainties through analysis chain
- Combine statistical and systematic uncertainties
- Present as error budget

Step 12: Create comprehensive physics report
- Event displays showing candidate signal events
- Kinematic distributions (momentum, energy, angles)
- Invariant mass plots with fitted signal
- ROC curves for ML classifiers
- Cross-section measurements with error bars
- Comparison with theoretical predictions
- Systematic uncertainty breakdown
- Statistical significance calculations
- Interpretation:
  * Consistency with Standard Model
  * Constraints on new physics parameters
  * Discovery potential or exclusion limits
- Recommendations:
  * Detector improvements
  * Additional data needed
  * Future analysis strategies
- Export publication-ready PDF formatted for physics journal

Expected Output:
- Reconstructed physics events
- Signal vs background classification
- Measured cross-sections and branching ratios
- Statistical significance of observations
- Systematic uncertainty analysis
- Comprehensive experimental physics paper
```

---

## 化学工程与工艺优化

### 实施例 19：化学反应器设计和操作的优化

**目标**：设计和优化连续化学反应器，以实现最大产量和效率，同时满足安全和经济限制。

**使用的技能**：
- `sympy` - 符号方程和反应动力学
- `scipy` - 数值积分和优化
- `pymoo` - 多目标优化
- `simpy` - 过程模拟
- `pymc` - 贝叶斯参数估计
- `scikit-learn` - 流程建模
- `stable-baselines3` - 实时控制优化
- `matplotlib` - 流程图
- `reportlab` - 工程报告

**工作流程**：

```bash
Step 1: Define reaction system and kinetics
- Chemical reaction: A + B → C + D
- Use Sympy to define symbolic rate equations:
  * Arrhenius equation: k = A × exp(-Ea/RT)
  * Rate law: r = k × [A]^α × [B]^β
- Define material and energy balances symbolically
- Include equilibrium constants and thermodynamics
- Account for side reactions and byproducts

Step 2: Develop reactor model
- Select reactor type: CSTR, PFR, batch, or semi-batch
- Write conservation equations:
  * Mass balance: dC/dt = (F_in × C_in - F_out × C)/V + r
  * Energy balance: ρCp × dT/dt = Q - ΔH_rxn × r × V
  * Momentum balance (pressure drop)
- Include heat transfer correlations
- Model mixing and mass transfer limitations

Step 3: Parameter estimation with PyMC
- Load experimental data from pilot reactor
- Bayesian inference to estimate kinetic parameters:
  * Pre-exponential factor (A)
  * Activation energy (Ea)
  * Reaction orders (α, β)
- Use MCMC sampling with PyMC
- Incorporate prior knowledge from literature
- Calculate posterior distributions and credible intervals
- Assess parameter uncertainty and correlation

Step 4: Model validation
- Simulate reactor with estimated parameters using scipy.integrate
- Compare predictions with experimental data
- Calculate goodness of fit (R², RMSE)
- Perform sensitivity analysis:
  * Which parameters most affect yield?
  * Identify critical operating conditions
- Refine model if needed

Step 5: Machine learning surrogate model
- Train fast surrogate model with scikit-learn
- Generate training data from detailed model (1000+ runs)
- Features: T, P, residence time, feed composition, catalyst loading
- Target: yield, selectivity, conversion
- Models: Gaussian Process Regression, Random Forest
- Validate surrogate accuracy (R² > 0.95)
- Use for rapid optimization

Step 6: Single-objective optimization
- Maximize yield with scipy.optimize:
  * Decision variables: T, P, feed ratio, residence time
  * Objective: maximize Y = (moles C produced) / (moles A fed)
  * Constraints:
    - Temperature: 300 K ≤ T ≤ 500 K (safety)
    - Pressure: 1 bar ≤ P ≤ 50 bar (equipment limits)
    - Residence time: 1 min ≤ τ ≤ 60 min
    - Conversion: X_A ≥ 90%
- Use Sequential Least Squares Programming (SLSQP)
- Identify optimal operating point

Step 7: Multi-objective optimization with PyMOO
- Competing objectives:
  1. Maximize product yield
  2. Minimize energy consumption (heating/cooling)
  3. Minimize operating cost (raw materials, utilities)
  4. Maximize reactor productivity (throughput)
- Constraints:
  - Safety: temperature and pressure limits
  - Environmental: waste production limits
  - Economic: minimum profitability
- Run NSGA-II or NSGA-III
- Generate Pareto front of optimal solutions
- Select operating point based on preferences

Step 8: Dynamic process simulation with SimPy
- Model complete plant:
  * Reactors, separators, heat exchangers
  * Pumps, compressors, valves
  * Storage tanks and buffers
- Simulate startup, steady-state, and shutdown
- Include disturbances:
  * Feed composition variations
  * Equipment failures
  * Demand fluctuations
- Evaluate dynamic stability
- Calculate time to steady state

Step 9: Control system design
- Design feedback control loops:
  * Temperature control (PID controller)
  * Pressure control
  * Flow control
  * Level control
- Tune PID parameters using Ziegler-Nichols or optimization
- Implement cascade control for improved performance
- Add feedforward control for disturbance rejection

Step 10: Reinforcement learning for advanced control
- Use Stable-Baselines3 to train RL agent:
  * Environment: reactor simulation (SimPy-based)
  * State: T, P, concentrations, flow rates
  * Actions: adjust setpoints, flow rates, heating/cooling
  * Reward: +yield -energy cost -deviation from setpoint
- Train PPO or TD3 agent
- Compare with conventional PID control
- Evaluate performance under disturbances
- Implement model-free adaptive control

Step 11: Economic analysis
- Calculate capital costs (CAPEX):
  * Reactor vessel cost (function of size, pressure rating)
  * Heat exchanger costs
  * Pumps and instrumentation
  * Installation costs
- Calculate operating costs (OPEX):
  * Raw materials (A, B, catalyst)
  * Utilities (steam, cooling water, electricity)
  * Labor and maintenance
- Revenue from product sales
- Calculate economic metrics:
  * Net present value (NPV)
  * Internal rate of return (IRR)
  * Payback period
  * Levelized cost of production

Step 12: Safety analysis
- Identify hazards:
  * Exothermic runaway reactions
  * Pressure buildup
  * Toxic or flammable materials
- Perform HAZOP-style analysis
- Calculate safe operating limits:
  * Maximum temperature of synthesis reaction (MTSR)
  * Adiabatic temperature rise
  * Relief valve sizing
- Design emergency shutdown systems
- Implement safety interlocks

Step 13: Uncertainty quantification
- Propagate parameter uncertainties from PyMC:
  * How does kinetic parameter uncertainty affect yield?
  * Monte Carlo simulation with parameter distributions
- Evaluate robustness of optimal design
- Calculate confidence intervals on economic metrics
- Identify critical uncertainties for further study

Step 14: Generate comprehensive engineering report
- Executive summary of project objectives and results
- Process flow diagram (PFD) with material and energy streams
- Reaction kinetics and model equations
- Parameter estimation results with uncertainties
- Optimization results:
  * Pareto front for multi-objective optimization
  * Recommended operating conditions
  * Trade-off analysis
- Dynamic simulation results (startup curves, response to disturbances)
- Control system design and tuning
- Economic analysis with sensitivity to key assumptions
- Safety analysis and hazard mitigation
- Scale-up considerations:
  * Pilot to commercial scale
  * Heat and mass transfer limitations
  * Equipment sizing
- Recommendations:
  * Optimal reactor design (size, type, materials of construction)
  * Operating conditions for maximum profitability
  * Control strategy
  * Further experimental studies needed
- Technical drawings and P&ID (piping and instrumentation diagram)
- Export as professional engineering report (PDF)

Expected Output:
- Validated reactor model with parameter uncertainties
- Optimal reactor design and operating conditions
- Pareto-optimal solutions for multi-objective optimization
- Dynamic process simulation results
- Advanced control strategies (RL-based)
- Economic feasibility analysis
- Safety assessment
- Comprehensive chemical engineering design report
```

---

## 总结

这些例子表明：

1. **跨领域适用性**：技能在许多科学领域都有用
2. **技能集成**：复杂的工作流程结合了多个数据库、包和分析方法
3. **现实世界的相关性**：解决实际研究问题和临床需求的示例
4. **端到端工作流程**：从数据采集到可发布的报告
5. **最佳实践**：质量控制、统计严谨性、可视化、解释和文档

### 如何使用这些示例

1. **适应您的需求**：针对您的具体研究问题修改参数、数据集和目标
2. **创造性地组合技能**：混合搭配不同类别的技能
3. **遵循结构**：每个示例都提供了清晰的分步工作流程
4. **生成全面的输出**：以出版质量的数据和专业报告为目标
5. **引用您的来源**：始终验证数据并提供正确的引用

### 附加说明

- 始终以：“尽可能使用可用的‘技能’。保持输出井井有条。”
- 对于复杂的项目，分解为可管理的步骤并验证中间结果
- 保存检查点和中间数据文件
- 记录参数和可重复性决策
- 生成解释方法的自述文件
- 创建 PDF 以供利益相关者沟通

这些示例展示了结合该存储库中的技能来解决跨多个领域的复杂的、现实世界的科学挑战的力量。