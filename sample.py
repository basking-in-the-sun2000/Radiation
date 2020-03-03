import solcast
import time
import pytz 

r = solcast.get_radiation_forecasts(48.438880, 13.333152, hours=24)
print(r.next_forecast) # contains the next forecast datapoint
print(r.forecasts)  # contain the next datapoints for forecast given the hours parameter

r1 = solcast.get_radiation_estimated_actuals(48.438880, 13.333152, hours=24)
print(r1.last_estimated) #contains the next forecast datapoint
print(r1.estimated_actuals) #contains the next datapoints for forecast given the hours parameter


# site_id is in the format xxxx-xxxx-xxxx-xxxx, x being a hexadecimal digit
#retrieving rooftop forcasts
r1 = solcast.get_rooftop_forcasts("site_id")

for x in r1.content['forecasts']:
	dt = x['period_end'] 
	dt = dt.replace(tzinfo=pytz.timezone('UTC'))
	dt = dt.astimezone(pytz.timezone("your timezone"))
	dt = time.mktime(dt.timetuple())

	measurement = {'power': float(x['pv_estimate']), 'power10': float(x['pv_estimate10']), 'power90': float(x['pv_estimate90']) }
	
	#dt has the epoch value, and measurements has the forcasts in kW


#sending inverter values for rooftop tuning
measurements = []
slices = 10 #sending data for 10 minutes periods
for i in inverter_values: #inverter_values has the data for the actual produced power average in kW
	temp = {}
	temp['total_power'] = str(round(i['power'],3))
	j = int(time.mktime(time.strptime(i["time"], "%Y-%m-%dT%H:%M:%SZ")))

	temp['period_end'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(j + 60 * slices ))
	temp['period'] = 'PT'+str(slices)+'M'
	measurements.append(temp)

roof = solcast.post_rooftop_measurements("site_id", measurements)
