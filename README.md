# energeretailer

next version:
1. two database,one for reading ,one for writing,reduce the database pressure
2. store the output in the redis, and get it from redis, so to get the output can be faster, just as the current system


Test links:

http://localhost:8000/api/bill?icp_id=33&startdate=2018-06-14 00:30:00&enddate=2018-06-16 00:30:00

http://localhost:8000/api/output?icp_id=33&startdate=2018-06-14 00:30:00&enddate=2018-06-16 00:30:00&role=X

http://localhost:8000/api/page?icp_id=33

http://localhost:8000/api/key?startdate=2018-06-14 00:30:00&enddate=2018-06-16 00:30:00