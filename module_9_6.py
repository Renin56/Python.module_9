def all_variants(text):
    n = len(text)

    for i in range(n):
        for j in range(i + 1, n + 1):
            yield text[i:j]


al = all_variants('abc')
for i in al:
    print(i)
