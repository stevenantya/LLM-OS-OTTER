#include <mbed.h>
#include <map>
#include <cstring>
#include <string>
#include <Wire.h>

#define MS(x) chrono::milliseconds(x)

using namespace std; // we will be using std::chrono
using namespace rtos; // we will be using rtos::ThisThread
using namespace std::chrono_literals;

std::map<String, Thread*> sensorThreads;

Mutex i2cMutex;

struct Range {
  uint8_t startBit;
  uint8_t endBit;
};

// OEL Struct
struct SensorConfig {
    String name;
    String protocol;
    uint8_t i2cAddress;
    uint8_t wakeupCommand[10];
    uint8_t lenWakeupCommand;
    uint8_t readCommand[10];
    uint8_t lenReadCommand;
    uint8_t lenIncomingData;
    String dataKeyVals[10];
    uint8_t lenDataKeyVals;
    Range dataRange[10];
    String scaleFormats[10];
};

//OEL Parser
SensorConfig parseSensorConfig(String input) {
  SensorConfig config;
  // Split the input by semicolons
  int startPos = 0;
  int endPos = input.indexOf(';');
  
  while (endPos != -1 || startPos < input.length()) {
    // Extract the current command
    String command;
    if (endPos != -1) {
      command = input.substring(startPos, endPos);
      startPos = endPos + 1;
    } else {
      command = input.substring(startPos);
      startPos = input.length();
    }
    
    // Find the equals sign if it exists
    int equalsPos = command.indexOf('=');
    String commandName;
    String commandValue;
    
    if (equalsPos != -1) {
      commandName = command.substring(0, equalsPos);
      commandValue = command.substring(equalsPos + 1);
      
      // Trim spaces from both parts
      commandName.trim();
      commandValue.trim();
    } else {
      command.trim();
      commandName = command;
      commandValue = "";
    }
    
    // Parse each command
    if (commandName == "NEW_SENSOR") {
      // Set the sensor name
      config.name = commandValue;
    }
    else if (commandName == "PROTOCOL") {
      // Set the protocol
      config.protocol = commandValue;
    }
    else if (commandName == "SENSOR_ADDR") {
      // Parse the I2C address (hex format)
      config.i2cAddress = (uint8_t)strtol(commandValue.c_str(), NULL, 16);
    }
    else if (commandName == "INIT_CMD") {
      // Parse the wakeup command bytes
      int cmdStart = commandValue.indexOf('(') + 1;
      int cmdEnd = commandValue.indexOf(')');
      String cmdStr = commandValue.substring(cmdStart, cmdEnd);
      
      config.lenWakeupCommand = 0;
      
      // Split by commas and parse bytes
      int bytesStartPos = 0;
      int bytesEndPos = cmdStr.indexOf(',');
      
      while (bytesEndPos != -1 || bytesStartPos < cmdStr.length()) {
        String byteStr;
        if (bytesEndPos != -1) {
          byteStr = cmdStr.substring(bytesStartPos, bytesEndPos);
          bytesStartPos = bytesEndPos + 1;
        } else {
          byteStr = cmdStr.substring(bytesStartPos);
          bytesStartPos = cmdStr.length();
        }
        
        // Trim spaces
        byteStr.trim();
        
        // Parse hex value
        if (byteStr.startsWith("0x")) {
          config.wakeupCommand[config.lenWakeupCommand] = (uint8_t)strtol(byteStr.c_str(), NULL, 16);
        } else {
          config.wakeupCommand[config.lenWakeupCommand] = (uint8_t)byteStr.toInt();
        }
        
        config.lenWakeupCommand += 1;
        
        // Find next comma
        bytesEndPos = cmdStr.indexOf(',', bytesStartPos);
      }
    }
    else if (commandName == "READ_CMD") {
      // Parse the read command bytes
      int cmdStart = commandValue.indexOf('(') + 1;
      int cmdEnd = commandValue.indexOf(')');
      String cmdStr = commandValue.substring(cmdStart, cmdEnd);
      
      config.lenReadCommand = 0;
      
      // Split by commas and parse bytes
      int bytesStartPos = 0;
      int bytesEndPos = cmdStr.indexOf(',');
      
      while (bytesEndPos != -1 || bytesStartPos < cmdStr.length()) {
        String byteStr;
        if (bytesEndPos != -1) {
          byteStr = cmdStr.substring(bytesStartPos, bytesEndPos);
          bytesStartPos = bytesEndPos + 1;
        } else {
          byteStr = cmdStr.substring(bytesStartPos);
          bytesStartPos = cmdStr.length();
        }
        
        // Trim spaces
        byteStr.trim();
        
        // Parse hex value
        if (byteStr.startsWith("0x")) {
          config.readCommand[config.lenReadCommand] = (uint8_t)strtol(byteStr.c_str(), NULL, 16);
        } else {
          config.readCommand[config.lenReadCommand] = (uint8_t)byteStr.toInt();
        }
        
        config.lenReadCommand += 1;
        
        // Find next comma
        bytesEndPos = cmdStr.indexOf(',', bytesStartPos);
      }
    }
    else if (commandName == "DATA_LEN") {
      // Set the expected data length
      config.lenIncomingData = commandValue.toInt();
    }
    else if (commandName == "DATA_KEY_VAL") {
      // Parse the data keys
      int keysStart = commandValue.indexOf('(') + 1;
      int keysEnd = commandValue.indexOf(')');
      String keysStr = commandValue.substring(keysStart, keysEnd);
      
      config.lenDataKeyVals = 0;
      
      // Split by commas and parse key-value pairs
      int keysStartPos = 0;
      int keysEndPos = keysStr.indexOf(',');
      
      while (keysEndPos != -1 || keysStartPos < keysStr.length()) {
        String keyStr;
        if (keysEndPos != -1) {
          keyStr = keysStr.substring(keysStartPos, keysEndPos);
          keysStartPos = keysEndPos + 1;
        } else {
          keyStr = keysStr.substring(keysStartPos);
          keysStartPos = keysStr.length();
        }
        
        // Trim spaces
        keyStr.trim();
        
        // Parse index and name
        int colonPos = keyStr.indexOf(':');
        String nameStr = keyStr.substring(colonPos + 1);
        nameStr.trim();
        
        // Remove quotes if present
        if (nameStr.startsWith("\"") && nameStr.endsWith("\"")) {
          nameStr = nameStr.substring(1, nameStr.length() - 1);
        }
        
        config.dataKeyVals[config.lenDataKeyVals] = nameStr;
        config.lenDataKeyVals += 1;
        
        // Find next comma
        keysEndPos = keysStr.indexOf(',', keysStartPos);
      }
    }
    else if (commandName == "DATA_FORMAT") {
      // Parse the data format ranges
      int formatStart = commandValue.indexOf('(') + 1;
      int formatEnd = commandValue.indexOf(')');
      String formatStr = commandValue.substring(formatStart, formatEnd);
      
      // Split by commas and parse format ranges
      int formatStartPos = 0;
      int formatEndPos = formatStr.indexOf(',');
      int index = 0;
      
      while (formatEndPos != -1 || formatStartPos < formatStr.length()) {
        String rangeStr;
        if (formatEndPos != -1) {
          rangeStr = formatStr.substring(formatStartPos, formatEndPos);
          formatStartPos = formatEndPos + 1;
        } else {
          rangeStr = formatStr.substring(formatStartPos);
          formatStartPos = formatStr.length();
        }
        
        // Trim spaces
        rangeStr.trim();
        
        // Parse index and range
        int colonPos = rangeStr.indexOf(':');
        String rangeDef = rangeStr.substring(colonPos + 1);
        rangeDef.trim();
        
        // Remove brackets
        if (rangeDef.startsWith("[") && rangeDef.endsWith("]")) {
          rangeDef = rangeDef.substring(1, rangeDef.length() - 1);
        }
        
        // Split start and end bits
        int rangeDelimPos = rangeDef.indexOf(':');
        config.dataRange[index].startBit = rangeDef.substring(0, rangeDelimPos).toInt();
        config.dataRange[index].endBit = rangeDef.substring(rangeDelimPos + 1).toInt();
        
        index += 1;
        
        // Find next comma
        formatEndPos = formatStr.indexOf(',', formatStartPos);
      }
    }
    else if (commandName == "SCALE_FORMAT") {
      // Parse the scaling formats
      int scaleStart = commandValue.indexOf('(') + 1;
      int scaleEnd = commandValue.indexOf(')');
      String scaleStr = commandValue.substring(scaleStart, scaleEnd);
      
      // Split by commas and parse scaling formats
      int scaleStartPos = 0;
      int scaleEndPos = scaleStr.indexOf(',');
      int index = 0;
      
      while (scaleEndPos != -1 || scaleStartPos < scaleStr.length()) {
        String formatStr;
        if (scaleEndPos != -1) {
          formatStr = scaleStr.substring(scaleStartPos, scaleEndPos);
          scaleStartPos = scaleEndPos + 1;
        } else {
          formatStr = scaleStr.substring(scaleStartPos);
          scaleStartPos = scaleStr.length();
        }
        
        // Trim spaces
        formatStr.trim();
        
        // Parse index and format
        int colonPos = formatStr.indexOf(':');
        String formatDef = formatStr.substring(colonPos + 1);
        formatDef.trim();
        
        // Remove quotes if present
        if (formatDef.startsWith("\"") && formatDef.endsWith("\"")) {
          formatDef = formatDef.substring(1, formatDef.length() - 1);
        }
        
        config.scaleFormats[index] = formatDef;
        index += 1;
        
        // Find next comma
        scaleEndPos = scaleStr.indexOf(',', scaleStartPos);
      }
    }
    else if (commandName == "NEW_SENSOR_READ") {
      // This is just a marker, no value to parse
    }
    
    // Find the next command
    endPos = input.indexOf(';', startPos);
  }
  return config;
}

