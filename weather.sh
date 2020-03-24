#!/bin/bash
key="heWeather-api-key"
location="hefei"
base_url_now="https://free-api.heweather.net/s6/weather/now?location=${location}&key=${key}"
base_url_air_now="https://free-api.heweather.net/s6/air/now?location=${location}&key=${key}"
base_url_forecast="https://free-api.heweather.net/s6/weather/forecast?location=${location}&key=${key}"
echo "获取当前天气数据..."

weatherNow=$(wget $base_url_now -q -O -)
airNow=$(wget $base_url_air_now -q -O -)
weatherForecast=$(wget $base_url_forecast -q -O -)
echo "完成"

# datas
# weather datas of now
update_time=`echo $weatherNow | jq -r '.HeWeather6[0].update.loc'`
now_location=`echo $weatherNow | jq -r '.HeWeather6[0].basic.location'`
now_cond_txt=`echo $weatherNow | jq -r '.HeWeather6[0].now.cond_txt'`
now_tmp=`echo $weatherNow | jq -r '.HeWeather6[0].now.tmp'`
now_wind_dir=`echo $weatherNow | jq -r '.HeWeather6[0].now.wind_dir'`
now_wind_sc=`echo $weatherNow | jq -r '.HeWeather6[0].now.wind_sc'`

# Air quality of now
air_now_qlty=`echo $airNow | jq -r '.HeWeather6[0].air_now_station[0].qlty'`

# weather of today
tod_date=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].date'`
tod_cond_d=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].cond_txt_d'`
tod_cond_n=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].cond_txt_n'`
tod_wind_dir=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].wind_dir'`
tod_wind_sc=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].wind_sc'`
tod_tmp_min=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].tmp_min'`
tod_tmp_max=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[0].tmp_max'`
# weather of tomorrow
tom_date=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].date'`
tom_cond_d=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].cond_txt_d'`
tom_cond_n=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].cond_txt_n'`
tom_wind_dir=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].wind_dir'`
tom_wind_sc=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].wind_sc'`
tom_tmp_min=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].tmp_min'`
tom_tmp_max=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[1].tmp_max'`
# weather of the dat after tomorrow
aft_tom_date=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].date'`
aft_tom_cond_d=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].cond_txt_d'`
aft_tom_cond_n=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].cond_txt_n'`
aft_tom_wind_dir=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].wind_dir'`
aft_tom_wind_sc=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].wind_sc'`
aft_tom_tmp_min=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].tmp_min'`
aft_tom_tmp_max=`echo $weatherForecast | jq -r '.HeWeather6[0].daily_forecast[2].tmp_max'`
# 3days data value
update_time_txt="更新时间：$update_time"
now_weather="${now_location}当前：${now_cond_txt}，${now_tmp}℃，${now_wind_dir}${now_wind_sc}级"
tod_weather="今天(${tod_date})，${tod_cond_d}-${tod_cond_n}，${tod_wind_dir}${tod_wind_sc}级，${tod_tmp_min}-${tod_tmp_max}℃。"
tom_weather="明天(${tom_date})，${tom_cond_d}-${tom_cond_n}，${tom_wind_dir}${tom_wind_sc}级，${tom_tmp_min}-${tom_tmp_max}℃。"
aft_tom_weather="后天(${aft_tom_date})，${aft_tom_cond_d}-${aft_tom_cond_n}，${aft_tom_wind_dir}${aft_tom_wind_sc}级，${aft_tom_tmp_min}-${aft_tom_tmp_max}℃。"

#txt_lenth=(${#update_time_txt} ${#now_weather} ${#tod_weather} ${#tom_weather} ${#aft_tom_weather})
#max_lenth=${txt_lenth[0]}
#for i in {1..4}
#do
#    if [ ${txt_lenth[$i]} > $max_lenth ]
#    then
#        max_lenth=${txt_lenth[$i]}
#    fi
#done

echo "$now_location天气预报："
echo "-----------------------------"
echo ${update_time_txt}
echo ${now_weather}
echo "空气质量：$air_now_qlty"
echo "-------------------------------------"
echo ${tod_weather}
echo ${tom_weather}
echo ${aft_tom_weather}
echo "-------------------------------------"
