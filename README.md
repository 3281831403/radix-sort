# 基数排序：按位稳定与最大位

非负整数排序在大数组上退化、负数顺序反：取位没有用绝对值，按位排序不稳定，最大位循环少一轮，空数组崩，最大值算错，结果校验缺失，批量排序只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
sort/__init__.py
sort/radix.py
tests/test_radix.py
```

## 当前状态

`sort/radix.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_radix.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 取位用绝对值
2. 按位稳定排序
3. 最大位循环
4. 空数组兜底
5. 最大值
6. 结果校验

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `sort/radix.py`
后 15 条用例应全部通过。
