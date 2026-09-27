import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if isinstance(x, (int, float)):
        return 1.0 / (1.0 + np.exp(-x))
    arr = np.array(x, dtype=float)
    return 1.0 / (1.0 + np.exp(-arr))