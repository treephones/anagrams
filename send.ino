#include <Mouse.h>

void setup() {
  Mouse.begin();
  Serial1.begin(9600);
  while(!Serial1) {}
}

int currPos = 0;
String currMove = String();

void loop() {
  if(Serial1.available() > 0) {
    int x = Serial1.read()-'0';
    if(x == -3) {
      currMove.concat("-");
    }
    else if(x == 5) {
      //"enter" sequence 
      Mouse.move(60-currPos,-21);
      Mouse.click();
      Mouse.move(currPos-60,21);
    }
    else {
      currMove.concat(String(x));
      if(isPos(currMove.toInt())) { 
        
        Mouse.move(conv(currMove.toInt()),0);
        Mouse.click();
        
        currPos += conv(currMove.toInt());
        Serial.println(currMove.toInt());
        //Mouse.click(); 
        currMove = String();
    }
   }
  }
} 

int conv(int x)  {
  int to[][2] = {
    {20, 18},
    {-20, -18},
    {40, 26},
    {-40, -26},
    {60, 31},
    {-60, -31},  //31.8
    {80, 36},
    {-80, -36},
    {100, 40},
    {-100, -40}
  };
  for(int i = 0; i < 10; ++i) {
    if(to[i][0] == x) {
      return to[i][1];
    }
  }
}

bool isPos(int x) {
  int v[] = {20,-20,40,-40,60,-60,80,-80,100,-100};
  for(int i = 0; i < 10; ++i) {
   if(x == v[i]) {
      return true;
    }
  }
  return false;
}
