import matplotlib.pyplot as plt


def save_image(x: list[int], ys: list[list[float]], labels: list[str], out: str, folder: str):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    for y, label in zip(ys, labels):
        ax.plot(x, y, label=label)
    plt.xlabel("Размер входных данных, N")
    plt.ylabel("Время выполнения, секунды")
    plt.legend()
    plt.title(folder)
    fig.savefig(f"../{folder}/{out}.png")
    plt.close(fig)


def draw_data(data: list[dict], folder: str):
    slow_data = list(
        map(lambda x: x["seconds"], filter(lambda x: x["func_name"] == "f_slow", data))
    )
    fast_data = list(
        map(lambda x: x["seconds"], filter(lambda x: x["func_name"] == "f_fast", data))
    )
    n = list(map(lambda x: x["n"], filter(lambda x: x["func_name"] == "f_fast", data)))

    save_image(n, [fast_data], ["Быстрый алгоритм"], "Быстрый алгоритм", folder)
    save_image(n, [slow_data], ["Медленный алгоритм"], "Медленный алгоритм", folder)
    save_image(
        n,
        [fast_data, slow_data],
        ["Быстрый алгоритм", "Медленный алгоритм"],
        "Объединение",
        folder,
    )