void init_i2c(SensorConfig config) {
  i2cMutex.lock();
  //Start Transmission to i2c address
  if (config.lenWakeupCommand > 0) {
    Wire.beginTransmission(config.i2cAddress);

    //Wire.write 0,1,2,3 byte wakeup/config command
    for (int i = 0; i < config.lenWakeupCommand; i += 1) {
      Wire.write(config.wakeupCommand[i]);
    }

    //End Transmission
    Wire.endTransmission();
  }
  i2cMutex.unlock();
}

float applyRPNScaling(uint32_t value, String rpnFormat) {
  float stack[10];
  int stackIndex = 0;

  int i = 0;
  while (i < rpnFormat.length()) {
    while (i < rpnFormat.length() && rpnFormat.charAt(i) == ' ') {
      i += 1;
    }
    
    if (i >= rpnFormat.length()) break;

    // Check for operators
    // Check for shift operators first by looking ahead
    if ( (rpnFormat.charAt(i) == '<' && (i+1 < rpnFormat.length() && rpnFormat.charAt(i+1) == '<')) ||
         (rpnFormat.charAt(i) == '>' && (i+1 < rpnFormat.length() && rpnFormat.charAt(i+1) == '>')) ) {
      // Pop two values from the stack
      if(stackIndex < 2) { /* handle error */ }
      uint32_t b = stack[--stackIndex]; // Previously was float
      uint32_t a = stack[--stackIndex];

      if (rpnFormat[i] == '<')
        stack[stackIndex++] = (uint32_t)((uint32_t)a << (uint32_t)b);
      else
        stack[stackIndex++] = (uint32_t)((uint32_t)a >> (uint32_t)b);

      i += 2; // skip both characters
    }
    // Check for other operators
    else if (rpnFormat.charAt(i) == '+' || rpnFormat.charAt(i) == '-' || 
        rpnFormat.charAt(i) == '*' || rpnFormat.charAt(i) == '/' ||
        rpnFormat.charAt(i) == '%' || rpnFormat.charAt(i) == '&' ||
        rpnFormat.charAt(i) == '|') {
      // Pop two values from stack
      stackIndex -= 1;
      float b = stack[stackIndex];
      
      stackIndex -= 1;
      float a = stack[stackIndex];

      switch (rpnFormat.charAt(i)) {
        case '+':
          stack[stackIndex] = a + b;
          stackIndex += 1;
          break;
        case '-':
          stack[stackIndex] = a - b;
          stackIndex += 1;
          break;
        case '*':
          stack[stackIndex] = a * b;
          stackIndex += 1;
          break;
        case '/':
          stack[stackIndex] = a / b;
          stackIndex += 1;
          break;
        case '%':
          stack[stackIndex] = fmod(a,b);
          stackIndex += 1;
          break;
        case '&':
          stack[stackIndex] = (float)((uint32_t)a & (uint32_t)b);
          stackIndex += 1;
          break;
        case '|':
          stack[stackIndex] = (float)((uint32_t)a | (uint32_t)b);
          stackIndex += 1;
          break;
      }
      i += 1;
    }
    // Check for 'x' which is substituted with the original value
    else if (rpnFormat.charAt(i) == 'x' || rpnFormat.charAt(i) == 'X') {
      stack[stackIndex] = (float) value;
      stackIndex += 1;
      i += 1;
    }
    // Parse number
    else if (isDigit(rpnFormat.charAt(i)) || rpnFormat.charAt(i) == '.') {
      String numStr = "";
      
      // Extract the full number string
      while (i < rpnFormat.length() && 
             (isDigit(rpnFormat.charAt(i)) || rpnFormat.charAt(i) == '.')) {
        numStr += rpnFormat.charAt(i);
        i += 1;
      }
      
      // Convert to float and push to stack
      stack[stackIndex] = numStr.toFloat();
      stackIndex += 1;
    }
    else {
      // Skip unknown characters
      i += 1;
    }
  }

  // The result should be the only value left on the stack
  return stack[0];
}

