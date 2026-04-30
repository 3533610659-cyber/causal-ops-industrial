"""
Causal-Ops 系统演示脚本
"""
import numpy as np
from causal_ops.agents import *
from causal_ops.utils.data_utils import load_baseline_data, generate_test_data

if __name__ == "__main__":
    print("="*50)
    print("🚀 Causal-Ops 工业因果诊断系统启动")
    print("="*50)

    # 1. 初始化基线
    baseline = load_baseline_data()

    # 2. 感知Agent
   感知 = MultimodalPerceptionAgent(baseline)
    dcs, vib, thermal = generate_test_data()
    异常节点 = 感知.anomaly_detection(dcs)
    print(f"🔍 检测到异常节点：{异常节点[:5]}")

    # 3. 因果Agent
    因果 = CausalDiscoveryAgent(mechanism_model=None)
    故障链, 置信度 = 因果.counterfactual_inference(None)
    print(f"🧠 根因假设：{故障链[0]} | 置信度：{置信度}")

    # 4. 孪生验证Agent
    孪生 = DigitalTwinAgent()
    仿真曲线 = 孪生.inject_fault_simulation(故障链)
    相似度 = 孪生.dtw_similarity(dcs, 仿真曲线)
    print(f"🔬 仿真验证置信度：{相似度}")

    # 5. 预测Agent
    预测 = TimeSeriesPredictionAgent()
    rti = 预测.calculate_rti(dcs, 1.5)
    print(f"⏱️ 剩余干预窗口：{rti} 分钟")

    # 6. 决策Agent
    决策 = DecisionArbitrationAgent()
    建议 = 决策.generate_recommendation("冷却水回路结垢", rti)
    print(f"✅ {建议}")

    print("="*50)
    print("🎯 系统运行完成！")