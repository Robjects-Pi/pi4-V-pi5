#!/bin/bash

output_file="benchmark_0.csv"

case "$1" in
  idle)
    echo "Idle data for 60 seconds"
    duration=60
    ;;
  stress)
    echo "Stress data for 300 seconds"
    duration=300
    ;;
  cooldown)
    echo "Cool down data for 60 seconds"
    duration=60
    ;;
  *)
    echo "Usage: $0 {idle|stress|cooldown}"
    exit 1
    ;;
esac

echo "Timestamp,CPU Temperature (°C),CPU Clock Speed (MHz),CPU Throttled" > "$output_file"

for i in $(seq 1 $duration); do
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  cpu_temp=$(vcgencmd measure_temp | cut -d= -f2 | cut -d\' -f1)
  cpu_clock_speed=$(($(vcgencmd measure_clock arm | awk -F= '{print $2}') / 1000000))
  throttled_status=$(vcgencmd get_throttled)
  echo "$timestamp,$cpu_temp,$cpu_clock_speed,$throttled_status" >> "$output_file"
  sleep 1
done

echo "Data collection complete. Results saved in $output_file"
