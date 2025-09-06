def convert_length(value,from_unit,to_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid length unit provided")
    value_meters = value * conversion_factors[from_unit]
    converted_value = value_meters / conversion_factors[to_unit]
    return converted_value

def convert_weight(value,from_unit,to_unit):
    conversion_factors = {
        'kilogram': 1.0,
        'gram': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid weight unit provided")
    value_kilos = value * conversion_factors[from_unit]
    converted_value = value_kilos / conversion_factors[to_unit]
    return converted_value