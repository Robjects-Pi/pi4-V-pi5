## Benchmark Overview

This document outlines the structure and results of four different benchmarks conducted to evaluate the performance of Raspberry Pi 4 and Raspberry Pi 5 under various conditions. Each benchmark aims to provide a comprehensive understanding of the system's capabilities and identify areas for improvement.

## Structure of Individual Benchmarks

Each benchmark markdown is divided into several key sections, each focusing on different aspects of the system's performance:

1. **Introduction**
   - Overview of the benchmark goals and objectives.
   - Description of the system configuration and setup used for the benchmark.

2. **Methodology**
   - Detailed explanation of the benchmarking process, including the tools and metrics used for evaluation.
   - Description of the test scenarios and workloads.

3. **Results**
   - Presentation of the benchmark results, including graphs and tables for easier comparison and analysis.
   - Analysis of the results, highlighting key findings and performance trends.

4. **Discussion**
   - Interpretation of the benchmark results, discussing the system's performance in the context of the test scenarios.
   - Identification of any bottlenecks or limitations observed during the benchmark.

5. **Conclusion and Recommendations**
   - Summary of the benchmark findings and their implications for the system's performance.
   - Recommendations for improving system performance based on the benchmark results.

## Benchmark Overview

This document outlines the structure and results of four different benchmarks conducted to evaluate the performance of Raspberry Pi 4 and Raspberry Pi 5 under various conditions. Each benchmark aims to provide a comprehensive understanding of the system's capabilities and identify areas for improvement.

## Structure of Individual Benchmarks

Each benchmark markdown is divided into several key sections, each focusing on different aspects of the system's performance:

1. **Introduction**
   - Overview of the benchmark goals and objectives.
   - Description of the system configuration and setup used for the benchmark.

2. **Methodology**
   - Detailed explanation of the benchmarking process, including the tools and metrics used for evaluation.
   - Description of the test scenarios and workloads.

3. **Results**
   - Presentation of the benchmark results, including graphs and tables for easier comparison and analysis.
   - Analysis of the results, highlighting key findings and performance trends.

4. **Discussion**
   - Interpretation of the benchmark results, discussing the system's performance in the context of the test scenarios.
   - Identification of any bottlenecks or limitations observed during the benchmark.

5. **Conclusion and Recommendations**
   - Summary of the benchmark findings and their implications for the system's performance.
   - Recommendations for improving system performance based on the benchmark results.

## Quick Instructions for Running Benchmarks

To ensure consistency across all benchmarks, we will use the same scripts for both terminal and file output. Below are the instructions for running each benchmark tool:

### Sysbench

**Installation:**

```bash
sudo apt-get install sysbench
```

**Single-Threaded CPU Test:**

```bash
sysbench --test=cpu --cpu-max-prime=20000 run | tee sysbench_single_thread.txt
```

**Multi-Threaded CPU Test:**

```bash
sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run | tee sysbench_multi_thread.txt
```

### Stress-ng

**Installation:**

```bash
sudo apt-get install stress-ng
```

**CPU Stress Test:**

```bash
stress-ng --cpu 4 --cpu-method matrixprod --timeout 300s | tee stress_ng_cpu.txt
```

### PassMark PerformanceTest

**Installation:**

Download the Linux version from the PassMark website and follow the installation instructions.

**Usage:**

```bash
./pt_linux_arm64 -r 3 | tee passmark_performance_test.txt
```

### Vcgencmd

**Installation:**

```bash
sudo apt-get install stress
```

**Benchmarking Script:**

Create a script named `benchmark.sh` with the following content:

```bash
#!/bin/bash

echo "Benchmark Tool"
output_file="benchmark.csv"
echo "Timestamp,CPU Temperature (°C),CPU Clock Speed (MHz),CPU Throttled" > "$output_file"

echo "Idle data for 60 seconds"
for i in {1..60}; do
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    cpu_temp=$(vcgencmd measure_temp | cut -d= -f2 | cut -d\' -f1)
    cpu_freq=$(vcgencmd measure_clock arm | cut -d= -f2)
    cpu_throttled=$(vcgencmd get_throttled | cut -d= -f2)
    echo "$timestamp,$cpu_temp,$cpu_freq,$cpu_throttled" >> "$output_file"
    sleep 1
done

stress --cpu 4 -t 300 &
echo "Stress data for 300 seconds"
for i in {1..300}; do
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    cpu_temp=$(vcgencmd measure_temp | cut -d= -f2 | cut -d\' -f1)
    cpu_freq=$(vcgencmd measure_clock arm | cut -d= -f2)
    cpu_throttled=$(vcgencmd get_throttled | cut -d= -f2)
    echo "$timestamp,$cpu_temp,$cpu_freq,$cpu_throttled" >> "$output_file"
    sleep 1
done
```

**Run the Script:**

```bash
chmod +x benchmark.sh
./benchmark.sh | tee vcgencmd_benchmark.txt
```

## Benchmark 1: Performance Under Load

