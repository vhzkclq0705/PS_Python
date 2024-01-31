# Silver 3 - 에너지 드링크

import sys
input = sys.stdin.readline

n = int(input())
energy = list(map(int, input().split()))
m_e = max(energy)

print(m_e + (sum(energy) - m_e) / 2)