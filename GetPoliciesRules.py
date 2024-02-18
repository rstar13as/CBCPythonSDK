# Getting policies & rules with the SDK:

from cbc_sdk.rest_api import CBCloudAPI
from cbc_sdk.platform import Policy
from cbc_sdk.platform import Observation

# Debug logging shows the http request content from the SDK. Helps as you build if you get unexpected results back. Good to turn off before shipping it.
import logging
logging.basicConfig(level=logging.DEBUG)

api = CBCloudAPI(profile='partner')

policies = list(api.select(Policy))
for idx, policy in enumerate(policies, start=1):
	print(f"{idx}. {policy['name']}")

selected_policy = policies[1]
rules = selected_policy.get('rules')
