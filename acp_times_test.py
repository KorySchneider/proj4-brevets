"""
Nose tests for acp_times.py

Note that negative controle distances are not tested, as the functions in acp_times.py
will not be called if a negative controle distance is given. Same goes for controle
distances that are more than 10% over the length of the brevet length.

Test data from https://rusa.org/octime_acp.html
"""

import arrow, acp_times

def test_open_time():
    assert acp_times.open_time(0,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:00:00+00:00'
    assert acp_times.open_time(1,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:02:00+00:00'
    assert acp_times.open_time(2,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:04:00+00:00'
    assert acp_times.open_time(50,  200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T01:28:00+00:00'
    assert acp_times.open_time(100, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T02:56:00+00:00'
    assert acp_times.open_time(199, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:51:00+00:00'
    assert acp_times.open_time(200, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:53:00+00:00'
    assert acp_times.open_time(201, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:53:00+00:00'
    assert acp_times.open_time(220, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:53:00+00:00'

def test_close_time():
    assert acp_times.close_time(0,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T01:00:00+00:00'
    assert acp_times.close_time(1,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:04:00+00:00'
    assert acp_times.close_time(2,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:08:00+00:00'
    assert acp_times.close_time(50,  200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T03:20:00+00:00'
    assert acp_times.close_time(100, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T06:40:00+00:00'
    assert acp_times.close_time(199, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:16:00+00:00'
    assert acp_times.close_time(200, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:30:00+00:00'
    assert acp_times.close_time(201, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:30:00+00:00'
    assert acp_times.close_time(220, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:30:00+00:00'
