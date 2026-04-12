# triangle-sides-height

小学校算数の三角形の面積問題を Python で再現するリポジトリです。

元ネタ: https://www.threads.com/@vul829_1984/post/DW8tKy7Cdw0

## 問題

底辺5cm・右辺4cm・高さ3cmの三角形の面積を求めます。

```
底辺 × 高さ ÷ 2 = 5 × 3 ÷ 2 = 7.5 cm²
```

## ファイル

| ファイル | 内容 |
|---|---|
| `triangle-sides-height.py` | 三角形を描画して面積を計算するスクリプト |
| `triangle-3-4-5-height.jpg` | 元の問題画像 |
| `triangle-plot.png` | スクリプトの出力画像 |

## 実行方法

```bash
python triangle-sides-height.py
```

## テスト

```bash
python -m pytest test_triangle.py -v
```
