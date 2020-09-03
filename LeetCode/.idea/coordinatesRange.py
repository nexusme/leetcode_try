import requests
from geopy.distance import geodesic  # 执行API调用并储存响应
import pandas as pd


def count_dis(lat, long, lat1, long1):
    result = geodesic((long, lat), (long1, lat1)).km
    print(round(result, 2))


def test():
    long_c = 120.73056
    lat_c = 31.270745
    data = []
    for i in range(0, 15):
        for i in range(0, 15):
            url = 'https://api.caiyunapp.com/v2.5/VFDGN6fLnrZxEagi/' + str(long_c)[0:9] + ',' + str(lat_c)[
                                                                                                0:9] + '/weather.json?'
            r = requests.get(url)
            response_dict = r.json()
            # print("keywords: ", str(lat_c)[0:9], str(long_c)[0:9])
            # print("actual: ", response_dict['location'][0], response_dict['location'][1])

            lat = response_dict['location'][0]
            long = response_dict['location'][1]
            resp = response_dict['result']
            respp = resp['realtime']
            # print(respp)
            cloud_rate = respp['cloudrate']
            # print('cloud_rate:', cloud_rate)

            wind = respp['wind']
            wind_speed = wind['speed']
            # print("wind speed:", wind_speed)

            precipitation = respp['precipitation']
            local = precipitation["local"]
            intensity = local['intensity']
            # print('intensity:', intensity)

            columns = ["lat", "long", "lat_real", "long_real", "cloud_rate", "wind_speed", "intensity", "dis"]
            data.append([str(lat_c)[0:9], str(long_c)[0:9], lat, long, cloud_rate, wind_speed, intensity, 0])
            lat_c += 0.01
        long_c += 0.01

    df = pd.DataFrame(data, columns=columns)
    df = df.sort()
    print(df)


test()

# count_dis(120.74056, 31.280745, 120.76056, 31.300745)
