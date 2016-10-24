"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    # Max speeds for various brevet lengths
    max_speeds = { 200: 34,
                   300: 32,
                   400: 32,
                   600: 30,
                  1000: 28 }

    if control_dist_km > brevet_dist_km:
        control_dist_km = 200

    time = str(float(control_dist_km / max_speeds[brevet_dist_km])).split('.')
    hours = time[0]
    minutes = str(int(round(float('.' + time[1]) * 60)))

    brevet_start_time = arrow.get(brevet_start_time)
    open_time = brevet_start_time.replace(hours=+int(hours), minutes=+int(minutes))

    return str(open_time.isoformat())

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # rusa.org/pages/rulesForRiders
    # article 9

    # Min speeds for various brevet lengths
    min_speeds = { 200: 15,
                   400: 15,
                   600: 15,
                  1000: 11.428 }

    # Overall time limits for brevets according to distance
    # brevet_distance: (HH,MM)
    end_times = { 200: (13,30),
                  300: (20,00),
                  400: (27,00),
                  600: (40,00),
                 1000: (75,00) }

    # TODO controle can't be >20% further than brevet dist?
    # really really big numbers? ^ this would handle that

    if control_dist_km == 0:
        close_time = brevet_start_time.replace(hours=+1)
    elif control_dist_km >= brevet_dist_km:
        hours = end_times[brevet_dist_km][0]
        minutes = end_times[brevet_dist_km][1]
        close_time = brevet_start_time.replace(hours=+int(hours), minutes=+int(minutes))
    else:
        time = str(float(control_dist_km / min_speeds[brevet_dist_km])).split('.')
        hours = time[0]
        minutes = str(int(round(float('.' + time[1]) * 60)))
        close_time = brevet_start_time.replace(hours=+int(hours), minutes=+int(minutes))

    return str(close_time.isoformat())
