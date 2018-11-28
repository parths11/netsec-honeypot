import json
from pprint import pprint
from geolite2 import geolite2
from collections import Counter
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def stat_plot(x, y):
    plt.bar(range(len(x)), y, align='center')
    plt.xticks(range(len(x)), x)
    plt.show()

def show_on_map(ip):
    lon = []
    lat = []
    for i in ip:
        reader = geolite2.reader()
        x = reader.get(i)
        if x is not None:
            lat.append(float(x['location']['latitude']))
            lon.append(float(x['location']['longitude']))
    map = Basemap(projection='cyl')

    # map.drawmapboundary(fill_color='aqua')
    # map.fillcontinents(color='coral',lake_color='aqua')
    # map.drawcoastlines()
    map.bluemarble()

    x, y = map(lon, lat)

    map.scatter(x, y, marker='.',color='r')

    plt.show()
    # print(lon)
    # print(lat)

def loc_stat(ip):
    countries =[]
    for i in ip:
        reader = geolite2.reader()
        x = reader.get(i)
        if x is not None:
            try:
                countries.append(x['registered_country']['names']['en'])
            except KeyError:
                countries.append(x['country']['names']['en'])
        else:
            countries.append('others')
    cnt = Counter()
    for word in countries:
        cnt[word] += 1
    return cnt

def store_ips(data):
    x = []
    for i in data:
        x.append(i["src_ip"])
    return x

def json_readr(file):
    x = []
    for line in open(file, mode="r"):
        x.append(json.loads(line))
    return x

f1 = 'cowrie.json'
f2 = 'cowrie.json.2018-11-08'
f3 = 'cowrie.json.2018-11-07'
f4 = 'cowrie.json.2018-11-06'
data = json_readr(f1) + json_readr(f2) + json_readr(f3) + json_readr(f3)
src_ips = set(store_ips(data))
desh_stat = dict(loc_stat(src_ips))
d = Counter(desh_stat)
y = list(i[1] for i in d.most_common(10))
x = list(i[0] for i in d.most_common(10))
stat_plot(x, y)
show_on_map(src_ips)
