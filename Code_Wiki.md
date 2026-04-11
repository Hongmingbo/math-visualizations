# Math Visualizations (AIClaw) - Code Wiki

## 1. 项目整体架构 (Project Architecture)
本项目是一个基于原生前端技术（Vanilla HTML, CSS, JavaScript）构建的数学函数可视化教学工具集。项目采用**多页应用（MPA）**架构，将不同的数学概念（如一次函数、二次函数、反比例函数、三角函数）拆分到独立的HTML文件中。

### 架构特点：
- **零构建工具**：未使用 Webpack, Vite 等构建工具，开箱即用。
- **无前端框架**：不依赖 React, Vue, jQuery 等第三方库，完全使用原生 DOM API 和 HTML5 Canvas 绘图。
- **单文件组件化模式**：每个 HTML 文件自包含其所需的 HTML 结构、内联 CSS 样式（支持响应式布局、Flexbox/Grid）和 JavaScript 绘图逻辑，便于分发和独立演示。

---

## 2. 主要模块职责 (Main Module Responsibilities)
项目主要包含四个核心的可视化模块（页面）：

1. **`inverse-function.html` (反比例函数可视化)**
   - **职责**：展示 $y = k/x$ 的双曲线图像。
   - **核心功能**：支持通过滑块调节比例系数 $k$ 和坐标轴显示范围；实时计算并展示函数所在的象限分布、单调性以及渐近线位置；支持用户输入自定义解析式进行绘制。

2. **`linear-function-pro.html` (一次函数专业版)**
   - **职责**：深入解析 $y = kx + b$ 的直线图像。
   - **核心功能**：支持调节斜率 $k$ 和截距 $b$；高亮显示与 $x$ 轴、$y$ 轴的交点坐标；实时分析直线的单调性；提供特殊直线的快捷演示（如 $y=x$, 水平线等）。

3. **`quadratic-visualizer.html` (二次函数可视化)**
   - **职责**：动态演示 $y = ax^2 + bx + c$ 的抛物线图像。
   - **核心功能**：支持调节二次项、一次项和常数项系数；动态计算并标注顶点坐标、对称轴方程、开口方向及极值；支持鼠标悬停时在画布上实时显示坐标点（Mouse Tracking）。

4. **`trigonometry-visualizer.html` (三角函数可视化)**
   - **职责**：综合展示正弦 ($\sin$)、余弦 ($\cos$) 和正切 ($\tan$) 函数的周期性规律。
   - **核心功能**：采用**双画布联动**设计，左侧展示单位圆（Unit Circle）上的动点投影，右侧同步绘制笛卡尔坐标系下的函数波形；支持调节角度 $\theta$、振幅 $A$ 和周期 $\omega$。

---

## 3. 关键类与函数说明 (Key Functions)
由于项目采用原生 JS 编写，主要依赖函数式编程范式，各页面中复用了以下核心函数架构：

### 3.1 解析与用户输入处理
- **`parseFunction(expr)`**
  - **功能**：解析用户输入的自定义数学表达式字符串。
  - **实现**：将输入中的空格移除，将 `^` 替换为 `**`，并返回一个闭包函数，内部通过 `eval()` 动态计算 $x$ 对应的 $y$ 值。
- **`applyCustom()` / `clearCustom()`**
  - **功能**：将用户输入的自定义函数应用到画布，或清除自定义函数恢复标准模式。

### 3.2 绘图引擎 (Canvas API)
- **`draw()`**
  - **功能**：核心渲染主循环（Render Loop）。
  - **流程**：
    1. 清空画布 (`ctx.clearRect` 或 `ctx.fillRect`)。
    2. 绘制坐标系背景，包括网格线、$x$ 轴、$y$ 轴、箭头及刻度值。
    3. 根据当前滑块参数（如 $k, b$ 或 $a, b, c$）或自定义函数，通过步进循环计算轨迹点，使用 `moveTo` 和 `lineTo` 连线并 `stroke()` 绘制曲线。
    4. 调用 `updateInfo()` 更新侧边栏数学属性。
- **`resize()` / `resizeCanvas()`**
  - **功能**：监听窗口 `resize` 事件，动态调整 Canvas 的 `width` 和 `height` 属性以匹配 DOM 元素的实际像素大小，防止图像拉伸模糊，并触发重绘。

### 3.3 数学属性计算与 DOM 更新
- **`updateInfo(...)`**
  - **功能**：根据当前的数学参数，实时计算数学特征（如截距、顶点、象限、单调性），并将结果更新到对应的 HTML DOM 节点（如信息面板卡片）中。
- **`getValues()`**
  - **功能**：获取页面上各类 `<input type="range">` 滑块的当前实时数值。

### 3.4 三角函数特有函数 (`trigonometry-visualizer.html`)
- **`drawCircle(angle, amplitude)`**：专门用于在左侧画布上绘制单位圆、当前角度的半径线以及到坐标轴的投影虚线。
- **`drawGraph(angle, amplitude, omega)`**：在右侧画布上绘制标准的三角函数展开波形，并用圆点标记当前角度所处的相位位置。
- **`getFuncValue(angle, amp, omega)`**：根据当前选中的 Tab（sin/cos/tan）计算对应的三角函数 $y$ 值。

---

## 4. 依赖关系 (Dependencies)
本项目贯彻了极简主义，**没有任何外部依赖**：
- **UI 渲染**：原生 HTML5 + CSS3 (CSS Variables, Flexbox, CSS Grid, Gradients)。
- **交互逻辑**：Vanilla JavaScript (ES6+)。
- **图形绘制**：HTML5 `<canvas>` API (`CanvasRenderingContext2D`)。
- **字体**：依赖系统默认字体 (`'Segoe UI', 'Microsoft YaHei', sans-serif`)。

不需要安装 Node.js、NPM 包或任何第三方 CDN 链接即可运行。

---

## 5. 项目运行方式 (How to Run)
由于项目是纯静态的客户端前端应用，运行方式非常简单：

### 方法一：直接本地打开（最简单）
1. 在文件管理器中打开项目目录。
2. 双击任意 `.html` 文件（如 `linear-function-pro.html`）。
3. 文件将自动在系统默认的现代浏览器（如 Chrome, Edge, Firefox, Safari）中打开并运行。

### 方法二：使用本地开发服务器（推荐，体验更好）
虽然直接打开文件即可运行，但为了避免某些浏览器对本地文件 (`file://` 协议) 的安全限制（如跨域或模块加载限制，尽管本项目暂未涉及），推荐使用轻量级 HTTP 服务器：
- **VS Code 插件**：安装并使用 `Live Server` 插件，右键点击 HTML 文件选择 "Open with Live Server"。
- **Python 快速启动**：
  在项目根目录下运行以下命令（需已安装 Python）：
  ```bash
  # Python 3.x
  python -m http.server 8000
  ```
  然后在浏览器中访问 `http://localhost:8000/`，点击对应的 HTML 文件即可预览。
- **Node.js 快速启动**：
  ```bash
  npx serve .
  # 或
  npx http-server
  ```
