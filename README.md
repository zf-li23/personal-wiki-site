# 个人维基网站 (Personal Wiki Site)

这是一个基于 React, Vite 和 Tailwind CSS 构建的个人知识库和作品集网站。设计目标是易于部署到 GitHub Pages，并提供类似 GitBook 的阅读体验。

## 功能特点

-   **维基系统**: 支持无限层级的文档结构，自动生成侧边栏导航。
-   **Markdown 支持**: 使用 Markdown 编写内容，支持代码高亮和 GFM 语法。
-   **数学公式支持**: 集成 KaTeX，支持 LaTeX 数学公式（行内 `$`, `\(` 和 行间 `$$`, `\[`）。
-   **代码增强**: 代码块支持语法高亮、一键复制，行内代码优化样式。
-   **目录导航 (TOC)**: 自动生成当前页面的右侧/文内目录。
-   **深色/浅色模式**: 跟随系统设置自动切换，也支持手动切换。
-   **响应式设计**: 适配移动端和桌面端。
-   **GitHub Pages 部署**: 预配置了部署脚本，一键发布。
-   **严格结构验证**: 构建时自动检查文件编号与层级结构的一致性。

## 技术栈

-   **框架**: React 18 + Vite
-   **语言**: TypeScript
-   **样式**: Tailwind CSS + Tailwind Typography
-   **路由**: React Router DOM v6
-   **Markdown**: react-markdown, remark-gfm, remark-math, rehype-highlight, rehype-katex
-   **图标**: Lucide React

## 项目结构

```
personal-wiki-site/
├── docs/
│   └── wiki/            # [核心] 你的 Markdown 文档放在这里
│       ├── 1.离散数学/
│       │   ├── index.md # 对应 "1.离散数学" 页面
│       │   ├── 1.1.数理逻辑/
│       │   │   └── index.md # 对应 "1.1.数理逻辑" 页面
│       │   └── ...
├── src/
│   ├── components/      # UI 组件
│   ├── data/
│   │   └── wikiData.ts  # 自动读取 docs/wiki/ 下的 md 文件并生成路由数据
│   ├── pages/           # 页面组件
│   └── ...
├── ...
```

## 如何添加内容

1.  **文件夹结构**: 在 `docs/wiki/` 下创建文件夹，文件夹名称必须包含编号（如 `1.离散数学`）。
2.  **内容文件**: 在每个文件夹内创建 `index.md` 作为该章节的内容。
3.  **严格编号**: 
    -   文件夹名称必须以数字编号开头（如 `1.1.数理逻辑`）。
    -   子文件夹的编号必须是父文件夹编号的延伸（如 `1.1` 的子文件夹必须是 `1.1.x`）。
    -   构建脚本 (`scripts/validate-wiki.js`) 会在编译时严格检查此规则，不符合规范将导致构建失败。
4.  **标题显示**: 页面标题会自动根据路径生成，格式为 `祖先1 - 祖先2 - 相对编号.标题`。

## 数学公式与代码

-   **行内公式**: 使用 `$E=mc^2$` 或 `\(E=mc^2\)`。
-   **行间公式**: 使用 `$$` 或 `\[` 包裹。
-   **代码块**: 使用标准 Markdown 语法，右上角提供复制按钮。

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
