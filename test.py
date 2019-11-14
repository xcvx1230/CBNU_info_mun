import pymysql

db = pymysql.connect(host="101.101.166.68",user = "root",passwd="1q2w3e4r!",db ="drone")
try:
    with db.cursor() as cur :
        a=14
        b=15
        #dql="delete from pm_sensor;"
        #cql="update pm_sensor set PM25=NULL,PM10=NULL;"
        #qql="insert into pm_sensor value(10,11);"
        sql="select*from end_project;"
        
        #sql="insert into end_project(lat,lon,PM25,PM10) select 9,11,PM25,PM10 from pm_sensor;"
        #sql="insert into pm_sensor value(1,6);"
        
        #cur.execute(dql)
        #cur.execute(cql)
        #cur.execute(qql)
        cur.execute(sql)
        
        db.commit()
        for row in cur.fetchall():
            print row[0],row[1],row[2],row[3]
finally :
    db.close()
    
    