from collections import defaultdict
import bisect

import numpy as np


#  题目一
def min_num_of_subseq(src: str, target: str) -> int:
    pos = defaultdict(list)  # 记录每个字符在src中的位置
    for i, char in enumerate(src):
        pos[char].append(i)

    cnt, i = 0, 0
    while i < len(target):
        if target[i] not in pos:
            return -1  # src中不包含当前字符

        cnt += 1
        cur_src_index = -1  # 从头开始匹配
        # cur_str = ""  # for test
        while i < len(target) and target[i] in pos:
            idx_list = pos[target[i]]

            # The return value j is such that all e in
            # a[:j] have e <= x, and all e in a[j:] have e > x.
            # 注：idx_list是单调递增的，所以可以用二分查找
            j = bisect.bisect_right(idx_list, cur_src_index)

            if j == len(idx_list):
                break  # 在索引列表中没有找到当前字符
            # cur_str += target[i]
            cur_src_index = idx_list[j]
            i += 1
        # print(f"cur_str={cur_str}")

    return cnt


#  题目二
def check_bracket(s):
    stack = []
    res = [' '] * len(s)  # 占位

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # 压栈
        elif char == ')':
            if len(stack) == 0:
                res[i] = '?'  # 该')'没有匹配的'('
            else:
                stack.pop()  # 出栈

    # 处理栈中未匹配的'('
    for idx in stack:
        res[idx] = 'x'

    print(s)
    print(''.join(res))


# 题目三（注：暴搜，未满足时间复杂度要求...）
def find_max_weighted_subseq(a):
    max_value = float('-inf')
    n = len(a)

    for i in range(1, 1 << n):
        subset = [a[j] for j in range(n) if (i & (1 << j))]
        if subset:
            sub_mean = np.mean(subset)
            sub_median = np.median(subset)
            sub_val = sub_mean - sub_median
            if sub_val > max_value:
                max_value = sub_val

    return max_value


if __name__ == '__main__':
    print("===============题目一===============")
    print(min_num_of_subseq("abc", "abcbc"))
    print(min_num_of_subseq("abc", "acdbc"))
    print(min_num_of_subseq("xyz", "xzyxz"))
    # print(min_num_of_subseq("BUPT工位有我在", "我在BUPT有工位"))
    print("===============题目一===============")

    print("\n")

    print("===============题目二===============")
    check_bracket("bge))))))))))")
    check_bracket("((IIII))))))")
    check_bracket("))))UUUU((()")
    print("===============题目二===============")

    print("\n")

    print("===============题目三===============")
    print(f"最大权值: {find_max_weighted_subseq([1, 3, 5, 9]):.3f}")
    print("===============题目三===============")
