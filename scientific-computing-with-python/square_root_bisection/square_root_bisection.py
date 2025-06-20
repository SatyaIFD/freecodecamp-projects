def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Approximates the square root of a non-negative number using the bisection method.
    
    Parameters:
    - square_target (float): The number to find the square root of.
    - tolerance (float): The acceptable error margin.
    - max_iterations (int): Maximum iterations to prevent infinite loops.
    
    Returns:
    - float or None: Approximate square root if successful, else None.
    """
    # Handle special cases
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Initialize the bounds for bisection
        low = 0
        high = max(1, square_target)
        root = None

        # Perform binary search for square root
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid ** 2

            # Check if mid^2 is close enough to the target
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        # Handle case where result did not converge in given iterations
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')
    
    return root


# Test the function with an example
N = 16
square_root_bisection(N)
