# Running an Observation search:

observations = list(api.select(Observation).where(query).set_time_range(window='-30d'))
for observation in observations:
	# Looks like everything you want is already in the Observation search output
	# e.g. observation.get("event_type")
	# But you can choose to get Observation Details or Process Details if you need additional info
	# https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/platform-search-fields

	observation_details = observation.get_details()

	process_guid = observation.get("process_guid")
	process_details = api.select("Process", process_guid).get_details()
