import numpy as np
import matplotlib.pyplot as plt

def aceleration_to_velocity(a, t, v):
    '''
    V = V0 + AT
    Returns: Intregrated Velocity.
    '''
    return v + a.dot(t)

def get_velocity(data):
    '''
    Get the data and transform it in velocity via integration.
    Returns: Total Velocity
    '''
    total_velocity = []
    is_first = True
    for time in range(len(data)):
        if is_first:
            total_velocity.append( aceleration_to_velocity(data[time], time, 0) )
        else:
            total_velocity.append( aceleration_to_velocity(data[time], time, total_velocity[-1]) )
    return np.array(total_velocity)

def plot_data(x, y):
    plt.plot(x, y)
    plt.show()

data = np.genfromtxt('foo1.csv', delimiter=',').T
aceleration = np.array(data[:, :3])
dont_repeat_ur_self = np.array(range(len(aceleration)))
plot_data(dont_repeat_ur_self, aceleration[:, 0])
velocity = get_velocity(aceleration)
plot_data(dont_repeat_ur_self, velocity[:, 0])
