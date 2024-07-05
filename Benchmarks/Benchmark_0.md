# Benchmark #0: test of all metrics with noterminal output to a file

## Test Setup

### Control Variables

- Both Raspberry Pi 4 and Raspberry Pi 5 are brand new and have never been utilized.
- The software that's going to be incorporated is the exact same on both devices.
- Both devices are powered by their respective power supplies (3 A vs 5 A).
- Both devices are equipped with the standard Raspberry Pi fan with PWM control capabilities HOWEVER, we will conduct the 2 test without the fan with each microcontroller to see if the fan has any effect on the performance.
- Both devices are connected to the same network and and will utilize only the wireless connection for the tests.
- Both devices are connected to the will have no external devices connected to them during the tests besides power and the wireless connection (we will modify this in the next benchmarks).
- Both devices are running the latest version of Raspberry Pi OS (64-bit) with all updates installed. 
- Both devices are running the same version of the benchmarking software.
- Both devices will be in the same room with the same ambient temperature with the Rpi fan attached but turned off.
- Both rpis have metal enclosures for optimal heat dissapation. 
- And lastly, we




Note: I tried to keep the control variables as consistent as possible to ensure a fair comparison between the two devices, I definitely welcome any suggestions on how to improve the test setup, but I essentially wanted to keep the test as simple as possible to the average use cases.

<!-- TODO: Add a diagram of the test setup -->

### Metrics Captured