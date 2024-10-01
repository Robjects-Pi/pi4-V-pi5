#!/bin/bash

# iperf3 Installation Script for Raspberry Pi

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Update package lists
log_message "Updating package lists..."
sudo apt-get update

# Install iperf3
log_message "Installing iperf3..."
sudo apt-get install -y iperf3

# Verify installation
if command -v iperf3 &> /dev/null
then
    log_message "iperf3 installed successfully."
    IPERF3_VERSION=$(iperf3 --version | head -n1)
    log_message "Installed version: $IPERF3_VERSION"
else
    log_message "Error: iperf3 installation failed."
    exit 1
fi

# Create a directory for benchmark results
log_message "Creating directory for benchmark results..."
mkdir -p ~/network_benchmarks

# Create a simple iperf3 test script
log_message "Creating iperf3 test script..."
cat << 'EOF' > ~/network_benchmarks/run_iperf3_test.sh
#!/bin/bash

# Simple iperf3 test script

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Check if server address is provided
if [ $# -eq 0 ]; then
    log_message "Error: No iperf3 server address provided."
    echo "Usage: $0 <server_address>"
    exit 1
fi

SERVER_ADDRESS=$1
OUTPUT_FILE="iperf3_result_$(date '+%Y%m%d_%H%M%S').txt"

log_message "Starting iperf3 test to server: $SERVER_ADDRESS"
iperf3 -c $SERVER_ADDRESS -t 30 -J > ~/network_benchmarks/$OUTPUT_FILE

log_message "Test completed. Results saved to: ~/network_benchmarks/$OUTPUT_FILE"
EOF

chmod +x ~/network_benchmarks/run_iperf3_test.sh

log_message "Installation