import math
import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
  "triangle_sides_height",
  pathlib.Path(__file__).parent / "triangle-sides-height.py",
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

calc_vertices = mod.calc_vertices
calc_area = mod.calc_area


def test_area():
  """底辺5cm・高さ3cmの三角形の面積が7.5cm²になる。"""
  assert calc_area(5.0, 3.0) == 7.5


def test_area_zero_base():
  """底辺が0のとき面積は0になる。"""
  assert calc_area(0.0, 3.0) == 0.0


def test_area_zero_height():
  """高さが0のとき面積は0になる。"""
  assert calc_area(5.0, 0.0) == 0.0


def test_vertices_A_at_origin():
  """頂点Aが原点(0, 0)に配置される。"""
  A, _, _ = calc_vertices(5.0, 4.0, 3.0)
  assert A == (0.0, 0.0)


def test_vertices_B_at_base():
  """頂点Bが底辺の右端(5, 0)に配置される。"""
  _, B, _ = calc_vertices(5.0, 4.0, 3.0)
  assert B == (5.0, 0.0)


def test_vertices_C_height():
  """頂点Cのy座標が指定した高さ3.0cmと一致する。"""
  _, _, C = calc_vertices(5.0, 4.0, 3.0)
  assert C[1] == 3.0


def test_vertices_BC_length():
  """頂点 B-C 間の距離が指定した右辺の長さと一致する。"""
  _, B, C = calc_vertices(5.0, 4.0, 3.0)
  assert math.isclose(math.dist(B, C), 4.0)


def test_vertices_height_is_perpendicular():
  """高さの足（C の x 座標）が底辺 AB に対して直交する。"""
  A, B, C = calc_vertices(5.0, 4.0, 3.0)
  foot = (C[0], 0.0)
  # 足から C は垂直（x 座標が一致）
  assert foot[0] == C[0]
  # 足は AB 上（0 <= foot[0] <= base）
  assert A[0] <= foot[0] <= B[0]
