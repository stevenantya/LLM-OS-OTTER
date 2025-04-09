#include <Wire.h>
//working
// I am using Arduino Nano 33 BLE Sense Lite. I want to connect to MCP9808 using I2C. I do not want to use any library. You can refer to the datasheet to program.
// MCP9808 I2C address (default: 0x18)
#define MCP9808_ADDR 0x18

// Register addresses
#define REG_CONFIG 0x01
#define REG_TEMP 0x05

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  // Configure MCP9808
  Wire.beginTransmission(MCP9808_ADDR);
  Wire.write(REG_CONFIG);
  Wire.write(0x00); // Default configuration
  Wire.write(0x00);
  Wire.endTransmission();
}

void loop() {
  float temperature = readTemperature();
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  delay(1000);
}

float readTemperature() {
  uint16_t tempData;
  
  // Request temperature data
  Wire.beginTransmission(MCP9808_ADDR);
  Wire.write(REG_TEMP);
  Wire.endTransmission();
  
  // Read temperature data (2 bytes)
  Wire.requestFrom(MCP9808_ADDR, 2);
  if (Wire.available() == 2) {
    uint8_t msb = Wire.read();
    uint8_t lsb = Wire.read();
    
    // Clear flag bits
    msb &= 0x1F;
    
    // Convert to temperature
    tempData = (msb << 8) | lsb;
    if (msb & 0x10) { // Handle negative temperatures
      tempData = ((~tempData) + 1) & 0x1FFF;
      return -(tempData * 0.0625);
    } else {
      return tempData * 0.0625;
    }
  }
  return -999.0; // Return error value if read fails
}

