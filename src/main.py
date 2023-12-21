import json


from random import seed

from test_count_letters import generate_data as count_letters_generate_data
from test_find_element import generate_data as find_element_generate_data
from test_fibonacci_numbers import generate_data as fibonacci_numbers_generate_data

from draw_charts import draw_data

use_cache = True


if __name__ == "__main__":
    seed(42)
    # --------- example 1 ---------
    if use_cache:
        with open("../data/count_letters_data.json") as fp:
            count_letters_data = json.load(fp)
    else:
        count_letters_data = count_letters_generate_data(30_000)

        with open("../data/count_letters_data.json", "w") as fp:
            json.dump(count_letters_data, fp, indent=2)

    draw_data(count_letters_data, "count_letters") 

    # --------- example 2 ---------
    if use_cache:
        with open("../data/find_element_data.json") as fp:
            find_element_data = json.load(fp)
    else:
        find_element_data = find_element_generate_data(1_000_000)

        with open("../data/find_element_data.json", "w") as fp:
            json.dump(find_element_data, fp, indent=2)

    draw_data(find_element_data, "find_element")

    # --------- example 3 ---------
    if use_cache:
        with open("../data/fibonacci_numbers_data.json") as fp:
            fibonacci_numbers_data = json.load(fp)
    else:
        fibonacci_numbers_data = fibonacci_numbers_generate_data(41)

        with open("../data/fibonacci_numbers_data.json", "w") as fp:
            json.dump(fibonacci_numbers_data, fp, indent=2)

    draw_data(fibonacci_numbers_data, "fibonacci_numbers")
