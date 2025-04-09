#include <Arduino.h>
#include <queue>
#include <mutex>

class OTTER_Scheduler {
public:
    std::queue<I2CTask> taskQueue;  
    std::mutex i2cMutex;  

    void addTask(String sensorName, String operation, float value = 0) {
        I2CTask newTask = {sensorName, operation, value};
        taskQueue.push(newTask);
    }

    void executeTasks() {
        while (!taskQueue.empty()) {
            // Lock I2C bus for the current task
            std::lock_guard<std::mutex> lock(i2cMutex); 

            I2CTask currentTask = taskQueue.front();  
            taskQueue.pop();  

            // Process the task
            if (currentTask.operation == "SENSOR_READ") {
                
                performSensorRead(currentTask.sensorName);
            } 
            else if (currentTask.operation == "SENSOR_WRITE") {
                
                performSensorWrite(currentTask.sensorName, currentTask.value);
            }

            
        }
    }

private:
    
    void performSensorRead(String sensorName) {
        Serial.print("Reading from sensor: ");
        Serial.println(sensorName);
    }

    void performSensorWrite(String sensorName, float value) {
        Serial.print("Writing to sensor: ");
        Serial.print(sensorName);
        Serial.print(" with value: ");
        Serial.println(value);
    }
};
