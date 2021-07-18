def reverse_csv(src: str, dst: str, headers: int = 0) -> None:
    with open(src, "r") as fr:
        data = fr.readlines()
        if headers:
            data_2_write = data[:headers] + data[::-1][:-headers]
        else:
            data_2_write = data[::-1]

    with open(dst, "w") as fw:
        fw.writelines(data_2_write)
