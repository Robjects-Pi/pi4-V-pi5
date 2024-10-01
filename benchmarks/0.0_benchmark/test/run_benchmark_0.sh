#!/bin/bash

: '
This script runs a comprehensive performance evaluation of the Raspberry Pi
It includes the following tests:
1. System Information
2. Idle State Measurement
3. CPU Performance Test
4. Memory Performance Test
5. Storage I/O Test
6. Stress Test
7. Cool Down Period
8. Network Performance Test
'
# Usage: ./run_test.sh



# Benchmark #0: Comprehensive Performance Evaluation of Raspberry Pi

# Print the start message
echo "Starting Benchmark #0: Comprehensive Performance Evaluation"

# Check dependencies
if ! command -v sysbench &> /dev/null; then
    echo "sysbench is not installed. Please run install_benchmark_dependencies.sh first."
    exit 1
fi


if ! command -v stress-ng &> /dev/null; then
    echo "stress-ng is not installed. Please run install_benchmark_dependencies.sh first."
    exit 1
fi

if ! command -v iperf3 &> /dev/null; then
    echo "iperf3 is not installed. Please run install_benchmark_dependencies.sh first."
    exit 1
fi



# Create output directory
mkdir -p benchmark_results
cd benchmark_results

# Copy the benchmark tool script
cp ../benchmark_tool.sh .

# Copy the analysis script
cp ../analyze_benchmark.py .

# Function to log messages with timestamps
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a benchmark_log.txt
}

# 1. System Information
log_message "Collecting System Information"
uname -a > system_info.txt
cat /proc/cpuinfo >> system_info.txt
cat /proc/meminfo >> system_info.txt
vcgencmd get_config int >> system_info.txt

# 2. Idle State Measurement (60 seconds)
log_message "Starting Idle State Measurement"
./benchmark_tool.sh idle

# 3. CPU Performance Test
log_message "Starting CPU Performance Tests"

# Sysbench CPU Test (Single-threaded)
log_message "Running Sysbench Single-threaded CPU Test"
sysbench --test=cpu --cpu-max-prime=20000 run > sysbench_single_thread.txt

# Sysbench CPU Test (Multi-threaded)
log_message "Running Sysbench Multi-threaded CPU Test"
sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run > sysbench_multi_thread.txt

# 4. Memory Performance Test
log_message "Starting Memory Performance Tests"

# Sysbench Memory Test
log_message "Running Sysbench Memory Test"
sysbench --test=memory run > sysbench_memory.txt

# 5. Storage I/O Test
log_message "Starting Storage I/O Test"
./benchmark_tool.sh storage

# 6. Stress Test (300 seconds)
log_message "Starting Stress Test"
stress-ng --cpu 4 --cpu-method matrixprod --timeout 300s > stress_ng_output.txt &
./benchmark_tool.sh stress

# 7. Cool Down Period (60 seconds)
log_message "Starting Cool Down Period"
./benchmark_tool.sh cooldown

# Generate summary report
log_message "Generating Summary Report"
echo "Benchmark #0 Summary" > summary_report.txt
echo "=====================" >> summary_report.txt
echo "" >> summary_report.txt
echo "CPU Performance:" >> summary_report.txt
grep "total time:" sysbench_single_thread.txt >> summary_report.txt
grep "total time:" sysbench_multi_thread.txt >> summary_report.txt
echo "" >> summary_report.txt
echo "Memory Performance:" >> summary_report.txt
grep "transferred" sysbench_memory.txt >> summary_report.txt
echo "" >> summary_report.txt
echo "Maximum Temperature:" >> summary_report.txt
vcgencmd measure_temp >> summary_report.txt

log_message "Benchmark #0 Completed"

log_message "Creating detailed analysis report"
python3 analyze_benchmark.py sysbench_single_thread.txt sysbench_multi_thread.txt sysbench_memory.txt summary_report.txt