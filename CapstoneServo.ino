#include <WiFi.h>
#include <ESP32Servo.h>

Servo servoA;
Servo servoB;
Servo servoC;
Servo servoD;


const char* ssid = "capstone-wifi";
const char* password = "password";

//const char* ssid = "Barronsrevenge";
//const char* password = "98765432";

// const int LEDpin = 27;

float deg = 0;          // variable to store the servo position
int servoPin = 27; 
int servoPinB = 26;

int servoPinC = 33;

int servoPinD = 17;


WiFiServer server(80);

void setup() {

  Serial.begin(9600);
  delay(1000);
  Serial.println("Starting!");
  delay(1000);
	ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);


  //servoA.write(degreeToPos(50)); //22 = closed
  //delay(10000);
  //servoA.write(degreeToPos(22));


  //servoB.write(degreeToPos(50)); //22 = closed
  //delay(10000);
  //servoB.write(degreeToPos(22));

  servoD.setPeriodHertz(50);    // standard 50 hz servo
	servoD.attach(servoPinD, 500, 2500);

  bool attached2 = servoD.attached();
  Serial.println(attached2 ? "Servo D attached successfully" : "Servo D attach failed");


  servoB.setPeriodHertz(50);    // standard 50 hz servo
	servoB.attach(servoPinB, 500, 2500);

  delay(1000);

  servoA.setPeriodHertz(50);    // standard 50 hz servo
	servoA.attach(servoPin, 500, 2500);



  bool attached = servoA.attached();
  Serial.println(attached ? "Servo A attached successfully" : "Servo A attach failed");

  delay(500);
  //servoA.write(degreeToPos(50));

  servoC.setPeriodHertz(50);    // standard 50 hz servo
	servoC.attach(servoPinC, 500, 2500);

  //servoC.write(degreeToPos(50)); //22 = closed
  //delay(10000);
  //servoC.write(degreeToPos(22));

  

  //servoD.write(degreeToPos(50)); //22 = closed
  //delay(10000);
  //servoD.write(degreeToPos(22));

  servoA.write(degreeToPos(0)); //22 = closed
  servoD.write(degreeToPos(0)); //22 = closed
  servoC.write(degreeToPos(0)); //22 = closed
  servoB.write(degreeToPos(0)); //22 = closed
  

  delay(10000);
  servoA.write(degreeToPos(20)); //22 = closed
  servoB.write(degreeToPos(20)); //22 = closed
  servoC.write(degreeToPos(20)); //22 = closed
  servoD.write(degreeToPos(20)); //22 = closed

  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
 
  Serial.println("Connected to the WiFi network");
  server.begin();

}

void loop() {


  WiFiClient client = server.available(); // Listen for incoming clients

  if (client) {
    Serial.println("New Client.");
    String currentLine = "";
    
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c); // For debugging

        currentLine += c;
        

        // Check for end of line
        if (c == '\n' || c == '\r') {
          Serial.println("Received command: " + currentLine);
          
          // Respond to the client
          handleCommand(currentLine);

          currentLine = ""; // Clear the line for the next command
          break; // Break out of the while loop
        }
      }
    }
    
    client.stop(); // Close the connection
    Serial.println("Client disconnected.");
  }
}

float degreeToPos(float deg) {
  return deg/1.5;
}

void moveServo(Servo &servo, int angle) {
  Serial.println("Moving!");
    servo.write(degreeToPos(angle));
    delay(2000); // Remove or reduce if not needed
}

void handleCommand(String command) {
    if (command.startsWith("A")) {
        Serial.println("Starts with A!");
        Serial.println(command);
        moveServo(servoA, parseAngle(command));
    } else if (command.startsWith("B")) {
        moveServo(servoB, parseAngle(command));
    } else if (command.startsWith("C")) {
        moveServo(servoC, parseAngle(command));
    } else if (command.startsWith("D")) {
        moveServo(servoD, parseAngle(command));
    }
}

int parseAngle(String command) {
    //if (command.endsWith("ten")) return 60;
    //if (command.includes("nine")) return 31;
    //if (command.endsWith("eight")) return 30;
    //if (command.endsWith("seven")) return 29;
    //if (command.endsWith("six")) return 28;
    //if (command.endsWith("five")) return 27;
    //if (command.endsWith("four")) return 26;
    //if (command.endsWith("three")) return 25;
    //if (command.endsWith("two")) return 24;
    //if (command.endsWith("one")) return 23;
    //if (command.endsWith("zero")) return 22;

    if(command.indexOf("ten") > 0) return 10;
    if(command.indexOf("nine") > 0) return 11;
    if(command.indexOf("eight") > 0) return 12;
    if(command.indexOf("seven") > 0) return 13;
    if(command.indexOf("six") > 0) return 14;
    if(command.indexOf("five") > 0) return 15;
    if(command.indexOf("four") > 0) return 16;
    if(command.indexOf("three") > 0) return 17;
    if(command.indexOf("two") > 0) return 18;
    if(command.indexOf("one") > 0) return 19;
    if(command.indexOf("zero") > 0) return 20;
    // Add all mappings as needed


}