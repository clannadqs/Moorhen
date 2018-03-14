import elasticsearch
import os
import json


#indexes mappings such as elasticsearch specific mappings and Shipper specific mappings such as
#expectedMetrics.json. Since nodes can be different from one another, no set mappings or metrics 
#can be assumed at the hub. With this script, users will be able to automate the indexing of their 
#mappings and expectedMetrics to a specified elasticsearch index for use by elasticsearch and 
#queries to obtain expectedMetrics mappings from any node, or hub, on the same network. Allowing for
#a one time automated indexing from each node at setup time.
