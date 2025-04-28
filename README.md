# OTTER - LLM for Embedded Systems

### OTTER Components Directory
- OTTER LLM in v2_LLM_OS/LLM/experiment.py
- OTTER LLM to OEL in v2_LLM_OS/LLM/Experiment_Helper_Code/convert_to_oel.py
- OTTER Engine in v2_LLM_OS/LLM/fyp_rtos.ino

### Data extraction files
- v2_LLM_OS/LLM/Experiment_Helper_Code/extract_i2c_data.py
- v2_LLM_OS/LLM/Experiment_Helper_Code/extract_latency.py
- v2_LLM_OS/LLM/Experiment_Helper_Code/extract_no_helpful_chunks.py

### The experiment results are combined in
- v2_LLM_OS/OTTER Experiment v2.xlsx



## Overview
OTTER is a lightweight middleware designed to streamline sensor interfacing in embedded systems using Large Language Models (LLMs). It simplifies I2C sensor communication by dynamically generating and executing sensor configurations, reducing development time and increasing flexibility.

## Features
- **LLM-Powered Sensor Configuration**: Converts natural language descriptions into optimized sensor configurations.
- **Dynamic I2C Communication**: Enables flexible interfacing with multiple sensors without hardcoded implementations.
- **OTTER Embedded Language (OEL)**: A proprietary language that enhances computational efficiency and enables real-time sensor data processing.
- **Kernel Process for Multi-Sensor Management**: Handles multiple I/O operations seamlessly, ensuring efficient data acquisition and processing.
- **Scalable and Modular**: Supports various embedded platforms including Arduino, ESP32, and Linux-based SBCs.
- **Proprietary Sensor Definition Language**: Defines data formats and scaling transformations for streamlined sensor integration.

## Workflow
1. **User Input**: Provide a natural language description of the sensor setup.
2. **LLM Processing**: The model interprets and translates the input into OEL.
3. **OEL Execution**: OTTER OS parses and executes OEL to configure sensors dynamically.
4. **Kernel Process Management**: Manages multi-sensor I2C communication efficiently.
5. **Data Retrieval & Processing**: Fetches, formats, and scales sensor data based on predefined rules.

## Supported Hardware
- **Microcontrollers**: Arduino Nano 33 BLE Sense Lite.
- **Sensors**:
  - Temperature Sensors: MCP9808, TMP102
  - Temperature & Humidity Sensors: AHT20, SHT31
  - Altitude/Pressure Sensors: MPL3115A2, GY-BMP280
  - Time of Flight Sensor: IRS11A 0J9776
  
## Installation
1. Clone the OTTER repository:
   ```sh
   git clone https://github.com/stevenantya/LLM-OS-OTTER.git
   ```
2. Install dependencies:
   - **Arduino IDE / PlatformIO** for microcontroller development.
   - **Python 3+** for LLM processing and serial communication.
3. Upload the firmware to the microcontroller and run the OTTER runtime on the edge device.

## Usage
1. Connect the microcontroller to the sensors and upload OTTER firmware.
2. Run the OTTER runtime on an edge device.
3. Send sensor descriptions in natural language via serial communication.
4. Retrieve and process sensor data dynamically.

## Example
### User Input:
```plaintext
Read humidity and temperature from AHT20 i2c sensor. Output it in humidity % and celcius.
```
### OEL Output:
```plaintext
NEW_SENSOR = AHT20;
PROTOCOL = I2C;
SENSOR_ADDR = 0x38;
INIT_CMD = (0xBE, 0x08, 0x00);
NEW_SENSOR_READ;
READ_CMD = (0xAC, 0x33, 0x00);
DATA_LEN = 6;
DATA_KEY_VAL = (0: "HUM", 1: "TEMP");
DATA_FORMAT = (0: [12:31], 1: [28:47]);
SCALE_FORMAT = (0: "x 100.0 * 1048576.0 / 50.0 - 50.0 +", 1: "x 200.0 * 1048576.0 / 50 -");
```
### OTTER Engine Output:
```plaintext
Running Sensor Thread AHT20
Hum = 50.54%
Temp = 26.62°C
```

## Future Developments
- **Enhanced LLM Processing**: Improve parsing and inference for more complex sensor configurations.
- **Expanded Hardware Support**: Integration with more microcontrollers and communication protocols.
- **Cloud Connectivity**: Enable remote monitoring and data logging.

## Contributors
- [**Steven Waskito**](https://swaskito.com) - Lead Developer
- [**Prof. Ambuj Varshney**](https://ambuj.se) - Principal Investigator

## License
[Apache 2.0]

## Contact
For inquiries, please reach out to **steven@comp.nus.edu.sg** or visit our GitHub repository.

---

OTTER is designed to revolutionize embedded sensor interfacing, making integration seamless and efficient through AI-driven automation.
