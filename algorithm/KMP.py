def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    print(table)
    while cur <= m - n:  # 长度不够就终止
        # print("新一轮匹配，开始位置", cur)
        for i in range(n):  # 一次匹配长度
            if s[i + cur] != p[i]:
                # print(s[i+cur], p[i], '不匹配。查表位置：', i, i - table[i-1])
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return cur
    return -1


# 部分匹配表
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    table = [0]
    for i in range(1, len(p)):  # 从1开始进行前后缀比较
        prefix.add(p[:i])  # 前缀每次累加就行
        postfix = set()
        for j in range(1, i + 1):  # i+1 因为i需要包括
            postfix.add(p[j:i + 1])
            # print(prefix, postfix)
        # print(prefix&postfix, len(prefix&postfix))
        # table.append(len((sorted((prefix&postfix),key = len)or {''}).pop()))
        if prefix & postfix:
            table.append(max(map(len, prefix & postfix)))
        else:
            table.append(0)
    return table

kmp_match("abcdafhg","daf")