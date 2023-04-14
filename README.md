# Prime Hasher

🔒 A Python class for generating unique hashes based on prime numbers.

## Usage

To use the `primeHasher` class, first import it from the `primeHasher` module:

```python
from primeHasher import primeHasher
```

Then, create a new instance of the class:

```python
hasher = primeHasher()
```

You can specify the chunk size (number of primes used for each hash) when creating the instance:

```python
hasher = primeHasher(chunk_size=512)
```

To hash a string, call the `hash` method and pass in the string:

```python
hasher.hash("my secret message")
```

You can then retrieve the hash string using the `get_hash_string` method:

```python
hash_string = hasher.get_hash_string()
```

## How it works

The `primeHasher` class generates unique hashes by selecting a set of prime numbers and multiplying them together. The set of prime numbers is determined by the binary representation of the input string. Each binary digit corresponds to a prime number, and if the digit is 1, the corresponding prime number is included in the set. If the digit is 0, the number 1 is included instead.

The resulting set of primes is then multiplied together to produce a large number. This number is converted to base 36, producing a string of alphanumeric characters. If the resulting string is less than 64 characters long, the hashing process is repeated using the string as the input. If the string is longer than 64 characters, a subset of the characters is chosen based on a random seed value, and the process is repeated until a 64-character string is produced.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.
