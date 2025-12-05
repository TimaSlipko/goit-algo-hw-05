import timeit

from kmp import kmp_search
from bm import bm_search
from rk import rk_search

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def measure_time(algorithm, text, pattern, iterations=1000):
    time = timeit.timeit(
        lambda: algorithm(text, pattern),
        number=iterations
    )
    return time / iterations

def main():
    texts = {
        'a1.txt': read_file('a1.txt'),
        'a2.txt': read_file('a2.txt')
    }
    
    patterns = {
        'a1.txt': [' якими можна видати', 'аіівврпп рап'],
        'a2.txt': [' блоку можна відсорту', '1234 праоап']
    }
    
    algorithms = {
        'Boyer-Moore': bm_search,
        'Knuth-Morris-Pratt': kmp_search,
        'Rabin-Karp': rk_search
    }
    
    for doc_name, text in texts.items():
        for pattern in patterns[doc_name]:
            for algo_name, algo_func in algorithms.items():
                time = measure_time(algo_func, text, pattern)
                print(f"{doc_name}, {pattern}, {algo_name}, {time:.6f}")

if __name__ == "__main__":
    main()
