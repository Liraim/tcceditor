import datetime
import sqlite3
import argparse
import time


def enable(client, service):
    print "Enable service {} for client {}...".format(service, client)
    conn = sqlite3.connect("TCC.db")
    conn.execute("INSERT or REPLACE INTO access VALUES('{}','{}',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,{})".format(
        service, client, int(time.mktime(datetime.datetime.now().timetuple()))
    ))
    conn.commit()
    conn.close()


def disable(client, service):
    print "Disable service {} for client {}...".format(service, client)
    conn = sqlite3.connect("TCC.db")
    conn.execute("INSERT or REPLACE INTO access VALUES('{}','{}',0,0,1,NULL,NULL,NULL,'UNUSED',NULL,0,{})".format(
        service, client, int(time.mktime(datetime.datetime.now().timetuple()))
    ))
    conn.commit()
    conn.close()


def remove(client, service):
    print "Remove service {} for client {}...".format(service, client)
    conn = sqlite3.connect("TCC.db")
    conn.execute("DELETE FROM access WHERE service='{}' AND client='{}'".format(
        service, client
    ))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    import sys

    parser = argparse.ArgumentParser()
    sp = parser.add_subparsers(dest='method')
    sp_enable = sp.add_parser('enable', help="Enable service for client app")
    sp_disable = sp.add_parser('disable', help="Disable service for client app")
    sp_remove = sp.add_parser('remove', help="Remove service + client record (like tccutil reset)")
    parser.add_argument("--client", action="store", help="client application id")
    parser.add_argument("--service", action="store", help="service id")

    parsed = parser.parse_args(sys.argv[1:])
    if parsed.method == 'enable':
        enable(parsed.client, parsed.service)
    elif parsed.method == 'disable':
        disable(parsed.client, parsed.service)
    elif parsed.method == 'remove':
        remove(parsed.client, parsed.service)

