---
name: generate-image
description: 使用 AI 模型（FLUX、Gemini）生成或编辑图像。用于科学插图、图表、示意图、信息图、概念可视化和艺术图像。支持图像编辑以修改现有图像（更改颜色、添加/移除元素、风格转换）。适用于图表、海报和视觉解释。
---

# Generate Image

使用 OpenRouter 的图像生成模型生成和编辑高质量图像，包括 FLUX.2 Pro 和 Nano Banana Pro (Gemini 3 Pro)。

## 快速开始

使用 `scripts/generate_image.py` 脚本来生成或编辑图像：

```bash
# 生成新图像
python scripts/generate_image.py "A beautiful sunset over mountains"

# 编辑现有图像
python scripts/generate_image.py "Make the sky purple" --input photo.jpg
```

这会在当前目录中生成/编辑图像并保存为 `generated_image.png`。

## API 密钥设置

**关键**：脚本需要 OpenRouter API 密钥。运行前，检查用户是否已配置其 API 密钥：

1. 在项目目录或父目录中查找 `.env` 文件
2. 在 `.env` 文件中查找 `OPENROUTER_API_KEY=<key>`
3. 如果未找到，告知用户需要：
   - 创建带有 `OPENROUTER_API_KEY=your-api-key-here` 的 `.env` 文件
   - 或设置环境变量：`export OPENROUTER_API_KEY=your-api-key-here`
   - 从 https://openrouter.ai/keys 获取 API 密钥

脚本会自动检测 `.env` 文件，如果缺少 API 密钥则提供清晰的错误消息。

## 模型选择

**默认模型**：`google/gemini-3-pro-image-preview`（高质量，推荐）

**可用于生成和编辑的模型**：
- `google/gemini-3-pro-image-preview` - 高质量，支持生成 + 编辑
- `black-forest-labs/flux.2-pro` - 快速，高质量，支持生成 + 编辑

**仅生成**：
- `black-forest-labs/flux.2-dev` - 开发版本，仅生成

根据以下条件选择：
- **质量**：使用 gemini-3-pro 或 flux.2-pro
- **编辑**：使用 gemini-3-pro 或 flux.2-pro（都支持图像编辑）
- **成本**：仅生成使用 flux.2-dev

## 常见使用模式

### 基础生成
```bash
python scripts/generate_image.py "Your prompt here"
```

### 指定模型
```bash
python scripts/generate_image.py "A cat in space" --model "black-forest-labs/flux.2-pro"
```

### 自定义输出路径
```bash
python scripts/generate_image.py "Abstract art" --output artwork.png
```

### 编辑现有图像
```bash
python scripts/generate_image.py "Make background blue" --input photo.jpg
```

### 使用特定模型编辑
```bash
python scripts/generate_image.py "Add sunglasses to person" --input portrait.png --model "black-forest-labs/flux.2-pro"
```

### 使用自定义输出编辑
```bash
python scripts/generate_image.py "Remove text from image" --input screenshot.png --output cleaned.png
```

### 多张图像
使用不同提示或输出路径多次运行脚本：
```bash
python scripts/generate_image.py "Image 1 description" --output image1.png
python scripts/generate_image.py "Image 2 description" --output image2.png
```

## 脚本参数

- `prompt`（必需）：要生成的图像的文本描述，或编辑指令
- `--input` 或 `-i`：用于编辑的输入图像路径（启用编辑模式）
- `--model` 或 `-m`：OpenRouter 模型 ID（默认：google/gemini-3-pro-image-preview）
- `--output` 或 `-o`：输出文件路径（默认：generated_image.png）
- `--api-key`：OpenRouter API 密钥（覆盖 .env 文件）

## 错误处理

脚本为以下情况提供清晰的错误消息：
- 缺少 API 密钥（附带设置说明）
- API 错误（附带状态代码）
- 意外的响应格式
- 缺少依赖项（requests 库）

如果脚本失败，请阅读错误消息并在重试之前解决问题。

## 注意事项

- 图像以 base64 编码的数据 URL 形式返回，并自动保存为 PNG 文件
- 脚本支持来自不同 OpenRouter 模型的 `images` 和 `content` 响应格式
- 生成时间因模型而异（通常 5-30 秒）
- 对于图像编辑，输入图像被编码为 base64 并发送给模型
- 支持的输入图像格式：PNG、JPEG、GIF、WebP
- 查看 OpenRouter 定价了解成本信息：https://openrouter.ai/models

## 图像编辑技巧

- 具体说明您想要的更改（例如，"将天空更改为日落颜色" vs "编辑天空"）
- 如果可能，引用图像中的特定元素
- 为获得最佳效果，使用清晰详细的编辑指令
- Gemini 3 Pro 和 FLUX.2 Pro 都通过 OpenRouter 支持图像编辑