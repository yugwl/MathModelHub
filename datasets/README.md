# 数据集资源库

存放美赛常用的各类数据集，方便快速调用。

## 📁 数据分类

### economic/ - 经济数据
- GDP数据
- 贸易数据
- 金融市场数据
- 通货膨胀率等

**常用来源**：
- World Bank Open Data
- IMF Data
- OECD Statistics
- 国家统计局

### geographic/ - 地理数据
- 地图数据（GeoJSON、Shapefile）
- 气候数据
- 人口分布数据
- 地形数据

**常用来源**：
- OpenStreetMap
- Natural Earth
- NASA Earth Data
- NOAA Climate Data

### social/ - 社会数据
- 人口统计
- 教育数据
- 健康数据
- 犯罪数据

**常用来源**：
- UN Data
- WHO
- UNESCO
- Kaggle Datasets

## 💡 使用建议

1. 数据文件较大，建议添加到`.gitignore`
2. 记录数据来源和获取时间
3. 预处理后的数据单独存放
4. 为每个数据集编写说明文档

## 🔗 数据获取资源

### 综合数据平台
- [Kaggle](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

### 专业数据源
- **经济金融**：World Bank, IMF, FRED
- **环境气候**：NOAA, NASA, EPA
- **社会健康**：WHO, UN Data, CDC
- **地理空间**：OpenStreetMap, Natural Earth

### Python数据获取库
```python
# 安装常用数据获取库
pip install pandas-datareader yfinance wbdata
```

