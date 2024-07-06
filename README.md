
# Raspberry Pi Benchmarking Suite

## Introduction

Welcome to the Raspberry Pi Benchmarking Suite! This repository contains tools and instructions for benchmarking the performance of your Raspberry Pi. Whether you are using a Raspberry Pi 4 or the latest Raspberry Pi 5, this guide will help you get started with configuring your device and running comprehensive benchmark tests.

## Table of Contents

- [Raspberry Pi Benchmarking Suite](#raspberry-pi-benchmarking-suite)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Configuring Raspberry Pi Connect](#configuring-raspberry-pi-connect)
  - [Benchmark Tests](#benchmark-tests)
    - [CPU Benchmarks](#cpu-benchmarks)
    - [Memory Benchmarks](#memory-benchmarks)
    - [Storage Benchmarks](#storage-benchmarks)
    - [Network Benchmarks](#network-benchmarks)
    - [GPU Benchmarks](#gpu-benchmarks)
  - [Benchmark Results](#benchmark-results)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- A Raspberry Pi 4 or Raspberry Pi 5
- A 64-bit distribution of Raspberry Pi OS Bookworm
- An active internet connection
- SSH enabled on your Raspberry Pi

### Configuring Raspberry Pi Connect

Raspberry Pi Connect provides secure access to your Raspberry Pi from anywhere in the world. Follow these steps to configure it:

1. **Update Your System**
---
```bash
   sudo apt update && sudo apt upgrade -y
```
---

2. **Install Raspberry Pi Connect**
---
```bash
   sudo apt install rpi-connect
```
---

3. **Reboot Your Raspberry Pi**
---
```bash
   sudo reboot
```
---

4. **Link Your Raspberry Pi to Your Raspberry Pi ID**

   - **Via the Raspberry Pi Desktop**:
     - Click on the Connect icon in the system tray and choose "Sign in".
     - Follow the instructions to generate a verification URL and link your device.

   - **Via the Command Line**:
---    
```bash
     rpi-connect signin
    ```
---
     - Visit the generated URL to complete the linking process.

5. **Verify Connection**
   - Once linked, the Connect system tray icon will turn blue.
   - You should receive an email notification indicating that a new device has signed into Connect.

For more detailed instructions, refer to the [Raspberry Pi Connect Documentation](https://www.raspberrypi.com/documentation/services/connect.html)[1].

## Benchmark Tests

Navigate to the `benchmarks` folder for detailed instructions and scripts for running the following benchmarks:

### CPU Benchmarks

- **Sysbench**: Measures CPU performance using prime number calculations.
---
```bash
  sysbench --test=cpu --cpu-max-prime=20000 run
```
---

- **Stress-ng**: Stress tests the CPU with various methods.
---
```bash
  stress-ng --cpu 4 --cpu-method matrixprod --timeout 300s
```
---

### Memory Benchmarks

- **RAMspeed**: Measures cache and memory performance.
---
```bash
  ramspeed -b 1M -m 1G
```
---

### Storage Benchmarks

- **HDParm**: Tests read speed of storage devices.
---
```bash
  sudo hdparm -Tt /dev/mmcblk0
```
---

- **Iozone**: Tests file system performance.
---
```bash
  sudo iozone -a -g 512M
```
---

### Network Benchmarks

- **Speedtest CLI**: Measures internet speed.
---
```bash
  speedtest-cli
```
---

### GPU Benchmarks

- **glmark2**: Tests GPU performance.
---
```bash
  glmark2
```
---

## Benchmark Results

Detailed benchmark results for Raspberry Pi 4 and Raspberry Pi 5 can be found in the `results` folder.Here, you will find the results of running the above benchmarks on both Raspberry Pi models and the corresponding performance metrics. 

 These results include comparisons across various benchmarks to highlight the performance improvements and differences between the two models.

For more information, refer to the [Raspberry Pi Benchmark Results](./results/README.md).

[1]: https://www.raspberrypi.com/documentation/services/connect.html


This README provides a comprehensive guide to getting started with benchmarking on Raspberry Pi, including configuration steps for Raspberry Pi Connect and detailed benchmark instructions and results.

