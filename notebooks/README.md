# Jupyter Notebooks

用于算法学习、实验探索和快速原型开发。

## 📁 目录说明

### examples/ - 算法示例
存放各类算法的使用示例，快速上手。

**建议内容**：
- `ahp_example.ipynb` - 层次分析法示例
- `arima_forecast.ipynb` - 时间序列预测
- `genetic_algorithm.ipynb` - 遗传算法示例
- `kmeans_clustering.ipynb` - 聚类分析
- 等等

### tutorials/ - 学习教程
系统性的教程笔记，深入理解算法原理。

**建议内容**：
- 美赛高频算法详解
- 数据可视化技巧
- Python科学计算基础
- 机器学习速成

### experiments/ - 实验探索
比赛前的算法测试和参数调优。

## 🚀 快速开始

```bash
# 启动Jupyter Notebook
jupyter notebook

# 或使用JupyterLab（推荐）
jupyter lab
```

## 💡 使用建议

1. **比赛前准备**：
   - 熟悉常用算法的调用方式
   - 准备好可视化代码模板
   - 测试数据处理流程

2. **比赛中使用**：
   - 快速验证算法可行性
   - 调试参数设置
   - 生成初步结果

3. **比赛后总结**：
   - 整理经验教训
   - 保存可复用的代码片段

## 📚 推荐资源

### Jupyter技巧
- 快捷键：`Shift+Enter` 运行单元格
- 魔法命令：`%matplotlib inline` 内嵌图表
- 导出PDF：`File > Download as > PDF`

### 常用库
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, optimize
from sklearn import *
```

### 可视化样式
```python
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 设置美赛风格
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 300
```

