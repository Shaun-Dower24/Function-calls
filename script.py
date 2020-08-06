#global variables
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#function to convert fahrenheit to celcius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9

  f100_in_celcius = f_to_c(100)
  
#function to convert celcius to fahrenheit
def c_to_f(c_temp):
    return (c_temp * 9/5) + 32

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#function which multiplies mass and acceleration to create the train_force variable.
def get_force(mass,acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#function which uses the bomb_mass variable and the get_energy function to create the bomb_energy variable.
def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#function which uses get_force from an earlier function to create an equation for train_work.
def get_work(mass, acceleration, distance):
  return get_force(mass,acceleration) * distance
  
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
