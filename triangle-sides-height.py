import math
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Hiragino Sans'

# 三角形の寸法
# 元ネタ: https://www.threads.com/@vul829_1984/post/DW8tKy7Cdw0
base = 5.0    # 底辺 AB (cm)
BC = 4.0      # 右辺 BC (cm)
height = 3.0  # 高さ (cm)

# 頂点の座標
# BC=4, 高さ=3 → Cx = 5 - √(4²-3²) = 5 - √7
A = (0.0, 0.0)
B = (base, 0.0)
C = (base - math.sqrt(BC**2 - height**2), height)

# 面積
area = base * height / 2

# 描画
fig, ax = plt.subplots(figsize=(6, 5))

# 三角形
xs = [A[0], B[0], C[0], A[0]]
ys = [A[1], B[1], C[1], A[1]]
ax.plot(xs, ys, 'k-', linewidth=2)

# 高さ（破線）
ax.plot([C[0], C[0]], [C[1], 0], 'k--', linewidth=1)

# 直角マーク
sq = 0.12
ax.plot([C[0], C[0] + sq], [0, 0], 'k-', linewidth=1)
ax.plot([C[0] + sq, C[0] + sq], [0, sq], 'k-', linewidth=1)

# 頂点ラベル
ax.text(A[0] - 0.2, A[1] - 0.25, "A", fontsize=11, ha='center')
ax.text(B[0] + 0.2, B[1] - 0.25, "B", fontsize=11, ha='center')
ax.text(C[0], C[1] + 0.25, "C", fontsize=11, ha='center')

# 辺ラベル
ax.text(base / 2, -0.25, "5cm", fontsize=11, ha='center')
ax.text((B[0] + C[0]) / 2 + 0.2, (B[1] + C[1]) / 2, "4cm", fontsize=11, ha='left')
ax.text(C[0] - 0.15, height / 2, "3cm", fontsize=11, ha='right', va='center')

ax.set_title(
  f"三角形の面積 = 底辺 × 高さ ÷ 2 = {base} × {height} ÷ 2 = {area} cm²",
  fontsize=11
)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-0.6, 5.6)
ax.set_ylim(-0.55, 3.6)
ax.grid(True, alpha=0.3)
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")

plt.tight_layout()
plt.savefig("triangle-plot.png", dpi=150)
plt.show()