### Introduction
- **Goals and Objectives**: Evaluate the system's performance under high load conditions to identify potential bottlenecks.
- **System Configuration**: Both Raspberry Pi 4 and Raspberry Pi 5 are brand new, running the latest version of Raspberry Pi OS (64-bit) with all updates installed. Both devices are powered by their respective power supplies (3 A vs 5 A) and equipped with standard Raspberry Pi fans, though tests will be conducted without the fans initially.

### Methodology
- **Process**: Tools used include Sysbench, Stress-ng, and PassMark PerformanceTest.
- **Test Scenarios**: Single-threaded and multi-threaded CPU tests, stress tests, and comprehensive performance tests using PassMark.

### Results
- **Data Presentation**: Include graphs and tables showing performance metrics from Sysbench and Stress-ng.
- **Analysis**: Highlight key findings such as performance differences between Raspberry Pi 4 and Raspberry Pi 5 under load.

### Discussion
- **Interpretation**: Discuss the system's behavior under load and any performance issues identified.
- **Bottlenecks**: Identify specific areas where performance degraded, such as thermal throttling or power supply limitations.

### Conclusion and Recommendations
- **Summary**: Recap the main findings of the benchmark.
- **Recommendations**: Suggest improvements such as better cooling solutions or power supply upgrades.

## Benchmark 2: Scalability

### Introduction
- **Goals and Objectives**: Assess the system's ability to scale with increasing workloads.
- **System Configuration**: Same as Benchmark 1, with additional focus on network performance using wireless connections.

### Methodology
- **Process**: Tools used include Sysbench and Stress-ng for scalability tests.
- **Test Scenarios**: Increasing number of threads and workloads to test scalability.

### Results
- **Data Presentation**: Include graphs and tables showing scalability metrics.
- **Analysis**: Highlight key findings such as how well the system scales with increased workloads.

### Discussion
- **Interpretation**: Discuss the system's scalability and any performance issues identified.
- **Bottlenecks**: Identify specific areas where scalability was limited, such as network bandwidth or CPU limitations.

### Conclusion and Recommendations
- **Summary**: Recap the main findings of the benchmark.
- **Recommendations**: Suggest improvements such as network upgrades or optimized software configurations.

## Benchmark 3: Resource Utilization

### Introduction
- **Goals and Objectives**: Measure the system's resource utilization under various conditions.
- **System Configuration**: Same as Benchmark 1, with additional monitoring of CPU temperature and clock speed.

### Methodology
- **Process**: Tools used include Sysbench, Stress-ng, and Vcgencmd for monitoring.
- **Test Scenarios**: Various workloads to measure CPU, memory, and I/O utilization.

### Results
- **Data Presentation**: Include graphs and tables showing resource utilization metrics.
- **Analysis**: Highlight key findings such as resource usage patterns and inefficiencies.

### Discussion
- **Interpretation**: Discuss the system's resource utilization and any inefficiencies identified.
- **Bottlenecks**: Identify specific areas where resource utilization was suboptimal, such as high CPU temperatures or memory bottlenecks.

### Conclusion and Recommendations
- **Summary**: Recap the main findings of the benchmark.
- **Recommendations**: Suggest optimizations such as better cooling solutions or memory management improvements.

## Benchmark 4: Reliability

### Introduction
- **Goals and Objectives**: Evaluate the system's reliability under prolonged use.
- **System Configuration**: Same as Benchmark 1, with extended testing periods.

### Methodology
- **Process**: Tools used include Stress-ng and monitoring scripts for reliability tests.
- **Test Scenarios**: Prolonged stress tests to evaluate system stability and reliability.

### Results
- **Data Presentation**: Include graphs and tables showing reliability metrics.
- **Analysis**: Highlight key findings such as system stability and any failures observed.

### Discussion
- **Interpretation**: Discuss the system's reliability and any issues identified.
- **Bottlenecks**: Identify specific areas where reliability was compromised, such as hardware failures or software crashes.

### Conclusion and Recommendations
- **Summary**: Recap the main findings of the benchmark.
- **Recommendations**: Suggest improvements such as hardware upgrades or software patches to enhance reliability.

## How to Access the Benchmark Results

The detailed results and analysis of each benchmark are available in the following sections of this document. Readers are encouraged to review each section to gain a comprehensive understanding of the system's performance characteristics.

## Acknowledgments

We would like to thank all the contributors and participants who made these benchmarks possible. Their dedication and hard work have provided valuable insights into the system's performance.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/1998337/9dd9d995-7f07-4981-a4d6-d1e7ba3dee1a/0.0_Benchmark.md
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/1998337/40cc0bc5-5ee7-4ecc-9797-299afe7d99aa/README.md
[3] https://forums.raspberrypi.com/viewtopic.php?start=100&t=44080
[4] https://community.element14.com/products/raspberry-pi/w/documents/4319/benchmarking-the-raspberry-pi-4-model-b
[5] https://forums.raspberrypi.com/viewtopic.php?t=158768
[6] https://www.raspberrypi.com/news/benchmarking-raspberry-pi-5/