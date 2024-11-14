'''
Author: Wyatt Payne
Title: main.py
Lab: Lab10
Purpose: Output a Euler Circuit from a given nxn binary matrix
'''

def main():
    m = input("Enter a matrix ([1,0,1][0,1,0][1,1,1]): ")
    m = m.split('[')
    m.pop(0)
    for i in range(len(m)):
        m[i] = m[i].split(",")
        m[i][len(m) - 1] = m[i][len(m) - 1][0]
        for j in range(len(m)):
            m[i][j] = int(m[i][j])
    for i in range(len(m)):
        m[i][i] = 0
    vertex = list('abcdefghijklmnopqrstuvwxyz')
    euler(m,vertex)

def euler(m,v):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 1:
                circuit(m,v,len(m),j,i)

def circuit(m,v,i,j,origin):
    if i == len(m):
        t = trailM(m,origin,j)
    else:
        t = trailM(m,i,j)
    val = 0
    for l in range(len(m)):
        if t[j][l] == 1:
            val = 1
    if val == 0:
        if origin == i:
            return True
        else:
            return False
    else:
        for k in range(len(m)):
            if t[j][k] == 1:
                if circuit(m,v,j,k,origin):
                    print(v[j])
                    break
        
def trailM(m,i,j):
    trail = []
    for x in range(len(m)):
        trail.append([])
        for y in range(len(m)):
            trail[x].append(m[x][y])
    trail[i][j] = 0
    trail[j][i] = 0
    return trail

main()
