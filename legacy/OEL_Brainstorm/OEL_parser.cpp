#include <stdio.h>
#include <stdint.h>
#include <string>

using namespace std;

struct Range {
    uint8_t startBit;
    uint8_t endBit;
};

struct SensorConfig {
    string name;
    string protocol;
    uint8_t i2cAddress;
    uint8_t wakeupCommand[10];
    uint8_t lenWakeupCommand;
    uint8_t readCommand[10];
    uint8_t lenReadCommand;
    uint8_t lenIncomingData;
    string dataKeyVals[10];
    uint8_t lenDataKeyVals;
    Range dataRange[10];
    string scaleFormats[10];
};

void parseSensorConfig(String input, SensorConfig &config) {
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
        commandName = command.trim();
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
  }