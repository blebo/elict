import math

def power_3ph_real(Voltage_LL, Current_L, power_factor):
    """
    Calculate 3 phase power (real).

    :param Voltage_LL: 3 Phase Voltage, Line-Line (V)
    :param Current_L: Line Current (A)
    :param power_factor: Power Factor
    :returns power_real: Real Power (W)
    """
    power_real = math.sqrt(3) * Voltage_LL * Current_L * power_factor
    return power_real

def power_3ph_real_alt(Voltage_PN, Current_L, power_factor):
    """
    Calculate 3 phase power (real).

    :param Voltage_PN: 3 Phase Voltage, Phase-Neutral (V)
    :param Current_L: Line Current (A)
    :param power_factor: Power Factor
    :returns power_real: Real Power (W)
    """
    power_real = 3 * Voltage_PN * Current_L * power_factor
    return power_real

def power_3ph_aprnt(Voltage_LL, Current_L):
    """
    Calculate 3 phase power (apparent).

    :param Voltage_LL: 3 Phase Voltage, Line-Line (V)
    :param Current_L: Line Current (A)
    :param power_factor: Power Factor
    :returns power_apparent: Apparent Power (W)
    """
    power_apparent = math.sqrt(3) * Voltage_LL * Current_L
    return power_apparent

def power_3ph_aprnt_alt(Voltage_PN, Current_L):
    """
    Calculate 3 phase power (apparent).

    :param Voltage_PN: 3 Phase Voltage, Phase-Neutral (V)
    :param Current_L: Line Current (A)
    :param power_factor: Power Factor
    :returns power_apparent: Apparent Power (W)
    """
    power_apparent = 3 * Voltage_PN * Current_L
    return power_apparent