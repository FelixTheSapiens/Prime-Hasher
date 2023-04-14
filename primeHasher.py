from primeFinderV1 import primeFinder

def intToBase(n, b):
    BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(BS[int(n % b)])
        n //= b
    return digits[::-1]

def divide_chunks(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]



class primeHasher:
    def __init__(self, chunk_size = 1024):
        self.__chunk_size = chunk_size
        self.__primes = []
        self.hash_string =''
        self.generate_primes(chunk_size)

    def generate_primes(self, size):
        generator = primeFinder()
        limit = size
        generator.generate_primes(limit)
        while len(generator.get_primes()) < size:
            limit*=2
            generator.generate_primes(limit)
        primes = generator.get_primes()[:size]
        self.set_primes(primes)

    def set_primes(self, primes):
        self.__primes = primes

    def get_primes(self):
        return self.__primes

    def get_chunk_size(self):
        return self.__chunk_size

    def set_chunk_size(self, new_size):
        if self.get_chunk_size() == new_size:
            return
        
        self.generate_primes(new_size)
        self.__chunk_size = new_size

    def get_hash_string(self):
        return self.hash_string

    def hash(self, input_data):
        binary_string = ''.join(format(ord(letter), 'b') for letter in input_data)
        choosen_primes = []
        primes = self.get_primes()
        chunks = divide_chunks([*binary_string], self.get_chunk_size())

        for chunk in chunks:
            for index, zero_one in enumerate([*chunk]):
                choosen_primes.append(primes[index] if zero_one == '1' else 1)

        multiple = 1
        for prime in choosen_primes:
            multiple*=prime

        base_x = intToBase(multiple, 36)
        self.hash_string = ''.join(char for char in base_x)

        if len(self.hash_string) < 64:
            self.hash(self.hash_string)

        if len(self.hash_string) > 64:
            choosen_chars = self.hash_string[0]
            seed = ord(choosen_chars)
            while len(choosen_chars) < 64:
                a = 1103515245
                c = 35142
                m = 2 ** 31
                seed = (a * seed + c) % m
                index = seed % len(base_x)
                choosen_chars+=base_x[index]
            self.hash_string = choosen_chars
