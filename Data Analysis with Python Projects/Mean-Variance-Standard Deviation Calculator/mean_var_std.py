import numpy as np

def calculate(list):
    # test 3
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        n_array_3d = np.array(list).reshape(3, 3)
        n_array_flat = np.array(list)

        # test 1
        # test 2
        calculations = {
            'mean': mean(n_array_3d, n_array_flat), 
            'variance': variance(n_array_3d, n_array_flat),
            'standard deviation': standard_deviation(n_array_3d, n_array_flat),
            'max': max(n_array_3d, n_array_flat),
            'min': min(n_array_3d, n_array_flat),
            'sum': sum(n_array_3d, n_array_flat)
        }

    return calculations

def mean(n_3d, n_flat):
    mean_3d_axis1 = np.mean(n_3d, axis=0).tolist()
    mean_3d_axis2 = np.mean(n_3d, axis=1).tolist()
    mean_flat = np.mean(n_flat).tolist()

    return [mean_3d_axis1, mean_3d_axis2, mean_flat]

def variance(n_3d, n_flat):
    variance_3d_axis1 = np.var(n_3d, axis=0).tolist()
    variance_3d_axis2 = np.var(n_3d, axis=1).tolist()
    variance_flat = np.var(n_flat).tolist()

    return [variance_3d_axis1, variance_3d_axis2, variance_flat]

def standard_deviation(n_3d, n_flat):
    standard_deviation_3d_axis1 = np.std(n_3d, axis=0).tolist()
    standard_deviation_3d_axis2 = np.std(n_3d, axis=1).tolist()
    standard_deviation_flat = np.std(n_flat).tolist()

    return [standard_deviation_3d_axis1, standard_deviation_3d_axis2, standard_deviation_flat]

def max(n_3d, n_flat):
    max_3d_axis1 = np.max(n_3d, axis=0).tolist()
    max_3d_axis2 = np.max(n_3d, axis=1).tolist()
    max_flat = np.max(n_flat).tolist()

    return [max_3d_axis1, max_3d_axis2, max_flat]

def min(n_3d, n_flat):
    min_3d_axis1 = np.min(n_3d, axis=0).tolist()
    min_3d_axis2 = np.min(n_3d, axis=1).tolist()
    min_flat = np.min(n_flat).tolist()

    return [min_3d_axis1, min_3d_axis2, min_flat]

def sum(n_3d, n_flat):
    sum_3d_axis1 = np.sum(n_3d, axis=0).tolist()
    sum_3d_axis2 = np.sum(n_3d, axis=1).tolist()
    sum_flat = np.sum(n_flat).tolist()

    return [sum_3d_axis1, sum_3d_axis2, sum_flat]