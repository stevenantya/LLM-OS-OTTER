#include <Arduino.h>
#include <Wire.h>
#include <vector>
#include "expr.h"

static struct expr_func user_funcs[] = {
    {NULL, NULL, NULL, 0},
};

struct SensorCommand {
  String name;
  int address;
};

String convertToEvaluate(uint16_t rawData) {
    String evaluate_string = "rawData = ";
    String rawDataString = String(rawData);
    evaluate_string = evaluate_string + rawDataString + ", ";
    return evaluate_string;
}

class Sensor {
  private:
    String name;
    int address;
    int regAdr;
    String post_process;
  public:
    Sensor(const String& name, int address, int regAdr, String post_process) 
        : name(name), address(address), regAdr(regAdr), post_process(post_process) {}

    void readData() {
        Wire.beginTransmission(address);
        Wire.write(regAdr); // register to read from
        Wire.endTransmission(false);
        Wire.requestFrom(address, 2);

        while(Wire.available() < 2);

        uint16_t rawData = Wire.read() << 8 | Wire.read();

        // automatic post processing
        String evaluate_string = convertToEvaluate(rawData);
        String expression_string = post_process;
        evaluate_string = evaluate_string + expression_string;
        const char *expression = evaluate_string.c_str();
        struct expr_var_list vars = {0};
        struct expr *e = expr_create(expression, strlen(expression), &vars, user_funcs);

        if (e == NULL) {
            Serial.println("Expression creation failed");
            return;
        }

        float result = expr_eval(e);
        expr_destroy(e, &vars); // Clean up the expression object
        Serial.print("Sensor: ");
        Serial.print(name);
        Serial.print("  Temp in Celsius: ");
        Serial.println(result);
    }
};

volatile bool newCommandReceived = false;
String commandBuffer = "";
std::vector<Sensor*> sensors;

void serialEvent() {
    while (Serial.available()) {
        char receivedChar = Serial.read();
        if (receivedChar == '\n') {
            newCommandReceived = true;
            break; // Exit the loop to avoid reading more data after a complete command
        } else {
            commandBuffer += receivedChar;
        }
    }
}

void handleNewCommand(const String& command) {
    int firstComma = command.indexOf(',');
    int secondComma = command.indexOf(',', firstComma + 1);
    int thirdComma = command.indexOf(',', secondComma + 1);
    if (firstComma == -1 || secondComma == -1 || thirdComma == -1) {
        Serial.println("Invalid command format");
        return;
    }

    String name = command.substring(0, firstComma);
    int address = command.substring(firstComma + 1, secondComma).toInt();
    int regAdr = command.substring(secondComma + 1, thirdComma).toInt();
    String post_process = command.substring(thirdComma + 1);

    // Create and initialize a new sensor based on the command
    Sensor* sensor = new Sensor(name, address, regAdr, post_process);
    sensors.push_back(sensor);

    Serial.println("New sensor added: " + name + " at address " + String(address));
}

void readAllSensors() {
    for (Sensor* sensor : sensors) {
        sensor->readData();
    }
}

void setup() {
    Serial.begin(115200);
    Wire.begin();
    Serial.println("Ready to receive commands");
}

void loop() {
    delay(1000);
    if (Serial.available()) {
        while (Serial.available()) {
            char receivedChar = Serial.read();
            if (receivedChar == '\n') {
                newCommandReceived = true;
                break; // Exit the loop to avoid reading more data after a complete command
            } else {
                commandBuffer += receivedChar;
            }
            // Serial.println("nyangkut");
            readAllSensors();
        }

        if (newCommandReceived) {
            handleNewCommand(commandBuffer);
            commandBuffer = "";
            newCommandReceived = false;
        }
        
    }
    readAllSensors();
}