#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;
float applyRPNScaling(uint32_t value, std::string rpnFormat) {
    float stack[10];
    int stackIndex = 0;
  
    int i = 0;
    while (i < rpnFormat.length()) {
      while (i < rpnFormat.length() && rpnFormat[i] == ' ') {
        i += 1;
      }
      
      if (i >= rpnFormat.length()) break;
  
      // Check for operators
      // Check for shift operators first by looking ahead
      if ( (rpnFormat[i] == '<' && (i+1 < rpnFormat.length() && rpnFormat[i+1] == '<')) ||
           (rpnFormat[i] == '>' && (i+1 < rpnFormat.length() && rpnFormat[i+1] == '>')) ) {
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
      else if (rpnFormat[i] == '+' || rpnFormat[i] == '-' || 
          rpnFormat[i] == '*' || rpnFormat[i] == '/' ||
          rpnFormat[i] == '%' || rpnFormat[i] == '&' ||
          rpnFormat[i] == '|') {
        // Pop two values from stack
        stackIndex -= 1;
        float b = stack[stackIndex];
        
        stackIndex -= 1;
        float a = stack[stackIndex];
  
        switch (rpnFormat[i]) {
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
      else if (rpnFormat[i] == 'x' || rpnFormat[i] == 'X') {
        stack[stackIndex] = (float) value;
        stackIndex += 1;
        i += 1;
      }
      // Parse number
      else if (isdigit(rpnFormat[i]) || rpnFormat[i] == '.') {
        std::string numStr = "";
        
        // Extract the full number string
        while (i < rpnFormat.length() && 
               (isdigit(rpnFormat[i]) || rpnFormat[i] == '.')) {
          numStr += rpnFormat[i];
          i += 1;
        }
        
        // Convert to float and push to stack
        stack[stackIndex] = stof(numStr);
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

struct TestCase {
    uint32_t value;
    std::string rpn;
    float expected;
    std::string description;
};

int main() {
    TestCase tests[] = {
        {5, "x 3 <<", 40, "5 << 3"},
        {40, "x 1 >>", 20, "40 >> 1"},
        {5, "x 3 +", 8, "5 + 3"},
        {5, "x 3 -", 2, "5 - 3"},
        {5, "x 3 *", 15, "5 * 3"},
        {5, "x 3 /", 5.0f/3, "5 / 3"},
        {5, "x 3 %", 2, "fmod(5,3)"},
        {5, "x 3 &", (float)((uint32_t)5 & (uint32_t)3), "5 & 3"},
        {5, "x 3 |", (float)((uint32_t)5 | (uint32_t)3), "5 | 3"},
        {5, "x 2 * 3 +", 13, "(5 * 2) + 3"},
        {5, "x 4 * 2 /", 10, "(5 * 4) / 2"},
        {5, "x 3.5 *", 17.5, "5 * 3.5"},
        {5, "x 10 + 2 /", 7.5, "(5 + 10) / 2"},
        {5, "x 3 << 2 /", 20, "(5 << 3) / 2"},

        // Floating point specific tests:
        {5, "x 2.5 + 1.5 *", 11.25, "(5 + 2.5) * 1.5"},
        {5, "x 10.0 /", 0.5, "5 / 10.0"},
        {5, "x 2.3 %", 0.4, "fmod(5,2.3) ~ 0.4"},
        {5, "x 1.2 * 3.4 +", 9.4, "(5 * 1.2) + 3.4"}
    };

    int numTests = sizeof(tests) / sizeof(TestCase);
    // for (int i = 0; i < numTests; i++) {
    //     float result = applyRPNScaling(tests[i].value, tests[i].rpn);
    //     cout << "Test " << (i+1) << " (" << tests[i].description << "): ";
    //     cout << "Expected = " << tests[i].expected << ", Got = " << result;
    //     if (fabs(result - tests[i].expected) < 1e-5)
    //         cout << " [PASS]";
    //     else
    //         cout << " [FAIL]";
    //     cout << "\n";
    // }

    float result = applyRPNScaling(515029, "X 100.0 * 1048576.0 /");
    cout << "Hum: " << result << "\n";

    result = applyRPNScaling(3100, "X 4 >> 0.0625 *");
    cout << "Temp: " << result << "\n";
    return 0;
}

  
  