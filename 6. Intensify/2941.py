cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


def main():
    cro_in = str(input())
    count = 0
    for ca in cro:
        count += cro_in.count(ca)
        cro_in = cro_in.replace(ca, "*")
    cro_in = cro_in.replace("*", "")
    count += len(cro_in)
    print(count)


if __name__ == "__main__":
    main()
