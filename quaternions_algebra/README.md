# quaternions_algebra: Quaternion Algebra

## Overview

`quaternions_algebra` is a Python package that provides a Quaternion class for performing quaternion algebra. Quaternions are mathematical entities that extend complex numbers and are commonly used in computer graphics, robotics, and other fields.

## Installation

You can install `quaternions_algebra` using pip:

    pip install quaternions_algebra

## Usage

Here's a quick example of how to use the `Quaternion` class:

```python
    from quaternions_algebra import Quaternion

    # Create quaternions
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)

    # Perform operations
    result_addition = q1 + q2
    result_multiplication = q1 * q2

    print("Quaternion Addition:", result_addition)
    print("Quaternion Multiplication:", result_multiplication)
```

## Contributing

As an open  source project, we welcome contributers of all helpful forms.

## License

This project is licensed under the MIT License - see the root `LICENSE.md` file for details.
