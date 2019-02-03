# Readable ID

Use readableID to transform integer item ids to readable, nonconsecutive ids

Criteria for a good readable id:
- as short as possible
- should contain only numbers and characters that are easy to distinguish regardless of font, e.g. no `0` vs `O`.
- not create any duplicates with increase number of items!
- consecutive numbers should not create consecutive ids

```python
id_generator.generate_id(0)  # returns 9MBE
id_generator.generate_id(1)  # returns QCAH
```

This library does not use any dependencies outside of the python std lib!


### Installing

Just install using `pip`:
```
pip install readableID
```

### Usage

Usage is very simple after creating an object, just call the `generate_id` method:
```python
import readableID

id_generator = readableID.ReadableID()

for x in range(1000):
    readable_id = id_generator.generate_id(x)
    print(readable_id)
```

Generally it is easiest to use this library in conjunction with a database that allows auto-incrementing ids 
which you use as input for the generate_id method. 


### Adapting parameters to your needs

To create your own unique numbers, you can salt them using the following parameters:

```python
import readableID
id_generator = readableID.ReadableID(
    charset=readableID.DEFAULT_CHARSET, 
    min_length=readableID.DEFAULT_MINIMAL_LENGTH,
    prime=readableID.DEFAULT_PRIME, 
    xor=readableID.DEFAULT_XOR
)
```

#### `charset`:

The `charset` controls the allowed characters. There are 2 criteria for this string:
1. characters must be unique
2. length of string must be a power of 2, e.g. 8, 16, 32, 64

The default charset is chosen to create minimal confusion for readers, since only very distinct chars were chosen.

#### `min_length`:

The `min_length` controls the length of the generated ids. The library will fit as many item ids into the given `min_length` as possible,
but if your number of items grows beyond this number, the ids will automatically get longer!

Example: with the default parameters, you can fit `32 ^ 4` item ids into 4 characters.
So if you call `generate_id` with any number `0 <= x < 32^4` it will produce a id with length of 4.
Starting at `32^4`, you will see ids with length of 5! Starting at `32^5` you will see ids with length of 6 and so on.

#### `prime`:

The `prime` parameter allows you to change how the next number is chosen. It is critical that this is a `prime number > 2` if you want to avoid duplicates!

If you are unsure - you can skip changing this parameter and rather chose a different `xor` value!

#### `xor`:

The `xor` value allows you to create different sequences of numbers, you can chose `any integer >= 0`, 
but generally it makes more since to pick a number:
`100 < x < len(charset) ^ min_length`. Changing `xor` will not have as big of an effect as changing the `prime` value, 
but will still create reasonably different sequences of numbers/  