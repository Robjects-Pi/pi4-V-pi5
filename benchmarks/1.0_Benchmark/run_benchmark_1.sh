#!/bin/bash

# Benchmark 1: Testing Networking Features and Scalability

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a benchmark_1_log.txt
}

# Create output directory
mkdir -p benchmark_1_results
cd benchmark_1_results

log_message "Starting Benchmark 1: Testing Networking Features and Scalability"

# 1. Network Performance Baseline
log_message "Running network performance baseline test"
iperf3 -c iperf.he.net -t 30 -J > network_baseline.json

# 2. Scalability Tests
run_scalability_test() {
    threads=$1
    log_message "Running scalability test with $threads threads"
    sysbench --test=cpu --cpu-max-prime=20000 --num-threads=$threads run > cpu_scalability_$threads.txt
    sysbench --test=memory --num-threads=$threads run > memory_scalability_$threads.txt
}

for threads in 1 2 4 8; do
    run_scalability_test $threads
done

# 3. Network Performance Under Load
log_message "Running network performance test under CPU load"
stress-ng --cpu 4 --timeout 30s &
iperf3 -c iperf.he.net -t 30 -J > network_under_load.json

# 4. Long Duration Network Test
log_message "Running long duration network test (5 minutes)"
iperf3 -c iperf.he.net -t 300 -i 10 -J > network_long_duration.json

# Generate summary report
log_message "Generating summary report"
echo "Benchmark 1 Summary" > summary_report.txt
echo "===================" >> summary_report.txt
echo "" >> summary_report.txt

echo "Network Baseline:" >> summary_report.txt
jq '.end.sum_sent.bits_per_second / 1000000' network_baseline.json | xargs printf "%.2f Mbps\n" >> summary_report.txt

echo "" >> summary_report.txt
echo "CPU Scalability:" >> summary_report.txt
for threads in 1 2 4 8; do
    events=$(grep "total number of events" cpu_scalability_$threads.txt | awk '{print $NF}')
    echo "$threads threads: $events events" >> summary_report.txt
done

echo "" >> summary_report.txt
echo "Memory Scalability:" >> summary_report.txt
for threads in 1 2 4 8; do
    ops=$(grep "transferred" memory_scalability_$threads.txt | awk '{print $1}')
    echo "$threads threads: $ops operations" >> summary_report.txt
done

echo "" >> summary_report.txt
echo "Network Under Load:" >> summary_report.txt
jq '.end.sum_sent.bits_per_second / 1000000' network_under_load.json | xargs printf "%.2f Mbps\n" >> summary_report.txt

echo "" >> summary_report.txt
echo "Long Duration Network Test:" >> summary_report.txt
jq '.end.sum_sent.bits_per_second / 1000000' network_long_duration.json | xargs printf "Average: %.2f Mbps\n" >> summary_report.txt

log_message "Benchmark 1 completed. Results saved in benchmark_1_results directory."