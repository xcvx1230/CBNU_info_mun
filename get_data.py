#!/usr/bin/env python3

from gps.gps_class import GPS
import time
import sys
import pymysql
db=pymysql.connect(host="101.101.166.68",user = "root",passwd="1q2w3e4r!",db ="drone")
def main():
    gps_data = GPS(device='/dev/ttyAMA0')
    print("Press Control-C to stop.")
    gps_data.start()

    try:
        while True:
            print("{}, lat: {}, lon: {}, elevation: {}ft, speed: {}mph".format(
                gps_data.local_time,
                gps_data.lat,
                gps_data.lon,
                gps_data.altitude,
                gps_data.mph))
#            with db.cursor() as cur:
#                sql="insert into end_project(lat,lon,PM25,PM10) select %s,%s,PM25,PM10 from pm_sensor;"%(gps_data.lat,gps_data.lon)
#                cur.execute(sql)
#                db.commit()
            time.sleep(15)
    except KeyboardInterrupt:
        gps_data.stop()
        sys.exit(0)

if __name__ == '__main__':
    main()