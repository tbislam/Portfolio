#include <Servo.h>

int leftWhisker = 5;
int rightWhisker = 7;

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal


int PIEZOPIN = A0;

void setup() {
  // put your setup code here, to run once:\
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  Serial.begin(9600);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     //
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int leftWhiskerValue = digitalRead(leftWhisker);
  int rightWhiskerValue = digitalRead(rightWhisker);
  
  Serial.print("left whisker vlaue");
  Serial.print(leftWhiskerValue);
  delay(2000);
  Serial.println("right whisker value");
  Serial.println(rightWhiskerValue);
  delay(2000);
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  

  if(rightWhiskerValue == 0){ 
    servoLeft.writeMicroseconds(1700); 
    servoRight.writeMicroseconds(1300); 
    delay(300); 
  } 
  else if(rightWhiskerValue == 1){ 
    servoLeft.writeMicroseconds(1300); 
    servoRight.writeMicroseconds(1700); 
    delay(300);
  }
}

 
