def water_column_height(tower_height, tank_height):
    column_height = tower_height + (3 * tank_height / 4)
    return column_height

def pressure_gain_from_water_height(height):
    rho = 998.2  # density of water in kilogram/meter^3
    g = 9.80665  # acceleration due to gravity in meter/second^2
    pressure_gain = (rho * g * height) / 1000
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2  # density of water in kilogram/meter^3
    d = pipe_diameter
    L = pipe_length
    v = fluid_velocity
    f = friction_factor

    pressure_loss = -((f * L * rho * (v**2)) / (2000 * d))
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2  # density of water in kilogram/meter^3
    v = fluid_velocity
    n = quantity_fittings

    pressure_loss = -0.04 * rho * (v**2) * n / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2  # density of water in kilogram/meter^3
    d = hydraulic_diameter
    v = fluid_velocity
    mu = 0.0010016  # dynamic viscosity of water in Pascal seconds

    reynolds = (rho * d * v) / mu
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    rho = 998.2  # density of water in kilogram/meter^3
    v = fluid_velocity
    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter

    k = (0.1 + (50 / R)) * ((D/d)**4 - 1)
    pressure_loss = (-k * rho * (v**2)) / 2000
    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Print the pressure in kPa and psi
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    pressure_psi = kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure_psi:.2f} psi")

def kpa_to_psi(pressure_kpa):

    conversion_factor = 0.145
    pressure_psi = pressure_kpa * conversion_factor
    return pressure_psi

if __name__ == "__main__":
    main()
