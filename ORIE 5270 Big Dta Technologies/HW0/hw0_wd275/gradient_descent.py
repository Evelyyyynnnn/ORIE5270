import numpy
import numpy.linalg as linalg


def loss_function(A, b, x):
    """Evaluates the loss (1 / 2) * |Ax - b|^2."""
    # Calculate Ax - b
    residual = np.dot(A, x) - b
    # Return the loss function (1/2) * ||Ax - b||^2
    return 0.5 * np.dot(residual, residual)

def gradient(A, b, x):
    """Evaluates the gradient of (1 / 2) * |Ax - b|^2."""
    # Compute the gradient: A^T (Ax - b)
    residual = np.dot(A, x) - b
    grad = np.dot(A.T, residual)
    return grad

def gradient_descent(A, b, x_0, num_iterations):
    """Runs gradient descent to minimize the loss (1 / 2) * |Ax - b|^2."""
    # Initialize x as x_0
    x = x_0
    # Iterate num_iterations times
    for i in range(num_iterations):
        # Calculate the gradient at x
        grad = gradient(A, b, x)
        # Compute Polyak step size (1 / ||A^T(Ax - b)||^2)
        grad_norm = np.linalg.norm(grad)
        if grad_norm != 0:
            step_size = 1 / grad_norm**2
        else:
            step_size = 1e-6  # To avoid division by zero if the gradient is zero

        # Update x using gradient descent
        x = x - step_size * grad

    # Calculate the final gradient norm
    grad_norm = np.linalg.norm(gradient(A, b, x))
    # Return the final solution and gradient norm
    return x, grad_norm