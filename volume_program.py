#! /usr/bin/python3

import datetime
import calendar
import csv

#====================================================================================
#========== Given a datafile containing data in a format: ===========================
#========== Time: YYYY-MM-DD ; Rainfall (mm) ; Evaporation (mm) =====================
#========== Function process_data calculates and returns the volume of water ========
#========== collecting in the Jojo tank and the pool, as well as volume pumped ======
#========== out of the Jojo and into the pool. ======================================
#========== The function accepts datafile and case = {1,2} as its arguments. ========

def process_data(data,case):
    daily_evapo = []
    vol_jojo = []
    vol_rain_pool = []
    vol_pool = []
    vol_left_pool = []
    date_object = []
    pump_out = []

    with open (data, 'r') as f:
        f.readline()
        tot_water_jojo = 0.
        tot_water_pool = 0.
        tot_rain_pool = 0.
        for lines in f:
            line = lines.strip().split(',')
            select_data = line[0]
            my_date = datetime.datetime.strptime(line[0], '%Y-%m-%d').weekday()
            week_day = calendar.day_name[my_date]
            rainfall = float(line[1])
            evaporation = float(line[2])


            #========================================================================
            #============ Calculate total volume in Jojo and Pool ===================
            #========================================================================

            # Total rain per day in a Jojo
            # Assumption: All rain falling on the roof accumulates 
            #             in the Jojo tank; roof_surface_area = 10. m^2
            roof_surface_area = 10.
            water_jojo = rainfall*roof_surface_area  # Units: L
            
            # Jojo tank has a max capacity of 1000 L
            tank_capacity = 1000.
            if (my_date != 3 and tot_water_jojo < tank_capacity):
                tot_water_jojo += water_jojo
            if (my_date != 3 and tot_water_jojo >= tank_capacity):
                tot_water_jojo = tank_capacity
            
            # Total rain per day in a pool
            # Assumption: pool_surface_area = 6. m^2
            pool_surface_area = 6.
            water_pool = rainfall*pool_surface_area  # Units: L

            # Pool has a max capacity of 20000 L
            pool_capacity = 20000.
            if (my_date != 3 and tot_water_pool < pool_capacity):
                tot_rain_pool += water_pool
            
            if (select_data=='2015-01-01'):
                if (case==1):
                    tot_rain_pool = 0.
                else:
                    tot_rain_pool = 10000.

            # Check if it's Thursday and empty jojo into pool
            if (my_date == 3):
                if(tot_water_pool < pool_capacity):
                    tot_water_pool = tot_rain_pool + tot_water_jojo
                    pump_out.append(tot_water_jojo)
                else:
                    tot_water_pool = pool_capacity
                tot_water_jojo = 0.

            #========================================================================
            #============ Volume evaporating from the pool ==========================
            #========================================================================
            water_evaporating = evaporation*pool_surface_area

            # Calculate total left after evaporation
            total_left = tot_water_pool - water_evaporating
            
            # Append solutions into empty lists for use later
            daily_evapo.append(water_evaporating)
            vol_jojo.append(tot_water_jojo)
            vol_rain_pool.append(tot_rain_pool)
            vol_pool.append(tot_water_pool)
            vol_left_pool.append(total_left)
            date_object.append(line[0])

    return (date_object,vol_jojo,vol_left_pool,pump_out)

#====================================================================================
#============= Pass relevant info to function arguments =============================

# No water in pool on the 2015-01-01: case = 1
# Pool 50% full on the 2015-01-01: case = 2

def main():
    case = 2
    path = 'Scientific Programmer Assessment data sheet.csv'
    date_object,vol_jojo,vol_left_pool,pump_out = process_data(path,case)
    tot_pumped = 0.0

    for i in range(len(date_object)):
        value = datetime.datetime.strptime(date_object[i],'%Y-%m-%d').strftime('%Y%m%d')
        if value=='20160115':
            print('15 January 2016')
            print('Water in tank: ', vol_jojo[i])
            print('Water in pool: ', vol_left_pool[i])
            print('===================================')

        if value=='20161231':
            print('31 December 2016: ')
            print('Water in tank: ', vol_jojo[i])
            print('Water in pool: ', vol_left_pool[i])
            print('===================================')

    for i, pump_value in enumerate(pump_out):
        value = datetime.datetime.strptime(date_object[i],'%Y-%m-%d').strftime('%Y%m%d')
        if (value>='20150101' and value<='20191231'):
            tot_pumped += float(pump_value)

    print('Between 01 January 2015 and 31 December 2019')
    print('Total water pumped: ', tot_pumped)

if __name__=='__main__':
    main()