void process_data(uint8_t* data, SensorConfig config) {
  // Serial.println("-----------Received Data--------");
  // Serial.print(data[0],HEX);
  // Serial.print(data[1], HEX);
  // Serial.print(data[2],HEX);
  // Serial.print(data[3],HEX);
  // Serial.print(data[4], HEX);
  // Serial.print(data[5], HEX);
  // Serial.println("");
  // data[0] = 0x80;
  // data[1] = 0xB8;
  // data[2] = 0x30;
  // data[3] = 0x76;
  for (int i = 0; i < config.lenDataKeyVals; i += 1) {
    String dataName = config.dataKeyVals[i];

    Range dataRange = config.dataRange[i];
    uint8_t dataStartBit = dataRange.startBit;
    uint8_t dataEndBit = dataRange.endBit;

    // Serial.println("----------- Processing -----------");
    // Serial.print("Data Name: ");
    // Serial.println(dataName);
    // Serial.print("Start Bit: ");
    // Serial.println(dataStartBit);
    // Serial.print("End Bit: ");
    // Serial.println(dataEndBit);

    // Calculate which bytes contain our start and end bits
    uint8_t startByte = dataStartBit / 8;
    uint8_t startBitPosition = dataStartBit % 8;
    uint8_t endByte = dataEndBit / 8;
    uint8_t endBitPosition = dataEndBit % 8;

    // Serial.print("Start Byte: ");
    // Serial.println(startByte);
    // Serial.print("Start Bit Position: ");
    // Serial.println(startBitPosition);
    // Serial.print("End Byte: ");
    // Serial.println(endByte);
    // Serial.print("End Bit Position: ");
    // Serial.println(endBitPosition);

    // Calculate how many bits we need to extract
    uint8_t numBits = dataEndBit - dataStartBit + 1;
    // Serial.print("Number of Bits: ");
    // Serial.println(numBits);

    // Variable to hold our extracted value
    uint32_t extractedValue = 0;

    // Extract the bits
    if (startByte == endByte) {
      // All bits are in the same byte
      uint8_t mask = ((1 << numBits) - 1) << startBitPosition;
      extractedValue = (data[startByte] & mask) >> startBitPosition;

      // Serial.print("Single-byte mask: 0b");
      // Serial.println(mask, BIN);
      // Serial.print("Extracted Value: ");
      // Serial.println(extractedValue);
    } else {
      // Bits span multiple bytes
      // First byte - get bits from startBitPosition to end of byte
      uint8_t bitsFromFirstByte = 8 - startBitPosition;
      uint8_t firstByteMask = ((1 << bitsFromFirstByte) - 1);
      uint8_t firstByteData = data[startByte] & firstByteMask;
      extractedValue = firstByteData;
      // Serial.print("First Byte Mask: 0b");
      // Serial.println(firstByteMask, BIN);
      // Serial.print("Extracted First Byte Value: ");
      // Serial.println(extractedValue);

      // Middle bytes (if any) - get all bits
      for (int j = startByte + 1; j < endByte; j++) {
        // Serial.print("Processing Middle Byte: ");
        // Serial.println(j);
        // Serial.print("Byte Value: 0x");
        // Serial.println(data[j], HEX);
        uint8_t middleByteData = data[j];
        extractedValue = (extractedValue << 8) | middleByteData;
        // extractedValue |= ((uint32_t)data[j]) << (bitsFromFirstByte + (j - startByte - 1) * 8); //Little Endian
      }

      // Last byte - get bits from start of byte to endBitPosition
      uint8_t bitsFromLastByte = endBitPosition + 1;
      uint8_t lastByteMask = (1 << bitsFromLastByte) - 1;
      lastByteMask = lastByteMask << (8 - bitsFromLastByte);
      uint8_t lastByteData = (data[endByte] & lastByteMask);
      lastByteData = lastByteData >> (8 - bitsFromLastByte);
      extractedValue = (extractedValue << bitsFromLastByte) | lastByteData;
      
      // extractedValue |= ((data[endByte] & lastByteMask)) << (numBits - bitsFromLastByte); //Little Endian

      // Serial.print("Last Byte Mask: 0b");
      // Serial.println(lastByteMask, BIN);
      // Serial.print("Last byte: ");
      // Serial.println(lastByteData, HEX);
      // Serial.print("Extracted Last Byte Value: ");
      // Serial.println(data[endByte]&lastByteMask);
      
    }

    // Serial.print("Final Extracted Value: ");
    // Serial.print("dec= ");
    // Serial.print(extractedValue);
    // Serial.print("  hex= ");
    // Serial.println(extractedValue, HEX);

    String dataScaleFormat = config.scaleFormats[i];
    // Serial.print("Scale Format: ");
    // Serial.println(dataScaleFormat);
    float scaledValue = applyRPNScaling(extractedValue, dataScaleFormat);

    Serial.print(dataName);
    Serial.print(" = ");
    Serial.println(scaledValue);
    // Serial.println("----------------------------------");
  }
}

