def multiplication_table(num: int) -> None:
    for i in range(1, 10):
        for j in range(1, num+1):
            print(f"{i} * {j} = {i*j}", end="\t")
        print()

multiplication_table(5) # была использованна процедурная парадигма 