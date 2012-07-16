import math

def power_AC_3ph_real(Voltage_LL, Current_L, power_factor):
    """
    Calculate three phase AC power (real).

    :param Voltage_LL: Three Phase AC Voltage, Line-Line (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_real: Real Power (W)
    :rtype float
    """
    power_real = math.sqrt(3) * Voltage_LL * Current_L * power_factor
    return power_real

def power_AC_3ph_real_alt(Voltage_PN, Current_L, power_factor):
    """
    Calculate three phase AC power (real).

    :param Voltage_PN: Three Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_real: Real Power (W)
    :rtype float
    """
    power_real = 3 * Voltage_PN * Current_L * power_factor
    return power_real

def power_AC_3ph_rctv(Voltage_LL, Current_L, power_factor):
    """
    Calculate three phase AC power (reactive).

    :param Voltage_LL: Three Phase AC Voltage, Line-Line (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_apparent: Reactive Power (VAr)
    :rtype float
    """
    power_reactive = math.sqrt(3) * Voltage_LL * Current_L * math.sin(math.acos(power_factor))
    return power_reactive

def power_AC_3ph_rctv_alt(Voltage_PN, Current_L, power_factor):
    """
    Calculate three phase AC power (reactive).

    :param Voltage_PN: Three Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_apparent: Reactive Power (VAr)
    :rtype float
    """
    power_reactive = 3 * Voltage_PN * Current_L * math.sin(math.acos(power_factor))
    return power_reactive

def power_AC_3ph_aprnt(Voltage_LL, Current_L):
    """
    Calculate three phase AC power (apparent).

    :param Voltage_LL: Three Phase AC Voltage, Line-Line (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :returns power_apparent: Apparent Power (VA)
    :rtype float
    """
    power_apparent = math.sqrt(3) * Voltage_LL * Current_L
    return power_apparent

def power_AC_3ph_aprnt_alt(Voltage_PN, Current_L):
    """
    Calculate three phase AC power (apparent).

    :param Voltage_PN: Three Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :returns power_apparent: Apparent Power (VA)
    :rtype float
    """
    power_apparent = 3 * Voltage_PN * Current_L
    return power_apparent

def power_AC_1ph_real(Voltage_PN, Current_L):
    """
    Calculate single phase AC power (real).

    :param Voltage_PN: Single Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_real: Real Power (W)
    :rtype float
    """
    power_real = Voltage_PN * Current_L * power_factor
    return power_real

def power_AC_1ph_rctv(Voltage_PN, Current_L, power_factor):
    """
    Calculate single phase AC power (reactive).

    :param Voltage_PN: Single Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :param power_factor: Power Factor
    :type float
    :returns power_reactive: Reactive Power (VAr)
    :rtype float
    """
    power_reactive = Voltage_PN * Current_L * math.sin(math.acos(power_factor))
    return power_reactive

def power_AC_1ph_aprnt(Voltage_PN, Current_L):
    """
    Calculate single phase AC power (apparent).

    :param Voltage_PN: Single Phase AC Voltage, Phase-Neutral (V)
    :type float
    :param Current_L: Line Current (A)
    :type float
    :returns power_apparent: Apparent Power (VA)
    :rtype float
    """
    power_apparent = Voltage_PN * Current_L
    return power_apparent

def power_DC(Voltage, Current):
    """
    Calculate DC power.

    :param Voltage: DC Voltage (V)
    :type float
    :param Current: Line Current (A)
    :type float
    :returns power: Power (W)
    :rtype float
    """
    power = Voltage * Current
    return power