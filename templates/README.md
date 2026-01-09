# 美赛论文模板使用指南

> 📺 **强烈建议**：先在B站搜索「**美赛LaTeX教程**」或「**Overleaf使用教程**」看10-30分钟视频！
> 
> 推荐关键词：美赛LaTeX模板 | MCM论文写作 | Overleaf教程 | mcmthesis使用

---

## 📂 模板文件结构

```
templates/
├── README.md                    # 本文件（一站式教程）
├── LATEX_CHEATSHEET.md          # LaTeX命令速查表
├── latex/mcmthesis/             # LaTeX模板
│   ├── mcmthesis.cls           # ⭐ 核心类文件（必需）
│   ├── mcmthesis-demo.tex      # 示例文件
│   └── mcmthesis-demo.pdf      # 效果预览
└── word/
    └── MCM_Template.docx        # Word模板
```

---

## 🚀 快速开始（5分钟）

### 方式1：LaTeX + Overleaf（推荐）⭐

**为什么选择LaTeX？**
- ✅ 排版专业（O奖论文几乎都用LaTeX）
- ✅ 公式美观、自动编号
- ✅ 团队协作（实时多人编辑）
- ✅ 自动保存

**3步开始：**

```
Step 1: 注册Overleaf
→ 访问 https://www.overleaf.com
→ 用邮箱注册（免费）

Step 2: 创建项目
→ 点击「New Project」→「Blank Project」
→ 命名：MCM2026

Step 3: 上传模板
→ 点击左上角「Upload」图标
→ 上传这2个文件：
   ✓ latex/mcmthesis/mcmthesis.cls
   ✓ latex/mcmthesis/mcmthesis-demo.tex
→ 参考demo文件开始写作！
```

**团队协作：**
```
→ 点击右上角「Share」
→ 输入队友邮箱邀请
→ 实时协作编辑（类似腾讯文档）
⚠️ 免费版只能邀请1人，3人协作需升级或用教育邮箱
```

---

### 方式2：Word模板（简单但不推荐）

```
打开：word/MCM_Template.docx
填写摘要页，开始写作

⚠️ 注意：Word排版不如LaTeX专业，O奖论文很少用Word
```

---

### 方式3：VSCode本地（推荐熟手）

**需要配置：**
1. 安装LaTeX环境：MacTeX (Mac) / MiKTeX (Windows)
2. 安装VSCode + LaTeX Workshop插件

**配置VSCode（settings.json）：**
```json
{
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.latex.recipes": [
        {
            "name": "xelatex",
            "tools": ["xelatex"]
        }
    ],
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "%DOC%"
            ]
        }
    ]
}
```

**使用：**
```bash
cd templates/latex/mcmthesis
code .  # 打开VSCode

# 编译（Ctrl/Cmd + Alt + B）
xelatex mcmthesis-demo.tex
```

---

## 📖 LaTeX基础（够用版）

### mcmthesis模板基本结构

```latex
\documentclass{mcmthesis}

% 设置队伍信息
\mcmsetup{
    CornNumber = 2312345,        % 控制号
    Problem = C,                 % 题目
    Year = 2026,
    Title = Your Paper Title,
}

\begin{document}

% 1. 摘要（最重要！）
\begin{abstract}
摘要内容...必须回答4个问题：
- 问题是什么？
- 我们做了什么？
- 结论是什么？
- 建议是什么？
\end{abstract}

\begin{keywords}
Keyword1; Keyword2; Keyword3
\end{keywords}

% 2. 目录
\tableofcontents
\newpage

% 3. 正文
\section{Introduction}
...

\section{Problem Analysis}
...

\section{Model Development}
...

\section{Results}
...

\section{Conclusions}
...

% 4. 参考文献
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### 常用命令速查

**插入图片：**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/result.png}
    \caption{Prediction Results}
    \label{fig:result}
\end{figure}

引用：See Figure \ref{fig:result}.
```

**插入表格：**
```latex
\begin{table}[htbp]
    \centering
    \caption{Model Parameters}
    \begin{tabular}{ccc}
        \hline
        Parameter & Value & Description \\
        \hline
        $\alpha$ & 0.05 & Learning rate \\
        \hline
    \end{tabular}
\end{table}
```

**数学公式：**
```latex
% 行内公式
Learning rate $\alpha = 0.01$

% 独立公式
\begin{equation}
    y = \beta_0 + \beta_1 x + \epsilon
    \label{eq:linear}
\end{equation}

% 多行公式
\begin{align}
    x &= a + b \\
    y &= c + d
\end{align}
```

**📋 更多命令**：查看 [`LATEX_CHEATSHEET.md`](./LATEX_CHEATSHEET.md)

---

## 📝 论文结构建议

### 1. Summary（摘要）- 最重要！⭐

**必须回答4个问题：**
1. ✅ **问题是什么？**（Problem）
2. ✅ **我们做了什么？**（Approach/Model）  
3. ✅ **结论是什么？**（Results - 要有数据）
4. ✅ **建议是什么？**（Recommendations）

**长度**：1页以内  
**评分占比**：~40%  
**写作要求**：独立完整，不看正文也能理解

