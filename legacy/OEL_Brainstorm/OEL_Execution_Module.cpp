{
    "type": "NEW_FUNCTION",
    "name": "read_temp_5s_interval",
    "commands": [
        {"type": "SENSOR_READ", "sensor": "mcp9808"},
        {"type": "TIMER", "value": 5000}
    ],
}

#include "OTTER_Kernel.h"

class OTTER_Execution_Module {
public:
    void executeFunction(FunctionDef function) {
        for (auto command : function.commands) {
            if (command.type == "SENSOR_READ") {
                OTTER_Kernel.invoke(command.sensor, "SENSOR_READ");
            }
            else if (command.type == "SENSOR_RESOLUTION") {
                OTTER_Kernel.invoke(command.sensor, "SENSOR_RESOLUTION", command.value);
            }
            else if (command.type == "TIMER") {
                delay(command.value); // Wait for the specified time (in milliseconds)
            }
            else if (command.type == "EXIT") {
                return; // Exit the function execution
            }
        }
    }
};
