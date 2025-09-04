n, m = map(int, input().split(' '))

n_line = n-1
m_line = m-1 

count = n_line + (m_line * n)

print(count)