**模板：**
```
[Problem]
We address the problem of [具体问题]. This is important because [重要性].

[Approach]
To solve this, we develop a [模型] model that [做什么]. 
Specifically, we:
- First, [步骤1]
- Then, [步骤2] using [方法]
- Finally, [步骤3]

[Results]
Our results show that [发现1]. Specifically, [具体数据]. 
We also find that [发现2], with [量化结果].

[Recommendations]
Based on our analysis, we recommend [建议1] and [建议2].

Keywords: [3-5个关键词]
```

### 2. Introduction（引言）
- 问题背景
- 文献综述
- 论文组织结构

### 3. Problem Analysis（问题分析）
- 问题分解
- 关键因素识别
- 建模思路流程图

### 4. Assumptions（假设）⭐ 重要
- 列出所有假设
- 说明合理性
- 分析影响

### 5. Model Development（模型建立）
- 符号说明
- 模型推导
- 算法流程

### 6. Model Solution（模型求解）
- 数据处理
- 参数确定
- 求解过程

### 7. Model Analysis（模型分析）⭐ 重要
- 灵敏度分析
- 稳定性分析
- 误差分析

### 8. Results（结果）
- 数据可视化
- 结果解释

### 9. Conclusions（结论）
- 模型优缺点
- 改进方向
- 政策建议

### 10. References（参考文献）

---

## 💡 美赛写作要点

### 关键特点

1. **摘要决定命运**  
   初评主要看摘要，写不好论文再好也难获奖

2. **假设要充分**  
   美赛极度重视假设的合理性和必要性

3. **检验越多越好**  
   灵敏度分析、稳定性分析、误差分析

4. **图表要精美**  
   高分辨率（300 DPI）、配色协调、标注清晰

5. **创新可容错**  
   有创新即使有小错误也可能获奖

### 常见错误 ❌

- 摘要太简单或太差
- 假设不够充分
- 没有模型检验
- 图表质量差（模糊、低分辨率）
- 论文不完整
- 语法错误多

### 正确做法 ✅

- 摘要反复修改，独立完整
- 详细说明所有假设
- 多做灵敏度分析
- 图表300 DPI，专业配色
- 确保每个问题都有结论
- 使用Grammarly检查语法

---

## ⚠️ 常见问题

### LaTeX编译问题

**Q: "mcmthesis.cls not found"**
```
A: mcmthesis.cls必须和.tex文件在同一目录
   或上传到Overleaf项目根目录
```

**Q: 中文显示乱码**
```
A: 使用XeLaTeX编译，不要用PDFLaTeX
```

**Q: 图片无法显示**
```
A: 检查路径是否正确
   推荐：\includegraphics{figures/result.png}
```

**Q: 参考文献格式错误**
```
A: 完整编译流程：
   xelatex main.tex
   bibtex main
   xelatex main.tex
   xelatex main.tex
```

### Overleaf问题

**Q: 编译超时**
```
A: 免费版有限制
   - 压缩图片
   - 升级付费版
   - 或用本地编译
```

**Q: 无法上传大文件**
```
A: 免费版限制<50MB
   - 压缩图片
   - 使用外部图床
```

**Q: 3人协作怎么办？**
```
A: 免费版只能邀请1人
   - 用教育邮箱申请免费升级
   - 或升级付费版（$15/月）
   - 或使用VSCode+Git协作
```

### Word问题

**Q: 公式编号不连续**
```
A: 使用「插入题注」，不要手动编号
```

**Q: 图片位置乱跑**
```
A: 右键图片 → 自动换行 → 嵌入型
```

---

## 🎓 学习路径

### 赛前1周（推荐）

```
Day 1-2: 看B站视频（1-2小时）
         注册Overleaf，试用模板

Day 3-4: 练习写一篇简单文档
         学习插入图表、公式

Day 5-7: 和队友测试协作
         准备常用代码片段
```

### 比赛时（5天）

```
Day 1: 搭建框架，写引言
Day 2-3: 边做边写，及时更新
Day 4: 翻译、排版、美化图表
Day 5: 写摘要、最终检查
```

---

## 📋 提交前检查清单

```
□ 控制号（Control Number）填写正确
□ 题目选择（Problem Chosen）正确
□ 摘要完整（问题-方法-结果-建议）
□ 所有图表清晰（300 DPI）
□ 所有公式有编号并被引用
□ 参考文献格式统一
□ 无明显语法错误（Grammarly检查）
□ 页数 ≤ 25页
□ PDF文件名符合要求
```

---

## 📚 相关资源

### 项目内资源
- **LaTeX命令速查**：[`LATEX_CHEATSHEET.md`](./LATEX_CHEATSHEET.md)
- **论文写作指南**：[`../docs/mcm_guide.md`](../docs/mcm_guide.md)
- **团队协作流程**：[`../docs/team_workflow.md`](../docs/team_workflow.md)
- **算法使用手册**：[`../docs/algorithms_reference.md`](../docs/algorithms_reference.md)

### 在线教程
- **Overleaf文档**：https://www.overleaf.com/learn
- **LaTeX符号查询**：http://detexify.kirelabs.org/classify.html
- **表格生成器**：https://www.tablesgenerator.com/
- **B站搜索**：美赛LaTeX教程

---

**💡 温馨提示**：LaTeX学习曲线陡峭，建议提前1-2周开始学习，不要临时抱佛脚！

**🎓 祝论文写作顺利，美赛取得好成绩！**
