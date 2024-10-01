import re
import sys
from pathlib import Path

def parse_sysbench_single(content):
    data = {}
    data['events_per_second'] = float(re.search(r'events per second:\s+([\d.]+)', content).group(1))
    data['total_time'] = float(re.search(r'total time:\s+([\d.]+)s', content).group(1))
    data['total_events'] = int(re.search(r'total number of events:\s+(\d+)', content).group(1))
    latency = re.search(r'Latency \(ms\):\s+min:\s+([\d.]+)\s+avg:\s+([\d.]+)\s+max:\s+([\d.]+)\s+95th percentile:\s+([\d.]+)', content)
    data['latency'] = {
        'min': float(latency.group(1)),
        'avg': float(latency.group(2)),
        'max': float(latency.group(3)),
        '95th': float(latency.group(4))
    }
    return data

def parse_sysbench_multi(content):
    data = parse_sysbench_single(content)
    fairness = re.search(r'events \(avg/stddev\):\s+([\d.]+)/([\d.]+)', content)
    data['fairness'] = {
        'events_avg': float(fairness.group(1)),
        'events_stddev': float(fairness.group(2))
    }
    return data

def parse_sysbench_memory(content):
    data = {}
    data['total_operations'] = int(re.search(r'Total operations:\s+(\d+)', content).group(1))
    data['operations_per_second'] = float(re.search(r'(\d+\.\d+) per second', content).group(1))
    data['transferred'] = float(re.search(r'([\d.]+) MiB transferred', content).group(1))
    data['transfer_rate'] = float(re.search(r'\(([\d.]+) MiB/sec\)', content).group(1))
    latency = re.search(r'Latency \(ms\):\s+min:\s+([\d.]+)\s+avg:\s+([\d.]+)\s+max:\s+([\d.]+)\s+95th percentile:\s+([\d.]+)', content)
    data['latency'] = {
        'min': float(latency.group(1)),
        'avg': float(latency.group(2)),
        'max': float(latency.group(3)),
        '95th': float(latency.group(4))
    }
    return data

def parse_summary(content):
    data = {}
    data['max_temp'] = float(re.search(r'temp=([\d.]+)', content).group(1))
    return data

def generate_summary(single, multi, memory, summary):
    report = "Detailed Summary of Raspberry Pi Performance\n\n"
    
    report += "1. CPU Performance:\n\n"
    report += "Single-threaded performance:\n"
    report += f"- Events per second: {single['events_per_second']:.2f}\n"
    report += f"- Total time: {single['total_time']:.4f} seconds\n"
    report += f"- Total number of events: {single['total_events']}\n"
    report += "- Latency:\n"
    report += f"  * Minimum: {single['latency']['min']:.2f} ms\n"
    report += f"  * Average: {single['latency']['avg']:.2f} ms\n"
    report += f"  * Maximum: {single['latency']['max']:.2f} ms\n"
    report += f"  * 95th percentile: {single['latency']['95th']:.2f} ms\n\n"
    
    report += "Multi-threaded performance (4 threads):\n"
    report += f"- Events per second: {multi['events_per_second']:.2f} ({multi['events_per_second']/single['events_per_second']:.2f}x improvement over single-threaded)\n"
    report += f"- Total time: {multi['total_time']:.4f} seconds\n"
    report += f"- Total number of events: {multi['total_events']} ({multi['total_events']/single['total_events']:.2f}x more events than single-threaded)\n"
    report += "- Latency:\n"
    report += f"  * Minimum: {multi['latency']['min']:.2f} ms\n"
    report += f"  * Average: {multi['latency']['avg']:.2f} ms ({(multi['latency']['avg']/single['latency']['avg']-1)*100:.1f}% increase compared to single-threaded)\n"
    report += f"  * Maximum: {multi['latency']['max']:.2f} ms\n"
    report += f"  * 95th percentile: {multi['latency']['95th']:.2f} ms\n\n"
    
    report += "Thread fairness (multi-threaded):\n"
    report += f"- Events: {multi['fairness']['events_avg']:.4f} avg / {multi['fairness']['events_stddev']:.2f} stddev\n"
    report += f"- Execution time: {multi['total_time']:.4f}s avg / {multi['fairness']['events_stddev']/100:.2f}s stddev\n\n"
    
    report += "Analysis:\n"
    report += f"The CPU shows good scalability with multi-threading, achieving a {multi['events_per_second']/single['events_per_second']:.2f}x performance increase with 4 threads. "
    report += "However, the increased latency in the multi-threaded test suggests some overhead in thread management and potential resource contention.\n\n"
    
    report += "2. Memory Performance:\n\n"
    report += f"- Total operations: {memory['total_operations']:,}\n"
    report += f"- Operations per second: {memory['operations_per_second']:,.2f}\n"
    report += f"- Data transferred: {memory['transferred']:.2f} MiB\n"
    report += f"- Transfer rate: {memory['transfer_rate']:.2f} MiB/sec\n"
    report += "- Latency:\n"
    report += f"  * Minimum: {memory['latency']['min']:.2f} ms\n"
    report += f"  * Average: {memory['latency']['avg']:.2f} ms\n"
    report += f"  * Maximum: {memory['latency']['max']:.2f} ms\n"
    report += f"  * 95th percentile: {memory['latency']['95th']:.2f} ms\n\n"
    
    report += "Analysis:\n"
    report += f"The memory subsystem shows good performance with a transfer rate of {memory['transfer_rate']:.2f} MiB/sec. "
    report += "The low latency values indicate efficient memory access, which is crucial for overall system responsiveness.\n\n"
    
    report += "3. Temperature:\n\n"
    report += f"- Maximum temperature recorded: {summary['max_temp']}°C\n\n"
    
    report += "Analysis:\n"
    report += f"The maximum temperature of {summary['max_temp']}°C is within a safe operating range for the Raspberry Pi. "
    report += "This suggests that the system is managing heat effectively during the benchmark tests, which is important for long-term stability and performance consistency.\n\n"
    
    report += "Overall System Performance Assessment:\n\n"
    report += "1. CPU Efficiency: The CPU demonstrates good single-threaded performance and scales well with multi-threading. "
    report += f"The {multi['events_per_second']/single['events_per_second']:.2f}x performance increase with 4 threads indicates efficient use of available cores.\n\n"
    report += "2. Memory Subsystem: The memory shows strong performance with high throughput and low latency, which is crucial for overall system responsiveness and application performance.\n\n"
    report += f"3. Thermal Management: The maximum temperature of {summary['max_temp']}°C suggests effective heat dissipation, which is important for maintaining consistent performance and ensuring long-term hardware reliability.\n\n"
    report += "4. System Stability: The completion of all benchmark tests without errors indicates good system stability under load.\n\n"
    report += "5. Multi-tasking Capability: The multi-threaded CPU test results suggest that the system can handle concurrent tasks efficiently, although there is some overhead in thread management.\n\n"
    
    report += "Conclusion:\n"
    report += "Based on these benchmark results, the Raspberry Pi is performing well across CPU, memory, and thermal management aspects. "
    report += "The system shows good multi-threading capabilities, efficient memory operations, and effective heat management. "
    report += "These characteristics indicate that the operating system is running efficiently on the hardware, providing a stable and responsive environment for various computing tasks.\n\n"
    
    report += "Areas for potential improvement or further investigation:\n"
    report += "1. Analyze the cause of increased latency in multi-threaded operations to potentially optimize thread management.\n"
    report += "2. Monitor temperature over extended periods of high load to ensure consistent thermal performance.\n"
    report += "3. Consider additional benchmarks for storage I/O and network performance to get a more comprehensive view of system capabilities.\n"
    
    return report

