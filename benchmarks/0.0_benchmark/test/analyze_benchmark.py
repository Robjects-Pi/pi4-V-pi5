#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def analyze_benchmark(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Set timestamp as index
    df.set_index('Timestamp', inplace=True)
    
    # Calculate statistics
    stats = df.describe()
    
    # Plot temperature over time
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['CPU Temperature (°C)'])
    plt.title('CPU Temperature Over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.savefig('temperature_over_time.png')
    plt.close()
    
    # Plot clock speed over time
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['CPU Clock Speed (MHz)'])
    plt.title('CPU Clock Speed Over Time')
    plt.xlabel('Time')
    plt.ylabel('Clock Speed (MHz)')
    plt.savefig('clock_speed_over_time.png')
    plt.close()
    
    # Create a heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.close()
    
    # Generate summary report
    with open('benchmark_summary.txt', 'w') as f:
        f.write("Benchmark #0 Analysis Summary\n")
        f.write("=============================\n\n")
        f.write(f"Total duration: {(df.index[-1] - df.index[0]).total_seconds()} seconds\n")
        f.write(f"Average CPU Temperature: {stats['CPU Temperature (°C)']['mean']:.2f}°C\n")
        f.write(f"Max CPU Temperature: {stats['CPU Temperature (°C)']['max']:.2f}°C\n")
        f.write(f"Average CPU Clock Speed: {stats['CPU Clock Speed (MHz)']['mean']:.2f} MHz\n")
        f.write(f"Max CPU Clock Speed: {stats['CPU Clock Speed (MHz)']['max']:.2f} MHz\n")
        f.write(f"\nDetailed Statistics:\n{stats}\n")
        
        # Analyze throttling
        throttled_count = df['CPU Throttled'].str.contains('throttled').sum()
        f.write(f"\nNumber of times CPU was throttled: {throttled_count}\n")
    
    print("Analysis complete. Results saved in benchmark_summary.txt and plot images.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_benchmark.py <path_to_benchmark_csv>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    analyze_benchmark(file_path)