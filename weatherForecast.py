#!/data/data/com.termux/files/usr/bin/python
import urllib
import  re, urllib.request
from bs4 import BeautifulSoup
import json

# 3日天气预报函数
def day3WeatherForecast():
    # 3日天气信息链接
    day3Url = "https://free-api.heweather.com/s6/weather/forecast?location=hefei&key=322389fe745246a88c9371a867475438"
    # 获取天气链接返回的网页字符串，转换成json对象
    day3html = urllib.request.urlopen(day3Url).read()
    day3html = day3html.decode('utf-8') 
    day3json = json.loads(day3html)

    #print(day3json)    # 测试代码

    #定义天气预报的各个变量信息
    # 地点
    location = day3json['HeWeather6'][0]['basic']['location']
    # 更新时间
    update_time = day3json['HeWeather6'][0]['update']['loc']
    
    # 今天信息
    today_date = day3json['HeWeather6'][0]['daily_forecast'][0]['date']
    # 白天天气
    today_weather = day3json['HeWeather6'][0]['daily_forecast'][0]['cond_txt_d']
    # 夜晚天气
    tonight_weather = day3json['HeWeather6'][0]['daily_forecast'][0]['cond_txt_n']
    # 风向
    today_wind_dir = day3json['HeWeather6'][0]['daily_forecast'][0]['wind_dir']
    # 风力
    today_wind_sc = day3json['HeWeather6'][0]['daily_forecast'][0]['wind_sc']
    # 最高温和最低温
    today_tmp_max = day3json['HeWeather6'][0]['daily_forecast'][0]['tmp_max']
    today_tmp_min = day3json['HeWeather6'][0]['daily_forecast'][0]['tmp_min']
    
    #明天信息
    tomorrow_date = day3json['HeWeather6'][0]['daily_forecast'][1]['date']
    # 白天天气
    tomorrow_weather = day3json['HeWeather6'][0]['daily_forecast'][1]['cond_txt_d']
    # 夜晚天气
    tomorrow_weather_n = day3json['HeWeather6'][0]['daily_forecast'][1]['cond_txt_n']
    # 风向
    tomorrow_wind_dir = day3json['HeWeather6'][0]['daily_forecast'][1]['wind_dir']
    # 风力
    tomorrow_wind_sc = day3json['HeWeather6'][0]['daily_forecast'][1]['wind_sc']
    # 最高温和最低温
    tomorrow_tmp_max = day3json['HeWeather6'][0]['daily_forecast'][1]['tmp_max']
    tomorrow_tmp_min = day3json['HeWeather6'][0]['daily_forecast'][1]['tmp_min']
    
    #后天信息
    tday_tomorrow_date = day3json['HeWeather6'][0]['daily_forecast'][2]['date']
    # 白天天气
    tday_tomorrow_weather = day3json['HeWeather6'][0]['daily_forecast'][2]['cond_txt_d']
    # 夜晚天气
    tday_tomorrow_weather_n = day3json['HeWeather6'][0]['daily_forecast'][2]['cond_txt_n']
    # 风向
    tday_tomorrow_wind_dir = day3json['HeWeather6'][0]['daily_forecast'][2]['wind_dir']
    # 风力
    tday_tomorrow_wind_sc = day3json['HeWeather6'][0]['daily_forecast'][2]['wind_sc']
    # 最高温和最低温
    tday_tomorrow_tmp_max = day3json['HeWeather6'][0]['daily_forecast'][2]['tmp_max']
    tday_tomorrow_tmp_min = day3json['HeWeather6'][0]['daily_forecast'][2]['tmp_min']

    #预报信息汇总，今天，明天，后天
    today_weather_report = '今天 ' + '(' + today_date + ')' +  '，' + \
                           today_weather + '-' + tonight_weather + '，' + \
                           today_wind_dir + today_wind_sc + '级' + '，' + \
                           today_tmp_min +  '-' + today_tmp_max + '℃。\n'
    tomorrow_weather_report = '明天 ' + '(' + tomorrow_date + ')' +  '，' + \
                              tomorrow_weather + '-' + tomorrow_weather_n + '，' + \
                              tomorrow_wind_dir + tomorrow_wind_sc + '级' + '，' + \
                              tomorrow_tmp_min +  '-' + tomorrow_tmp_max + '℃。\n'
    tday_tomorrow_weather_report = '后天 ' + '(' + tday_tomorrow_date + ')' +  '，' + \
                                    tday_tomorrow_weather + '-' + tday_tomorrow_weather_n + '，' + \
                                    tday_tomorrow_wind_dir + tday_tomorrow_wind_sc + '级' + '，' + \
                                    tday_tomorrow_tmp_min +  '-' + tday_tomorrow_tmp_max + '℃。'
    
    # 打印天气预报信息
    
    #print('更新时间：' + update_time)  # 调试信息
    # 打印天气
    # print(location + today_weather_report + tomorrow_weather_report + tday_tomorrow_weather_report ) # 带地点打印信息
    print( today_weather_report + tomorrow_weather_report + tday_tomorrow_weather_report )
    
def realTimeWeatherForecast():
    # 实时天气信息
    realTimeUrl = "https://free-api.heweather.com/s6/weather/now?location=hefei&key=322389fe745246a88c9371a867475438"
    # 获取天气链接返回的网页字符串，转换成json对象
    realTimehtml = urllib.request.urlopen(realTimeUrl).read()
    realTimehtml = realTimehtml.decode('utf-8') 
    realTimejson = json.loads(realTimehtml)
    
    #定义天气预报的各个变量信息
    # 地点
    location = realTimejson['HeWeather6'][0]['basic']['location']
    # 更新时间
    update_time = realTimejson['HeWeather6'][0]['update']['loc']
    # Now weather
    now_weather = realTimejson['HeWeather6'][0]['now']['cond_txt']
    now_temp = realTimejson['HeWeather6'][0]['now']['tmp']
    now_wind_dir = realTimejson['HeWeather6'][0]['now']['wind_dir']
    now_wind_sc = realTimejson['HeWeather6'][0]['now']['wind_sc']
    
    print('更新时间：' + update_time + '\n' + location + '当前，' + now_weather + '，' + \
          now_temp + '℃，' + now_wind_dir + now_wind_sc + '级')
    
def airQlty():
    # 实时空气质量信息
    airQUrl = 'https://free-api.heweather.com/s6/air/now?location=hefei&key=322389fe745246a88c9371a867475438'
    airQhtml = urllib.request.urlopen(airQUrl).read()
    airQhtml = airQhtml.decode('utf-8') 
    airQjson = json.loads(airQhtml)
    air_qlty = airQjson['HeWeather6'][0]['air_now_city']['qlty']
    print('空气质量，' + air_qlty )
    
print('-'*30)    
realTimeWeatherForecast() # 调用实时预报
airQlty()
print('-'*50)
day3WeatherForecast() # 调用3日预报，并回显
print('-'*50)