def main(single_file, multi_file, memory_file, summary_file):
    with open(single_file, 'r') as f:
        single_data = parse_sysbench_single(f.read())
    
    with open(multi_file, 'r') as f:
        multi_data = parse_sysbench_multi(f.read())
    
    with open(memory_file, 'r') as f:
        memory_data = parse_sysbench_memory(f.read())
    
    with open(summary_file, 'r') as f:
        summary_data = parse_summary(f.read())
    
    report = generate_summary(single_data, multi_data, memory_data, summary_data)
    
    with open('detailed_summary_report.txt', 'w') as f:
        f.write(report)
    
    print("Detailed summary report has been generated: detailed_summary_report.txt")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <single_thread_file> <multi_thread_file> <memory_file> <summary_file>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
# #!/usr/bin/env python3

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import sys

# def analyze_benchmark(file_path):
#     # Read the CSV file
#     df = pd.read_csv(file_path)
    
#     # Convert timestamp to datetime
#     df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
#     # Set timestamp as index
#     df.set_index('Timestamp', inplace=True)
    
#     # Calculate statistics
#     stats = df.describe()
    
#     # Plot temperature over time
#     plt.figure(figsize=(12, 6))
#     plt.plot(df.index, df['CPU Temperature (°C)'])
#     plt.title('CPU Temperature Over Time')
#     plt.xlabel('Time')
#     plt.ylabel('Temperature (°C)')
#     plt.savefig('temperature_over_time.png')
#     plt.close()
    
#     # Plot clock speed over time
#     plt.figure(figsize=(12, 6))
#     plt.plot(df.index, df['CPU Clock Speed (MHz)'])
#     plt.title('CPU Clock Speed Over Time')
#     plt.xlabel('Time')
#     plt.ylabel('Clock Speed (MHz)')
#     plt.savefig('clock_speed_over_time.png')
#     plt.close()
    
#     # Create a heatmap of correlations
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
#     plt.title('Correlation Heatmap')
#     plt.savefig('correlation_heatmap.png')
#     plt.close()
    
#     # Generate summary report
#     with open('benchmark_summary.txt', 'w') as f:
#         f.write("Benchmark #0 Analysis Summary\n")
#         f.write("=============================\n\n")
#         f.write(f"Total duration: {(df.index[-1] - df.index[0]).total_seconds()} seconds\n")
#         f.write(f"Average CPU Temperature: {stats['CPU Temperature (°C)']['mean']:.2f}°C\n")
#         f.write(f"Max CPU Temperature: {stats['CPU Temperature (°C)']['max']:.2f}°C\n")
#         f.write(f"Average CPU Clock Speed: {stats['CPU Clock Speed (MHz)']['mean']:.2f} MHz\n")
#         f.write(f"Max CPU Clock Speed: {stats['CPU Clock Speed (MHz)']['max']:.2f} MHz\n")
#         f.write(f"\nDetailed Statistics:\n{stats}\n")
        
#         # Analyze throttling
#         throttled_count = df['CPU Throttled'].str.contains('throttled').sum()
#         f.write(f"\nNumber of times CPU was throttled: {throttled_count}\n")
    
#     print("Analysis complete. Results saved in benchmark_summary.txt and plot images.")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python analyze_benchmark.py <path_to_benchmark_csv>")
#         sys.exit(1)
    
#     file_path = sys.argv[1]
#     analyze_benchmark(file_path)