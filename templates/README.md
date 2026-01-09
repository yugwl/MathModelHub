# 美赛论文模板

## LaTeX模板

### MCM/ICM官方模板
- 符合美赛格式要求
- 包含摘要页、正文、参考文献等
- 预设好字体、页边距、页眉页脚

### 使用方法
```bash
cd latex/mcm_template
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

或使用在线LaTeX编辑器：
- [Overleaf](https://www.overleaf.com/)
- [TeXPage](https://www.texpage.com/)

## Word模板

适合不熟悉LaTeX的队伍使用。

### 包含内容
- 摘要页（Summary Sheet）
- 正文模板
- 图表样式
- 参考文献格式

## 📝 论文结构建议

### 1. Summary（摘要）- 最重要！
- 问题重述
- 模型方法简述
- 主要结果
- 结论与建议

**长度**：1页以内
**评分占比**：~40%

### 2. Introduction（引言）
- 问题背景
- 文献综述
- 论文组织结构

### 3. Problem Analysis（问题分析）
- 问题分解
- 关键因素识别
- 建模思路流程图

### 4. Assumptions（假设）
- 合理假设及理由
- 假设的影响分析

### 5. Model Development（模型建立）
- 符号说明
- 模型推导
- 算法流程

### 6. Model Solution（模型求解）
- 数据处理
- 参数确定
- 求解过程

### 7. Model Analysis（模型分析）
- 灵敏度分析
- 稳定性分析
- 误差分析

### 8. Model Testing & Validation（检验）
- 模型验证
- 结果对比

### 9. Results（结果）
- 数据可视化
- 结果解释

### 10. Conclusions（结论）
- 模型优缺点
- 改进方向
- 政策建议

### 11. References（参考文献）

## 💡 写作技巧

1. **摘要决定初评**：摘要必须独立完整，不看正文也能理解
2. **图表精美**：美赛重视视觉呈现，多用高质量图表
3. **逻辑清晰**：使用流程图、框架图展示思路
4. **假设充分**：美赛特别重视假设的合理性和必要性分析
5. **模型检验**：多做灵敏度分析、稳定性分析
6. **英文表达**：语法正确、表达专业、避免中式英语

## 📚 参考资源

- O奖论文：`../past_problems/`目录
- 写作指南：`../docs/`目录

