# Muhendislik Ekonomisi Formülleri
# Doğrudan çalıştırabilirsiniz ya da başka bir Python dosyasına dahil edebilirsiniz.
# Kullanım örneği:
# -40000 * pf(0.12, 3) + 20000 * pa(0.12, 3)


def pf(i, n):
    """(P/F, i, n): Bugünkü Değer Faktörü"""
    return 1 / ((1 + i) ** n)

def fp(i, n):
    """(F/P, i, n): Bileşik Miktar Faktörü"""
    return (1 + i) ** n

def pa(i, n):
    """(P/A, i, n): Uniform Seri Bugünkü Değer Faktörü"""
    return ((1 + i) ** n - 1) / (i * (1 + i) ** n)

def ap(i, n):
    """(A/P, i, n): Sermaye Kurtarma Faktörü"""
    return (i * (1 + i) ** n) / ((1 + i) ** n - 1)

def fa(i, n):
    """(F/A, i, n): Uniform Seri Bileşik Miktar Faktörü"""
    return ((1 + i) ** n - 1) / i

def af(i, n):
    """(A/F, i, n): Amortisman Faktörü"""
    return i / ((1 + i) ** n - 1)

def pg(i, n):
    """(P/G, i, n): Aritmetik Gradyan Bugünkü Değer Faktörü"""
    return (((1 + i) ** n - i * n - 1) / (i ** 2 * (1 + i) ** n))

def ag(i, n):
    """(A/G, i, n): Aritmetik Gradyan Uniform Seri Faktörü"""
    return (1 / i) - (n / ((1 + i) ** n - 1))

def pga(i, g, n, A1):
    """
    Geometrik Gradyan Bugünkü Değer Faktörü
    g: gradyan oranı
    i: faiz oranı
    n: dönem
    A!: ilk dönem nakit akışı
    """
    if g != i:
        return A1 * (1 - ((1 + g) / (1 + i)) ** n) / (i - g)
    else:
        return A1 * n / (1 + i)

if __name__ == "__main__":
    print("Kullanım örneği: -40000 * pf(0.12, 3) + 20000 * pa(0.12, 3)\n")
    ifade = input("İfadeyi girin: ")
    try:
        sonuc = eval(ifade, globals())
        print("Sonuç:", sonuc)
    except Exception as e:
        print("Hata:", e)