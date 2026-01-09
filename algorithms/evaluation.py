"""
评价决策类模型

包含美赛高频使用的评价模型：
- AHP（层次分析法）
- 熵权法（EWM）
- TOPSIS法
- 模糊综合评价
"""

import numpy as np
from typing import List, Tuple


class AHP:
    """
    层次分析法（Analytic Hierarchy Process）
    
    美赛出现频率最高的评价方法之一
    
    使用示例：
        ahp = AHP()
        matrix = np.array([[1, 3, 5], [1/3, 1, 2], [1/5, 1/2, 1]])
        weights = ahp.calculate_weights(matrix)
        cr = ahp.consistency_ratio(matrix)
    """
    
    # Saaty 1-9标度法的随机一致性指标
    RI = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 
          6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    
    def calculate_weights(self, matrix: np.ndarray) -> np.ndarray:
        """
        计算权重向量
        
        Args:
            matrix: 判断矩阵（n×n）
            
        Returns:
            权重向量
        """
        n = len(matrix)
        
        # 方法1: 几何平均法
        # 计算每行的几何平均
        geom_mean = np.prod(matrix, axis=1) ** (1/n)
        weights = geom_mean / np.sum(geom_mean)
        
        return weights
    
    def consistency_ratio(self, matrix: np.ndarray) -> float:
        """
        计算一致性比率 CR
        
        CR < 0.1 认为判断矩阵具有满意的一致性
        
        Args:
            matrix: 判断矩阵
            
        Returns:
            一致性比率 CR
        """
        n = len(matrix)
        weights = self.calculate_weights(matrix)
        
        # 计算最大特征值
        lambda_max = np.sum(np.dot(matrix, weights) / weights) / n
        
        # 计算一致性指标 CI
        CI = (lambda_max - n) / (n - 1)
        
        # 计算一致性比率 CR
        RI_value = self.RI.get(n, 0)
        CR = CI / RI_value if RI_value > 0 else 0
        
        return CR


class EntropyWeight:
    """
    熵权法（Entropy Weight Method）
    
    客观赋权法，美赛常用于综合评价
    """
    
    def calculate_weights(self, data: np.ndarray) -> np.ndarray:
        """
        计算各指标的熵权
        
        Args:
            data: 数据矩阵（m×n，m个样本，n个指标）
            
        Returns:
            权重向量（n维）
        """
        # 数据标准化
        data_norm = self._normalize(data)
        
        # 计算信息熵
        m, n = data_norm.shape
        p = data_norm / np.sum(data_norm, axis=0)
        
        # 避免log(0)
        p = np.where(p == 0, 1e-10, p)
        
        e = -np.sum(p * np.log(p), axis=0) / np.log(m)
        
        # 计算权重
        d = 1 - e
        weights = d / np.sum(d)
        
        return weights
    
    def _normalize(self, data: np.ndarray) -> np.ndarray:
        """数据归一化到[0,1]"""
        min_val = np.min(data, axis=0)
        max_val = np.max(data, axis=0)
        return (data - min_val) / (max_val - min_val + 1e-10)


class TOPSIS:
    """
    优劣解距离法（Technique for Order Preference by Similarity to Ideal Solution）
    
    美赛常用的多目标决策方法
    """
    
    def evaluate(self, data: np.ndarray, weights: np.ndarray, 
                 is_benefit: List[bool]) -> Tuple[np.ndarray, np.ndarray]:
        """
        TOPSIS评价
        
        Args:
            data: 决策矩阵（m×n）
            weights: 权重向量（n维）
            is_benefit: 指标类型列表，True表示效益型，False表示成本型
            
        Returns:
            (综合得分, 排名)
        """
        # 数据标准化
        data_norm = self._normalize(data, is_benefit)
        
        # 加权标准化矩阵
        weighted = data_norm * weights
        
        # 确定正理想解和负理想解
        ideal_best = np.max(weighted, axis=0)
        ideal_worst = np.min(weighted, axis=0)
        
        # 计算距离
        dist_best = np.sqrt(np.sum((weighted - ideal_best) ** 2, axis=1))
        dist_worst = np.sqrt(np.sum((weighted - ideal_worst) ** 2, axis=1))
        
        # 计算综合得分
        scores = dist_worst / (dist_best + dist_worst)
        
        # 排名
        ranks = np.argsort(-scores) + 1
        
        return scores, ranks
    
    def _normalize(self, data: np.ndarray, is_benefit: List[bool]) -> np.ndarray:
        """标准化处理"""
        data_norm = np.zeros_like(data, dtype=float)
        
        for j in range(data.shape[1]):
            col = data[:, j]
            if is_benefit[j]:
                # 效益型指标：越大越好
                data_norm[:, j] = (col - np.min(col)) / (np.max(col) - np.min(col) + 1e-10)
            else:
                # 成本型指标：越小越好
                data_norm[:, j] = (np.max(col) - col) / (np.max(col) - np.min(col) + 1e-10)
        
        return data_norm


def combined_weight(subjective_weights: np.ndarray, 
                   objective_weights: np.ndarray,
                   alpha: float = 0.5) -> np.ndarray:
    """
    组合权重法（主客观结合）
    
    美赛常用：AHP（主观）+ 熵权法（客观）
    
    Args:
        subjective_weights: 主观权重（如AHP得到的权重）
        objective_weights: 客观权重（如熵权法得到的权重）
        alpha: 主观权重系数（0-1之间），默认0.5表示等权重
        
    Returns:
        组合权重
    """
    combined = alpha * subjective_weights + (1 - alpha) * objective_weights
    combined = combined / np.sum(combined)  # 归一化
    return combined


if __name__ == "__main__":
    # 示例：AHP计算权重
    print("=== AHP示例 ===")
    ahp = AHP()
    # 判断矩阵示例
    matrix = np.array([
        [1,   3,   5],
        [1/3, 1,   2],
        [1/5, 1/2, 1]
    ])
    weights = ahp.calculate_weights(matrix)
    cr = ahp.consistency_ratio(matrix)
    print(f"权重: {weights}")
    print(f"一致性比率 CR: {cr:.4f}")
    print(f"是否通过一致性检验: {'是' if cr < 0.1 else '否'}")
    
    print("\n=== TOPSIS示例 ===")
    # 决策矩阵示例
    data = np.array([
        [80, 90, 70, 85],
        [85, 85, 80, 80],
        [90, 80, 85, 75],
        [75, 95, 75, 90]
    ])
    weights = np.array([0.3, 0.3, 0.2, 0.2])
    is_benefit = [True, True, True, True]  # 都是效益型指标
    
    topsis = TOPSIS()
    scores, ranks = topsis.evaluate(data, weights, is_benefit)
    print(f"综合得分: {scores}")
    print(f"排名: {ranks}")

