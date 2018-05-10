import numpy as np
import matplotlib.pyplot as plt

def aceleration_to_velocity(a, t, v):
    '''
    V = V0 + AT
    Returns: Intregrated Velocity.
    '''
    return v + a.dot(t)

def velocity_to_position(a, t, v, y):
    '''
    Y = Y0 + V0T + 1/2AT^2
    '''
    return y + v.dot(t) + (a.dot(t**2))/2

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

def get_position(data):
    '''
    Get the data and transform it in position via integration.
    Returns: Position Array
    '''
    total_position = []
    total_velocity = get_velocity(data)
    is_first = True
    for time in range(len(data)):
        if is_first:
            total_position.append( velocity_to_position(data[time], time, total_velocity[time], 0) )            
        else:
            total_position.append( velocity_to_position(data[time], time, total_velocity[time], total_position[-1]) ) 
    return np.array(total_position)       

def plot_data(x, y, title):
    plt.plot(x, y)
    plt.title(title)
    plt.show()

data = np.genfromtxt('data.csv', delimiter=',')# Descargo el csv tranformado en numpt array
aceleration = np.array(data[:, :3]) # Obtengo solo los 3 primeros, aceleracion X, Y y Z respectivamente
dont_repeat_ur_self = np.array(range(len(aceleration))) # Lista de array del tiempo

plot_data(dont_repeat_ur_self, aceleration[:, 0], 'ACELERACION X') # Grafica aceleracion eje x vs tiempo
# plot_data(dont_repeat_ur_self, aceleration[:, 1], 'ACELERACION Y') # Grafica aceleracion eje y vs tiempo
# plot_data(dont_repeat_ur_self, aceleration[:, 2], 'ACELERACION Z') # Grafica aceleracion eje z vs tiempo

velocity = get_velocity(aceleration) # Obtengo la velocidad con la funcion creada
plot_data(dont_repeat_ur_self, velocity[:, 0], 'VELOCIDAD X') # Grafica velocidad eje x vs tiempo
# plot_data(dont_repeat_ur_self, velocity[:, 1]) # Grafica velocidad eje y vs tiempo
# plot_data(dont_repeat_ur_self, velocity[:, 2]) # Grafica velocidad eje z vs tiempo


position = get_position(aceleration) # Obtengo la posicion con la funcion creada
plot_data(dont_repeat_ur_self, position[:, 0], 'POSICION X') # Grafica posicion eje x vs tiempo
# plot_data(dont_repeat_ur_self, position[:, 1]) # Grafica posicion eje y vs tiempo
# plot_data(dont_repeat_ur_self, position[:, 2]) # Grafica posicion eje z vs tiempo

