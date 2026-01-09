"""
AHP（层次分析法）示例

层次分析法是美赛中出现频率最高的评价方法之一。
"""

import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt
from algorithms.evaluation import AHP

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    print("=" * 60)
    print("AHP（层次分析法）示例")
    print("=" * 60)
    
    # 创建AHP对象
    ahp = AHP()
    
    # 示例问题：评价城市宜居性
    # 考虑因素：环境质量、经济发展、教育资源
    print("\n问题：评价三个城市的宜居性")
    print("考虑因素：1.环境质量 2.经济发展 3.教育资源")
    
    # 判断矩阵
    # 环境 vs 经济 = 3（环境明显重要）
    # 环境 vs 教育 = 5（环境更加重要）
    # 经济 vs 教育 = 2（经济稍微重要）
    matrix = np.array([
        [1,   3,   5],    # 环境
        [1/3, 1,   2],    # 经济
        [1/5, 1/2, 1]     # 教育
    ])
    
    print("\n判断矩阵：")
    print(matrix)
    
    # 计算权重
    weights = ahp.calculate_weights(matrix)
    
    print("\n各因素权重：")
    factors = ['环境质量', '经济发展', '教育资源']
    for factor, weight in zip(factors, weights):
        print(f"  {factor}: {weight:.4f} ({weight*100:.2f}%)")
    
    # 一致性检验
    cr = ahp.consistency_ratio(matrix)
    print(f"\n一致性比率 CR: {cr:.4f}")
    
    if cr < 0.1:
        print("✓ 通过一致性检验（CR < 0.1）")
    else:
        print("✗ 未通过一致性检验，需要调整判断矩阵")
    
    # 可视化
    visualize_weights(factors, weights)
    
    print("\n" + "=" * 60)
    print("示例完成！")
    print("=" * 60)


def visualize_weights(factors, weights):
    """可视化权重分布"""
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(factors, weights, alpha=0.8, edgecolor='black', 
                   color=['#3498db', '#e74c3c', '#2ecc71'])
    
    # 标注数值
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_ylabel('权重', fontsize=12)
    ax.set_title('城市宜居性评价指标权重分布', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(weights) * 1.2)
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('ahp_weights.png', dpi=300, bbox_inches='tight')
    print("\n图表已保存为 ahp_weights.png")
    plt.show()


if __name__ == "__main__":
    main()

