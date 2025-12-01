请使用 Claude Code 对我的项目进行完整初始化，包括以下步骤：

## 第一步：创建并配置 CLAUDE.md 文件

- 将 CLAUDE.md 文件内容翻译为中文
- 在文件中添加以下个人环境信息：
  - **设备**：搭载 Apple 芯片的 Mac 电脑
  - **Node.js 管理**：通过 bun 进行安装管理
  - **Python 环境**：通过 uv 配置
  - **Git代码托管平台**：github.com
  - **版本管理**： 对于任何大的变动自动创建一个tag，采取语义版本号管理方法，首次提交的版本号为v0.0.1，后续递增tag版本号0.0.1位
- 请确保所有后续沟通和回复都使用中文

## 第二步：初始化 Git 仓库

- 初始化 Git 仓库

## 第三步：创建完整的 .gitignore 文件

需要包含以下忽略项：

### 系统文件
- `.DS_Store`

### Node.js 相关
- 所有 `node_modules/` 目录
- `bun.lockb`
- `npm-debug.log*`
- `yarn-debug.log*`
- `yarn-error.log*`

### Python 相关
- `.venv/`
- `__pycache__/`
- `.pytest_cache/`

### Next.js 项目
- `.next/`
- `out/`
- `build/`

### 环境变量文件
- `.env.local`
- `.env.development.local`
- `.env.test.local`
- `.env.production.local`

## 第四步：提供项目初始化状态报告

完成上述所有设置后，请提供一个清晰的项目初始化状态报告。
