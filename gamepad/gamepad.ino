#include <SoftwareSerial.h>

// MOT DE PASS 4321
// BAUD 57600

#define led 13

SoftwareSerial BT(11, 10);
char c = -1;

int x = 0;
int y = 0;
int input[] = {5, 5, 0, 0};
enum          {X, Y, A, B};
String message;
String prev;

void setup() {
  Serial.begin(9600);
  BT.begin(57600);
  pinMode(led, OUTPUT);
}

void loop() {
  updateInputs();
  updateMessage();
  c = -1;
  while(BT.available() > 0)
    c = BT.read();

  if(message != prev){
    Serial.println(message);
    BT.write(message.c_str());
  }
  delay(100);
  prev = message;
}

void updateMessage() {
  message = "";
  message = message + input[X] + input[Y] + input[A] + input[B];
  message += ";";
}

void updateInputs() {
  input[A] = digitalRead(A);
  input[B] = digitalRead(B);
  input[X] = 10 - map(analogRead(1), 0, 1024, 1, 10);
  input[Y] = map(analogRead(0), 0, 1024, 1, 10);
}
