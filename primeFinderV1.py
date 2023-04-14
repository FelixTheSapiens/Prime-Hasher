import time

class primeFinder:
    def __init__(self):
        self.primes = []
        self.range_numbers = []
        self.start_time = None
        self.percentage = None

    def generate_primes(self, n):
        self.range_numbers = [True] * (n - 1)
        self.start_time = time.time()

        for num in range(2, n + 1):
            if self.range_numbers[num - 2]:
                self.primes.append(num)
                index = num * num
                while index <= n:
                    self.range_numbers[index - 2] = False
                    index += num

        self.percentage = (len(self.primes) / (n - 1)) * 100

    def print_results(self):
        print(f'Percentage of Primes: {self.percentage}%')
        print(f'Execution Time: {(time.time() - self.start_time)} seconds')

    def get_primes(self):
        return self.primes