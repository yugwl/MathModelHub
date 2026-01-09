"""
TOPSIS（优劣解距离法）示例

TOPSIS是美赛常用的多目标决策方法。
"""

import sys
sys.path.append('../..')

import numpy as np
import matplotlib.pyplot as plt
from algorithms.evaluation import TOPSIS

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    print("=" * 60)
    print("TOPSIS（优劣解距离法）示例")
    print("=" * 60)
    
    # 示例问题：评价4个方案
    print("\n问题：评价4个投资方案")
    print("评价指标：收益率、风险度、流动性、成长性")
    
    # 决策矩阵（4个方案，4个指标）
    data = np.array([
        [0.08, 0.15, 0.85, 0.90],  # 方案A
        [0.12, 0.25, 0.75, 0.85],  # 方案B
        [0.15, 0.35, 0.65, 0.80],  # 方案C
        [0.10, 0.20, 0.80, 0.88]   # 方案D
    ])
    
    print("\n决策矩阵：")
    print("       收益率  风险度  流动性  成长性")
    schemes = ['方案A', '方案B', '方案C', '方案D']
    for i, scheme in enumerate(schemes):
        print(f"{scheme}: {data[i]}")
    
    # 权重（可以用AHP或熵权法得到）
    weights = np.array([0.35, 0.25, 0.20, 0.20])
    
    print("\n指标权重：")
    indicators = ['收益率', '风险度', '流动性', '成长性']
    for indicator, weight in zip(indicators, weights):
        print(f"  {indicator}: {weight:.2f}")
    
    # 指标类型（True=效益型，False=成本型）
    # 收益率、流动性、成长性：越大越好（效益型）
    # 风险度：越小越好（成本型）
    is_benefit = [True, False, True, True]
    
    # TOPSIS评价
    topsis = TOPSIS()
    scores, ranks = topsis.evaluate(data, weights, is_benefit)
    
    print("\n评价结果：")
    for i, scheme in enumerate(schemes):
        print(f"  {scheme}: 得分={scores[i]:.4f}, 排名={ranks[i]}")
    
    # 可视化
    visualize_results(schemes, scores, ranks)
    
    print("\n" + "=" * 60)
    print("示例完成！")
    print("=" * 60)


def visualize_results(schemes, scores, ranks):
    """可视化评价结果"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左图：得分柱状图
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    bars = ax1.bar(schemes, scores, alpha=0.8, edgecolor='black', color=colors)
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax1.set_ylabel('综合得分', fontsize=12)
    ax1.set_title('TOPSIS综合得分', fontsize=14, fontweight='bold')
    ax1.grid(True, axis='y', alpha=0.3)
    ax1.set_ylim(0, max(scores) * 1.2)
    
    # 右图：排名
    rank_colors = [colors[np.where(ranks == i+1)[0][0]] for i in range(len(ranks))]
    bars2 = ax2.barh(range(1, len(schemes)+1), 
                     [1]*len(schemes), 
                     alpha=0.8, 
                     edgecolor='black',
                     color=rank_colors)
    
    # 标注方案名称
    for i, (rank, scheme) in enumerate(zip(range(1, len(schemes)+1), 
                                           [schemes[np.where(ranks == j+1)[0][0]] 
                                            for j in range(len(schemes))])):
        ax2.text(0.5, rank, scheme, ha='center', va='center', 
                fontsize=12, fontweight='bold', color='white')
    
    ax2.set_xlabel('', fontsize=12)
    ax2.set_ylabel('排名', fontsize=12)
    ax2.set_title('方案排名', fontsize=14, fontweight='bold')
    ax2.set_yticks(range(1, len(schemes)+1))
    ax2.set_xticks([])
    ax2.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('topsis_results.png', dpi=300, bbox_inches='tight')
    print("\n图表已保存为 topsis_results.png")
    plt.show()


if __name__ == "__main__":
    main()

