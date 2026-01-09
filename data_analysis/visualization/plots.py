"""
美赛常用可视化函数

提供高质量、专业的图表绘制函数
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, List, Tuple


# 设置美赛风格
def set_mcm_style():
    """设置适合美赛的图表风格"""
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['lines.linewidth'] = 2
    sns.set_style("whitegrid")
    sns.set_palette("husl")


def plot_time_series(x, y, title: str = "Time Series", 
                     xlabel: str = "Time", ylabel: str = "Value",
                     figsize: Tuple[int, int] = (10, 6),
                     save_path: Optional[str] = None):
    """
    绘制时间序列图
    
    Args:
        x: 时间轴数据
        y: 数值数据
        title: 图标题
        xlabel: x轴标签
        ylabel: y轴标签
        figsize: 图大小
        save_path: 保存路径（可选）
    """
    set_mcm_style()
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, y, marker='o', markersize=4, linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_comparison(data: dict, title: str = "Comparison",
                   ylabel: str = "Value", figsize: Tuple[int, int] = (10, 6),
                   save_path: Optional[str] = None):
    """
    绘制对比柱状图
    
    Args:
        data: 字典格式 {'Category1': value1, 'Category2': value2, ...}
        title: 图标题
        ylabel: y轴标签
        figsize: 图大小
        save_path: 保存路径（可选）
    """
    set_mcm_style()
    
    fig, ax = plt.subplots(figsize=figsize)
    categories = list(data.keys())
    values = list(data.values())
    
    bars = ax.bar(categories, values, alpha=0.8, edgecolor='black')
    
    # 在柱子上标注数值
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontweight='bold')
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_heatmap(data: np.ndarray, xticklabels: List[str], 
                yticklabels: List[str], title: str = "Heatmap",
                cmap: str = "YlOrRd", figsize: Tuple[int, int] = (10, 8),
                save_path: Optional[str] = None):
    """
    绘制热力图
    
    Args:
        data: 数据矩阵
        xticklabels: x轴标签列表
        yticklabels: y轴标签列表
        title: 图标题
        cmap: 颜色映射
        figsize: 图大小
        save_path: 保存路径（可选）
    """
    set_mcm_style()
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(data, annot=True, fmt='.2f', cmap=cmap,
                xticklabels=xticklabels, yticklabels=yticklabels,
                cbar_kws={'label': 'Value'}, ax=ax)
    ax.set_title(title, fontweight='bold', pad=20)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_sensitivity_analysis(parameter_range: np.ndarray, 
                              results: np.ndarray,
                              parameter_name: str = "Parameter",
                              result_name: str = "Result",
                              title: str = "Sensitivity Analysis",
                              figsize: Tuple[int, int] = (10, 6),
                              save_path: Optional[str] = None):
    """
    绘制灵敏度分析图
    
    美赛必备！展示参数变化对结果的影响
    
    Args:
        parameter_range: 参数取值范围
        results: 对应的结果
        parameter_name: 参数名称
        result_name: 结果名称
        title: 图标题
        figsize: 图大小
        save_path: 保存路径（可选）
    """
    set_mcm_style()
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(parameter_range, results, marker='o', linewidth=2.5, markersize=6)
    ax.set_xlabel(parameter_name)
    ax.set_ylabel(result_name)
    ax.set_title(title, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # 标注最大值和最小值
    max_idx = np.argmax(results)
    min_idx = np.argmin(results)
    ax.plot(parameter_range[max_idx], results[max_idx], 'r*', markersize=15, 
            label=f'Max: {results[max_idx]:.2f}')
    ax.plot(parameter_range[min_idx], results[min_idx], 'b*', markersize=15,
            label=f'Min: {results[min_idx]:.2f}')
    ax.legend()
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_radar(data: dict, title: str = "Radar Chart",
               figsize: Tuple[int, int] = (8, 8),
               save_path: Optional[str] = None):
    """
    绘制雷达图
    
    适合多维度评价展示
    
    Args:
        data: 字典格式 {'Dimension1': value1, 'Dimension2': value2, ...}
        title: 图标题
        figsize: 图大小
        save_path: 保存路径（可选）
    """
    set_mcm_style()
    
    categories = list(data.keys())
    values = list(data.values())
    
    # 闭合雷达图
    values += values[:1]
    
    # 计算角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(projection='polar'))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(title, fontweight='bold', pad=20)
    ax.grid(True)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    # 示例使用
    print("运行可视化示例...")
    
    # 时间序列示例
    x = np.arange(0, 10, 0.5)
    y = np.sin(x) + np.random.normal(0, 0.1, len(x))
    plot_time_series(x, y, title="Example Time Series", 
                     xlabel="Time (s)", ylabel="Signal")
    
    # 对比图示例
    data = {'Method A': 0.85, 'Method B': 0.92, 'Method C': 0.78, 'Method D': 0.88}
    plot_comparison(data, title="Model Performance Comparison", 
                   ylabel="Accuracy")
    
    # 灵敏度分析示例
    params = np.linspace(0, 1, 20)
    results = np.sin(params * np.pi) * 100
    plot_sensitivity_analysis(params, results, 
                             parameter_name="Parameter α",
                             result_name="Model Output",
                             title="Sensitivity Analysis of Parameter α")

