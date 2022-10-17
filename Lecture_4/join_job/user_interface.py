import data_provider as prov
import logger as log

def temparature_view(sensor):
    data = prov.get_temperature(sensor)
    log.temperature_logger(data)
    return data

def preassure_view(sensor):
    data = prov.get_preassure(sensor)
    log.pressure_logger(data)
    return data

def speed_wind_view(sensor):
    data = prov.get_wind_speed(sensor)
    log.speed_wind_logger(data)
    return data