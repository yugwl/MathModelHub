# 🚀 快速开始指南

## 环境配置

### 1. 安装依赖

```bash
cd MathModelHub
pip install -r requirements.txt
```

或者安装为Python包：

```bash
pip install -e .
```

### 2. 验证安装

```bash
python -c "import numpy, pandas, matplotlib; print('环境配置成功！')"
```

## 📚 快速使用

### 使用论文模板

**快速开始：查看 [`templates/README.md`](./templates/README.md)**

#### LaTeX + Overleaf（推荐）⭐

```
1. 访问 https://www.overleaf.com 注册
2. 创建新项目
3. 上传 templates/latex/mcmthesis/mcmthesis.cls
4. 参考 mcmthesis-demo.tex 开始写作
```

#### Word模板

```
打开 templates/word/MCM_Template.docx
填写摘要页，开始写作
```

**详细教程**：`templates/README.md`（含快速开始、VSCode配置、常见问题等）  
**命令速查**：`templates/LATEX_CHEATSHEET.md`

### 使用评价模型

```python
# 导入AHP模型
from algorithms.evaluation import AHP
import numpy as np

# 创建判断矩阵
ahp = AHP()
matrix = np.array([
    [1,   3,   5],
    [1/3, 1,   2],
    [1/5, 1/2, 1]
])

# 计算权重
weights = ahp.calculate_weights(matrix)
cr = ahp.consistency_ratio(matrix)

print(f"权重: {weights}")
print(f"一致性检验CR: {cr:.4f} {'✓通过' if cr < 0.1 else '✗未通过'}")
```

### 使用可视化工具

```python
from data_analysis.visualization.plots import *
import numpy as np

# 设置美赛风格
set_mcm_style()

# 绘制时间序列
x = np.arange(0, 10, 0.5)
y = np.sin(x)
plot_time_series(x, y, title="示例图表", xlabel="时间", ylabel="数值")

# 绘制灵敏度分析（美赛必备！）
params = np.linspace(0, 1, 20)
results = params**2 * 100
plot_sensitivity_analysis(params, results, 
                         parameter_name="参数α",
                         result_name="模型输出")
```

## 🎯 参加美赛准备

### 赛前准备清单

- [ ] 熟悉常用算法（见 `docs/algorithms_reference.md`）
- [ ] 准备代码模板（在 `notebooks/examples/` 中创建）
- [ ] 测试LaTeX环境（准备好论文模板）
- [ ] 阅读O奖论文（`past_problems/` 目录）
- [ ] 准备翻译工具（DeepL、ChatGPT等）

### 比赛时工作流程

1. **Day 1上午**：选题
   - 在 `competitions/2026/problem_analysis/` 中记录分析
   
2. **Day 1下午-Day 3**：建模求解
   - 代码存放在 `competitions/2026/code/`
   - 数据存放在 `competitions/2026/data/`
   
3. **Day 2-Day 4**：论文撰写
   - 使用 `templates/` 中的模板
   - 论文存放在 `competitions/2026/paper/`
   
4. **Day 5上午**：最终检查提交

## 📖 学习路径

### 新手入门（赛前1个月）

1. **第1周**：学习Python基础和NumPy、Pandas
2. **第2周**：掌握评价模型（AHP、熵权法、TOPSIS）
3. **第3周**：学习预测模型（ARIMA、回归分析）
4. **第4周**：练习论文写作，阅读O奖论文

### 快速提升（赛前1周）

1. 完成 `notebooks/examples/` 中的所有示例
2. 阅读 `docs/mcm_guide.md` 完整指南
3. 熟悉 `docs/algorithms_reference.md` 算法手册
4. 准备个人代码模板库

## 💡 常用资源快速链接

| 资源 | 位置 | 说明 |
|------|------|------|
| 完整指南 | `docs/mcm_guide.md` | 评审机制、选题策略等 |
| **团队协作** | **`docs/team_workflow.md`** | **详细分工、工具配置、协作流程** ⭐ |
| 算法手册 | `docs/algorithms_reference.md` | 算法使用参考 |
| 历年真题 | `past_problems/README.md` | 题目分析和统计 |
| 论文模板 | `templates/` | LaTeX和Word模板 |
| 代码示例 | `notebooks/examples/` | Jupyter示例 |

## 🔧 常见问题

### Q: 如何测试代码？

```bash
# 进入项目目录
cd MathModelHub

# 运行示例
python algorithms/evaluation.py
python data_analysis/visualization/plots.py
```

### Q: 如何导入自己的算法？

在对应的目录下创建`.py`文件，然后导入：

```python
from algorithms.optimization.my_algorithm import MyAlgorithm
```

### Q: 如何准备数据集？

将数据放入 `datasets/` 对应的子目录，并在README中记录来源。

## 🎓 学习建议

1. **不要贪多**：重点掌握5-6个高频算法
2. **多做笔记**：在 `notebooks/` 中记录学习心得
3. **看O奖论文**：学习摘要写法和图表设计
4. **练习英文**：提前准备常用表达和模板句
5. **团队协作**：提前分工，明确各自任务

## 📞 获取帮助

- 查看文档：`docs/` 目录
- 运行示例：`notebooks/examples/` 目录
- 参考历年题：`past_problems/` 目录

---

**祝比赛顺利，取得好成绩！🏆**

