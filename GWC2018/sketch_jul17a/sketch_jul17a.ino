#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal


int PIEZOPIN = 4;


// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin . 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
  // Attach LED pins here.
  
}  

void dance1()
{
  int pin = 3;
  pinMode(pin, OUTPUT);
  
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(250);                       // wait for a second
  digitalWrite(pin, LOW);
  delay(300);
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1500);
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(250);                       // wait for a second
  digitalWrite(pin, LOW);
  delay(250);
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(300);                       // wait for a second
  digitalWrite(pin, LOW);
  delay(300);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1900);
  delay(100);
  
  servoLeft.writeMicroseconds(1300);        
  servoRight.writeMicroseconds(1700);
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(250);  
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
  digitalWrite(pin,LOW);
  delay(250);
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  digitalWrite(pin,HIGH);
  delay(250);
  servoLeft.writeMicroseconds(1900);
  servoRight.writeMicroseconds(1500);
  digitalWrite(pin,LOW);
  delay(250);
  
}

void dance2()
{
  servoLeft.writeMicroseconds(2000);
  delay(2000);
  
}
void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  light();
  dance1();
  dance2();
  
  //Code spin 360
}
// the setup function runs once when you press reset or power the board
void light() 
{
     int PIEZOPIN = 4;                            // Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

    int pin = 3;
}

 
  

