#!/bin/bash

# Script to download and install dependencies for Benchmark #0

echo "Downloading and installing dependencies for Benchmark #0"

# Function to log messages with timestamps
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Update package lists
log_message "Updating package lists"
sudo apt-get update

# Install Sysbench
log_message "Installing Sysbench"
sudo apt-get install -y sysbench

# Install Stress-ng
log_message "Installing Stress-ng"
sudo apt-get install -y stress-ng

# Install iperf3 for network testing
log_message "Installing iperf3"
sudo apt-get install -y iperf3


# Install additional tools for system monitoring
log_message "Installing additional system monitoring tools"
sudo apt-get install -y htop iotop

# Install Python and required libraries for data analysis
log_message "Installing Python and required libraries"
sudo apt-get install -y python3 python3-pip
pip3 install matplotlib pandas

# Create the benchmark_tool.sh script
log_message "Creating benchmark_tool.sh script"
cat << 'EOF' > benchmark_tool.sh
#!/bin/bash

output_file="benchmark.csv"

case "$1" in
  idle)
    echo "Idle data for 60 seconds"
    duration=60
    ;;
  stress)
    echo "Stress data for 60 seconds"
    duration=60
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
EOF

chmod +x benchmark_tool.sh

log_message "All dependencies have been installed successfully"
log_message "Benchmark #0 is ready to run"