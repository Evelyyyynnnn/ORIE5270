# Fill in the blanks in the class methods below.
# Pay attention to the documentation: it specifies the expected behavior
# of each method.


class VectorND(object):
    def __init__(self, *args):
        """Create a VectorND from a sequence of real numbers.

        The length of the sequence passed to the constructor is arbitrary.
        """
        self.vector = list(args)  # Store the sequence as a list

    def __len__(self):
        """Return the length of the vector."""
        return len(self.vector)  # Use the built-in len function on the vector list

    def __eq__(self, other):
        """Check if the vector is equal to another."""
        if len(self.vector) != len(other.vector):
            return False  # If the lengths are not equal, vectors are not equal
        return self.vector == other.vector  # Compare the lists element by element

    def __add__(self, other):
        """Add two VectorND objects and return a new VectorND."""
        if len(self.vector) != len(other.vector):
            raise ValueError("vector lengths are incompatible")  # Check for length mismatch
        # Add corresponding elements of both vectors
        return VectorND(*(a + b for a, b in zip(self.vector, other.vector)))

    def __sub__(self, other):
        """Subtract one VectorND object from another."""
        if len(self.vector) != len(other.vector):
            raise ValueError("vector lengths are incompatible")  # Check for length mismatch
        # Subtract corresponding elements of both vectors
        return VectorND(*(a - b for a, b in zip(self.vector, other.vector)))

    def __repr__(self):
        """Output the "official" string representation of the object."""
        return f"Vector: {self.vector}"  # Return the vector in the required format