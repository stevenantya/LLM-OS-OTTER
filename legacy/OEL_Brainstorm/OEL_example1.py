'''
// OEL Syntax Documentation

// 1. Sensor Definition
NEW_SENSOR <name>
PROTOCOL <protocol>
ADDR <address>
REGISTER <reg_addr>
SCALE <scale_factor>
METHODS {
    SENSOR_READ {
        POST_PROCESS {
            operation1,
            operation2,
            ...,
        },
    },
}
END_SENSOR

// 2. Methods
METHODS
  <method_name> [PARAMS]
  ...
END_METHODS

// 3. Function Definition
NEW_FUNCTION <name>
BODY {
    SENSOR_READ <sensor_name>,
    TIMER 5000,
}

// 4. Comments
// Single-line comment
/* Multi-line comment */

// 5. Example
NEW_SENSOR <name>;
PROTOCOL <protocol>;
ADDR <address>;
REGISTER <reg_addr>;
DATA_SIZE <data_size_in_bytes>;
SCALE <scale_factor>;
RESOLUTION <resolution_in_bits>;
POST_PROCESS: <operation>;
END_SENSOR;

v1
NEW_SENSOR MCP9808_Temp_Sensor;
PROTOCOL I2C;
ADDR 0x18;
REGISTER 0x05;
DATA_SIZE 2;
SCALE 0.0625;
RESOLUTION 12;
POST_PROCESS: |16;
END_SENSOR;

NEW_SENSOR AHT120_Temp_Humid_Sensor;
PROTOCOL I2C;
ADDR 0x18;
REGISTER 0x05;
SCALE 0.0625;
RESOLUTION 12;
POST_PROCESS: |16;
END_SENSOR;

NEW_SENSOR SHT31_Temp_Humid_Sensor;
PROTOCOL I2C;
ADDR 0x18;
REGISTER 0x05;
SCALE 0.0625;
POST_PROCESS: |16;
END_SENSOR;

NEW_SENSOR MPL3115A2_Altimeter;
PROTOCOL I2C;
ADDR 0x18;
REGISTER 0x05;
SCALE 0.0625;
POST_PROCESS: |16;
END_SENSOR;

v2
NEW_SENSOR MCP9808_Temp_Sensor;
PROTOCOL I2C;
ADDR 0x18;
REGISTER 0x05;
SCALE 0.0625;
METHODS {
    SENSOR_READ {
        POST_PROCESS {
            convert_to_celsius,
            apply_calibration_offset,
        },
    },
};
END_SENSOR;


START_NEW_SENSOR
PROTOCOL I2C 
NAME 'mcp9808'
I2C_ADDR 0x21
REG_ADDR 0x10
SCALE 0.0625
LIST_POST_PROCESS
  RAW 16 >>
  SCALE *
END_LIST_POST_PROCESS
LIST_METHODS //these are the methods that is //constructed in the creation of the obj.
  SENSOR_READ
  SENSOR_RESOLUTION
END_LIST_METHODS
END_NEW_SENSOR

START_NEW_FUNCTION
NAME 'read_temp_5s_interval'
PARAMS
  SENSOR_NAME 'mcp9808'
BODY
  SENSOR_READ
  TIMER 5000
END_NEW_FUNCTION

START_NEW_FUNCTION
NAME 'set_res_1'
PARAMS
  SENSOR_NAME 'mcp9808'
BODY
  SENSOR_RESOLUTION 1
  EXIT //directly destructed
END_NEW_FUNCTION
'''
import time

class Sensor:
    def __init__(self, name, protocol, i2c_addr, reg_addr, scale):
        self.name = name
        self.protocol = protocol
        self.i2c_addr = i2c_addr
        self.reg_addr = reg_addr
        self.scale = scale
        self.methods = {}

    def add_method(self, method_name, func):
        self.methods[method_name] = func

    def execute_method(self, method_name):
        if method_name in self.methods:
            return self.methods[method_name]()
        else:
            print(f"Error: Method {method_name} not found for sensor {self.name}")

class OELInterpreter:
    def __init__(self):
        self.sensors = {}

    def execute(self, oel_code):
        lines = oel_code.strip().split("\n")
        current_sensor = None
        in_function = False
        function_name = None
        function_body = []

        for line in lines:
            line = line.strip()

            if line == "START":
                continue
            elif line.startswith("NEW_SENSOR"):
                current_sensor = {}
            elif line.startswith("NAME"):
                sensor_name = line.split("'")[1]
                current_sensor["name"] = sensor_name
            elif line.startswith("PROTOCOL"):
                current_sensor["protocol"] = line.split()[1]
            elif line.startswith("I2C_ADDR"):
                current_sensor["i2c_addr"] = int(line.split()[1], 16)
            elif line.startswith("REG_ADDR"):
                current_sensor["reg_addr"] = int(line.split()[1], 16)
            elif line.startswith("SCALE"):
                current_sensor["scale"] = float(line.split()[1])
            elif line.startswith("METHODS"):
                pass  # Methods will be handled later
            elif line == "END":
                if current_sensor:
                    sensor = Sensor(**current_sensor)
                    self.sensors[sensor.name] = sensor
                    current_sensor = None
                elif in_function:
                    self.add_function(function_name, function_body)
                    in_function = False
            elif line.startswith("NEW_FUNCTION"):
                in_function = True
                function_body = []
            elif in_function:
                function_body.append(line)

    def add_function(self, name, body):
        def func():
            for command in body:
                if "SENSOR_READ" in command:
                    print(f"Reading from sensor: {command.split()[1]}")
                elif "TIMER" in command:
                    delay = int(command.split()[1])
                    print(f"Waiting for {delay}ms")
                    time.sleep(delay / 1000)
                elif "EXIT" in command:
                    print("Function exited")
                    return
        self.sensors[name] = func

# Example OEL Code
oel_code = """
START
NEW_SENSOR
PROTOCOL I2C
NAME 'mcp9808'
I2C_ADDR 0x21
REG_ADDR 0x10
SCALE 0.0625
END

START
NEW_FUNCTION
NAME 'read_temp_5s_interval'
BODY
  SENSOR_READ 'mcp9808'
  TIMER 5000
END
"""

interpreter = OELInterpreter()
interpreter.execute(oel_code)
