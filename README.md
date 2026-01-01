# 个人维基网站 (Personal Wiki Site)

这是一个基于 React, Vite 和 Tailwind CSS 构建的个人知识库和作品集网站。设计目标是易于部署到 GitHub Pages，并提供类似 GitBook 的阅读体验。

## 功能特点

-   **维基系统**: 支持无限层级的文档结构，自动生成侧边栏导航。
-   **Markdown 支持**: 使用 Markdown 编写内容，支持代码高亮和 GFM 语法。
-   **目录导航 (TOC)**: 自动生成当前页面的右侧/文内目录。
-   **深色/浅色模式**: 跟随系统设置自动切换，也支持手动切换。
-   **响应式设计**: 适配移动端和桌面端。
-   **GitHub Pages 部署**: 预配置了部署脚本，一键发布。
-   **文件驱动**: 像 Jekyll 一样，通过在 `wiki/` 目录下创建 Markdown 文件来添加内容，无需修改代码。

## 技术栈

-   **框架**: React 18 + Vite
-   **语言**: TypeScript
-   **样式**: Tailwind CSS + Tailwind Typography
-   **路由**: React Router DOM v6
-   **Markdown**: react-markdown, remark-gfm, rehype-highlight
-   **图标**: Lucide React

## 项目结构

```
personal-wiki-site/
├── docs/
│   └── wiki/            # [核心] 你的 Markdown 文档放在这里
│       ├── 1.离散数学/
│       │   ├── 1.1.数理逻辑.md
│       │   └── 1.1.数理逻辑/
│       │       └── 1.1.1.数理逻辑与命题的基本概念.md
│       └── ...
├── src/
│   ├── components/      # UI 组件
│   ├── data/
│   │   └── wikiData.ts  # 自动读取 docs/wiki/ 下的 md 文件并生成路由数据
│   ├── pages/           # 页面组件
│   └── ...
├── ...
```

## 如何添加内容

1.  在项目根目录的 `docs/wiki/` 文件夹中创建 Markdown 文件 (`.md`)。
2.  **文件命名**: 必须严格遵循 `数字.标题.md` 的格式（如 `1.1.数理逻辑.md`）。
3.  **双保险机制**: 文件名中的编号必须与文件夹层级结构一致。例如，`1.1.1.xxx.md` 必须位于 `1.1.xxx` 文件夹内，而该文件夹必须位于 `1.xxx` 文件夹内。如果不一致，控制台会输出警告。
4.  **层级**: 创建文件夹来建立层级结构。文件夹内的文件将作为子页面显示。

## 开发与部署

1.  **安装依赖**
    ```bash
    pnpm install
    ```

2.  **启动开发服务器**
    ```bash
    pnpm dev
    ```

3.  **构建与部署**
    本项目使用 `gh-pages` 分支进行部署。
    *   **main 分支**: 存放源代码。
    *   **gh-pages 分支**: 存放构建后的静态文件（由脚本自动生成）。

    **部署步骤**:
    ```bash
    pnpm run deploy
    ```
    此命令会自动执行构建 (`pnpm build`) 并将 `dist` 目录推送到 `gh-pages` 分支。

## 常见问题

### 为什么有两个分支？
-   `main`: 是你的**源码**，包含 React 组件、TypeScript 代码和原始 Markdown 文档。你应该在这里进行所有的编辑和提交。
-   `gh-pages`: 是**发布代码**，包含经过 Vite 编译、压缩后的 HTML/CSS/JS 文件。浏览器只能运行这些编译后的代码。你**不需要**手动修改这个分支，部署脚本会处理一切。

### 为什么 gh-pages 文件很少？
因为它只包含编译后的产物（通常是一个 `index.html` 和 `assets` 文件夹），源码中的 TypeScript、React 组件等都被打包成了浏览器可识别的最小化 JavaScript 文件。

## 许可证

MIT
