def selection_sort_vooraan(rij):
    n = len(rij)
    for i in range(0,n-1,1):
        pos = i
        min = rij[i]
        for j in range(i+1,n,1):
            if a[j] < min:
                min = a[j]
                pos = j
        # minimum vooraan zetten
        a[pos] = a[i]
        a[i] = min
        print(a)

if __name__ == "__main__":
    rij = [int(_) for _ in input().split()]
    selection_sort_vooraan(rij)

