#include <Wire.h>

// MCP9808 I2C address (default: 0x18)
#define MCP9808_ADDR 0x18
// TMP102 I2C address (default: 0x48)
#define TMP102_ADDR 0x48

// Register addresses for MCP9808
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
  
  // TMP102 doesn't need configuration for basic operation
}

void loop() {
  float temp1 = readMCP9808Temperature();
  float temp2 = readTMP102Temperature();
  
  Serial.print("MCP9808 Temperature: ");
  Serial.print(temp1);
  Serial.println(" °C");
  
  Serial.print("TMP102 Temperature: ");
  Serial.print(temp2);
  Serial.println(" °C");
  
  delay(1000);
}

float readMCP9808Temperature() {
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

float readTMP102Temperature() {
  uint16_t tempData;
  
  // Request temperature data
  Wire.beginTransmission(TMP102_ADDR);
  Wire.write(0x00); // Temperature register
  Wire.endTransmission();
  
  // Read temperature data (2 bytes)
  Wire.requestFrom(TMP102_ADDR, 2);
  if (Wire.available() == 2) {
    uint8_t msb = Wire.read();
    uint8_t lsb = Wire.read();
    
    // Combine the bytes
    tempData = ((msb << 8) | lsb) >> 4; // 12-bit resolution
    
    // Convert to temperature (0.0625°C resolution)
    float temp = tempData * 0.0625;
    if (msb & 0x80) { // Handle negative temperatures
      temp -= 256;
    }
    return temp;
  }
  return -999.0; // Return error value if read fails
}
