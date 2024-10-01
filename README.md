# Raspberry Pi Benchmarking Suite

This repository contains tools and instructions for benchmarking the performance of your Raspberry Pi. Whether you are using a Raspberry Pi 4 or the latest Raspberry Pi 5, this guide will help you get started with configuring your device and running comprehensive benchmark tests.

## Introduction

Welcome to the Raspberry Pi Benchmarking Suite! This repository contains tools and instructions for benchmarking the performance of your Raspberry Pi. Whether you are using a Raspberry Pi 4 or the latest Raspberry Pi 5, this guide will help you get started with configuring your device and running comprehensive benchmark tests.

## Table of Contents

- [Raspberry Pi Benchmarking Suite](#raspberry-pi-benchmarking-suite)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Repository Organization](#repository-organization)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Configuring Raspberry Pi Connect](#configuring-raspberry-pi-connect)
- [Running Benchmark Tests](#running-benchmark-tests)

## Repository Organization

The repository is organized into two main directories:

### benchmarks

This directory contains the benchmark scripts and tools used to test various aspects of Raspberry Pi performance. The benchmarks include:

- **CPU Performance**: Tests for single-core and multi-core performance
- **Memory Speed**: Evaluates RAM read/write speeds
- **Storage I/O**: Measures disk read/write performance
- **Network Speed**: Tests network throughput and latency
- **GPU Performance**: Assesses graphics processing capabilities

### results

This directory stores the benchmark results for different Raspberry Pi models. It includes:

- **Pi4_results**: Benchmark outcomes for Raspberry Pi 4 models
- **Pi5_results**: Benchmark outcomes for Raspberry Pi 5 models
- **Comparison**: Comparative analysis between Pi 4 and Pi 5 performance

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- A Raspberry Pi 4 or Raspberry Pi 5
- A 64-bit distribution of Raspberry Pi OS Bookworm
- An active internet connection

### Configuring Raspberry Pi Connect

Raspberry Pi Connect provides secure access to your Raspberry Pi from anywhere in the world. Follow these steps to configure it:

1. **Update Your System**

```bash
sudo apt update && sudo apt full-upgrade -y
```

2. **Install Raspberry Pi Connect**

```bash
sudo apt install rpi-connect
```

3. **Reboot Your Raspberry Pi**

```bash
sudo reboot
```

4. **Link Your Raspberry Pi to Your Raspberry Pi ID**

- **Via the Raspberry Pi Desktop**:
  - Click on the Connect icon in the system tray and choose "Sign in".
  - Follow the instructions to generate a verification URL and link your device.

- **Via the Command Line**:
  - Run the following command:
    ```bash
    rpi-connect signin
    ```
  - Visit the generated URL to complete the linking process.

5. **Verify Connection**
   - Once linked, the Connect system tray icon will turn blue.
   - You should receive an email notification indicating that a new device has signed into Connect.
   - For more information, refer to the Raspberry Pi Connect documentation.

> **Note:** Content in section 'Configuring Raspberry Pi Connect' above adapted from Raspberry Pi Connect documentation created by Raspberry Pi Ltd and licensed under a [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

## Running Benchmark Tests

To run the benchmark tests on your Raspberry Pi:

1. Clone this repository:
   ```bash
   git clone https://github.com/Robjects-Pi/pi4-V-pi5.git
   ```

2. Navigate to the benchmarks directory:
   ```bash
   cd pi4-V-pi5/benchmarks
   ```

3. Go to the benchmark directory you want to test:
   ```bash
   cd 1.0_Benchmark
   ```
4. Change the permissions of the benchmark install and run script to make it executable and
   ```bash
   chmod +x install_benchmark_X_dependencies.sh run_benchmark_X.sh 
   ``` 
5. Run the benchmark install script:
   ```bash
   ./install_benchmark_X_dependencies.sh

   ```
6. Run the benchmark script:
   ```bash
   ./run_benchmark_X.sh
   ```
7. The results will be saved in the `benchmark_results` directory, organized by your Raspberry Pi model. Look for a detailed summary of the benchmark outcomes in the `results` directory.

> **Note:**
> - The benchmarking process may take some time to complete, depending on the test scenarios and workloads.
> - Make sure the installation and benchmark scripts are executed with the appropriate permissions, and no errors occur during the process.
> - For more detailed instructions on the benchmark tests, refer to the benchmark's `README.md` file in the respective benchmark directory.