void read_i2c(SensorConfig config) {
  
  //Start transmission to i2c address
  // Serial.println(config.i2cAddress, HEX);
  Wire.beginTransmission(config.i2cAddress);

  //Wire.write 1,2 byte read command
  for (int i = 0; i < config.lenReadCommand; i += 1) {
    // Serial.println(config.readCommand[i], HEX);
    Wire.write(config.readCommand[i]);
  }
  Wire.endTransmission();

  //Wait for the sensor to respond
  // ThisThread::sleep_for(50ms);

  //Wire.request 2 or 6 bytes from i2c address
  uint8_t rawDataBytes [config.lenIncomingData];

  Wire.requestFrom(config.i2cAddress, config.lenIncomingData);
  bool isDataRead = 0;

  unsigned long startTime = millis();
  unsigned long timeout = 20; // 50 ms timeout
  while (millis() - startTime < timeout) {
    if (Wire.available() >= config.lenIncomingData) {
      for (int i = 0; i < config.lenIncomingData; i += 1) {
        uint8_t rcv = Wire.read();
        // Serial.println(rcv, HEX);
        rawDataBytes[i] = rcv; //0th index is the MSB.
        // Serial.print(rawDataBytes[i], HEX);
      }
      isDataRead = 1;
      break;
    }
  }
  if (isDataRead) {
    process_data(rawDataBytes, config);
    isDataRead = 0;
  }
  // Serial.println("--------------------");
  // Serial.println("");
  
} 

