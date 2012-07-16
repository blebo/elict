import math

def power_3ph_real(Voltage_LL, Current_L, power_factor):
    """

    """
    power_real = math.sqrt(3) * Voltage_LL * Current_L * power_factor
    return power_real

def power_3ph_real_alt(Voltage_PN, Current_L, power_factor):
    """

    """
    power_real = 3 * Voltage_PN * Current_L * power_factor
    return power_real

def power_3ph_aprnt(Voltage_LL, Current_L):
    """

    """
    power_apparent = math.sqrt(3) * Voltage_LL * Current_L
    return power_apparent

def power_3ph_aprnt_alt(Voltage_PN, Current_L):
    """

    """
    power_apparent = 3 * Voltage_PN * Current_L
    return power_apparent