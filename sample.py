import solcast

r = solcast.get_radiation_forecasts(48.438880, 13.333152, hours=24)
print(r.next_forecast) # contains the next forecast datapoint
print(r.forecasts)  # contain the next datapoints for forecast given the hours parameter

r1 = solcast.get_radiation_estimated_actuals(48.438880, 13.333152, hours=24)
print(r1.last_estimated) #contains the next forecast datapoint
print(r1.estimated_actuals) #contains the next datapoints for forecast given the hours parameter