void thread_function(SensorConfig config) {
  osThreadId_t my_id = ThisThread::get_id();
  //Initialize sensor
  i2cMutex.lock();
  init_i2c(config);
  i2cMutex.unlock();
  ThisThread::sleep_for(300ms);

  for (;;) {
    i2cMutex.lock();
    Serial.print("Running Sensor Thread: ");
    Serial.print(config.name);
    Serial.print("\n");
    read_i2c(config);
    i2cMutex.unlock();
    ThisThread::sleep_for(3s);
  }
}

void create_new_thread(SensorConfig config) {

  SensorConfig *config_ptr = new SensorConfig(config); // Dynamically allocate memory
  char * cstr = new char [config.name.length()+1];
  std::strcpy (cstr, config.name.c_str()); //What if I have 2 of the same sensors
  Thread *new_thread = new Thread(osPriorityNormal, OS_STACK_SIZE, nullptr, cstr);
  new_thread->start([config_ptr]() {
      thread_function(*config_ptr);
      delete config_ptr; // Free the memory after use
  });
  sensorThreads[config.name] = new_thread; 
}

//DEBUG CODES
void printSensorConfig(SensorConfig config) {
  // Print basic info
  Serial.println("===== Sensor Configuration =====");
  Serial.print("Sensor Name: ");
  Serial.println(config.name);
  Serial.print("Protocol: ");
  Serial.println(config.protocol);
  Serial.print("I2C Address: 0x");
  Serial.println(config.i2cAddress, HEX);
  
  // Print wakeup command
  Serial.print("Wakeup Command (");
  Serial.print(config.lenWakeupCommand);
  Serial.print(" bytes): ");
  for (int i = 0; i < config.lenWakeupCommand; i += 1) {
    Serial.print("0x");
    if (config.wakeupCommand[i] < 16) {
      Serial.print("0"); // Add leading zero for single-digit hex values
    }
    Serial.print(config.wakeupCommand[i], HEX);
    if (i < config.lenWakeupCommand - 1) {
      Serial.print(", ");
    }
  }
  Serial.println();
  
  // Print read command
  Serial.print("Read Command (");
  Serial.print(config.lenReadCommand);
  Serial.print(" bytes): ");
  for (int i = 0; i < config.lenReadCommand; i += 1) {
    Serial.print("0x");
    if (config.readCommand[i] < 16) {
      Serial.print("0"); // Add leading zero for single-digit hex values
    }
    Serial.print(config.readCommand[i], HEX);
    if (i < config.lenReadCommand - 1) {
      Serial.print(", ");
    }
  }
  Serial.println();
  
  // Print data length
  Serial.print("Incoming Data Length: ");
  Serial.println(config.lenIncomingData);
  
  // Print data keys and corresponding formats
  Serial.println("Data Keys and Formats:");
  for (int i = 0; i < config.lenDataKeyVals; i += 1) {
    Serial.print("  ");
    Serial.print(i);
    Serial.print(": \"");
    Serial.print(config.dataKeyVals[i]);
    Serial.print("\" | Bits [");
    Serial.print(config.dataRange[i].startBit);
    Serial.print(":");
    Serial.print(config.dataRange[i].endBit);
    Serial.print("] | Scale: ");
    Serial.println(config.scaleFormats[i]);
  }
  
  Serial.println("===============================");
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
}
void loop() {
  Serial.print("Main thread started.\n");

  while (true) {
    if (Serial.available()) {
      String str_input = Serial.readString();
      str_input.trim();

      if (str_input.startsWith("NEW_SENSOR")) {
        SensorConfig config = parseSensorConfig(str_input);
        printSensorConfig(config);
        create_new_thread(config);
      } else if (str_input.startsWith("SENSOR_REMOVE")) {
          String sensor_name = str_input.substring(str_input.indexOf(' ') + 1);
          sensor_name.trim();
          if (sensorThreads.find(sensor_name) != sensorThreads.end()) {
              Thread *thread = sensorThreads[sensor_name];
              thread->terminate(); // Terminate the thread
              delete thread; // Clean up the thread object
              Serial.print("Freeing thread");
              Serial.print("\n");
              sensorThreads.erase(sensor_name); // Remove from map
              Serial.print("Removed Sensor: ");
              Serial.print(sensor_name);
              Serial.print("\n");
              Serial.print("Returning to OS");
              Serial.print("\n");
          }
      } 
      //TODO: Sensor Suspend and Resume
      //TODO: Sensor Resolution
    }
    ThisThread::sleep_for(1ms);
  }
}