# 图解 KDTree

## 安装 Graphviz

```bash
brew install graphviz
```

## 数据准备

```python
points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
```

相关代码参考 `tests/test_kd_tree_2d` 与 `tests/test_kd_tree_analyze`

```bash
dot -Tpng closest2045.dot -o closest2045.png
dot -Tpng closest2333.dot -o closest2333.png
dot -Tpng closest5595.dot -o closest5595.png
dot -Tpng closest6942.dot -o closest6942.png
```

[graphviz]: https://www.graphviz.org/ "Graphviz"