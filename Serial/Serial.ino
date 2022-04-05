int add0 = P6_0;
int add1 = P6_1;
int add2 = P6_2;
int add3 = P6_3;
int add4 = P6_4;

int relay1 = P6_5;
int relay2 = P6_6;
int relay3 = P7_0;
int relay4 = P1_6;
int relay5 = P2_7;
int relay6 = P3_2;
int relay7 = P4_1;
int relay8 = P4_2;
int relay9 = P3_6;

byte address = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  Serial1.begin(9600);
  Serial1.setTimeout(1);
  
  pinMode(add0, INPUT_PULLUP);
  pinMode(add1, INPUT_PULLUP);
  pinMode(add2, INPUT_PULLUP);
  pinMode(add3, INPUT_PULLUP);
  pinMode(add4, INPUT_PULLUP);
  
  pinMode(relay1, INPUT_PULLUP);
  pinMode(relay2, INPUT_PULLUP);
  pinMode(relay3, INPUT_PULLUP);
  pinMode(relay4, INPUT_PULLUP);
  pinMode(relay5, INPUT_PULLUP);
  pinMode(relay6, INPUT_PULLUP);
  pinMode(relay7, INPUT_PULLUP);
  pinMode(relay8, INPUT_PULLUP);
  pinMode(relay9, INPUT_PULLUP);

}

void loop() {
  char serial_pack[5];
  
  while(Serial1.available() > 0){
    for(int i = 0; i < 5; i++){
      serial_pack[i] = Serial1.read();
      delay(5);
    }
  }

  Serial1.print("MSP430");

  Serial.println("---- Data from Raspberry ----");  
  delay(5);
  for(int i = 0; i < 5; i++){
    Serial.print(serial_pack[i]); 
  }

//---------------------------------------------

  if(digitalRead(add0)){
    address |= (1<<0);
  } else {
    address &= ~(1<<0);
  }

  if(digitalRead(add1)){
    address |= (1<<1);
  } else {
    address &= ~(1<<1);
  }
  Serial.println("---- Uart 2 Address ----");
  Serial.println(address);
  
//---------------------------------------------
  
  Serial.println("---- Relays State ----");
  Serial.print("Relay 1: ");
  Serial.println(digitalRead(relay1));
  Serial.print("Relay 2: ");
  Serial.println(digitalRead(relay2));
  Serial.print("Relay 3: ");
  Serial.println(digitalRead(relay3));
  Serial.print("Relay 4: ");
  Serial.println(digitalRead(relay4));
  Serial.print("Relay 5: ");
  Serial.println(digitalRead(relay5));
  Serial.print("Relay 6: ");
  Serial.println(digitalRead(relay6));
  Serial.print("Relay 7: ");
  Serial.println(digitalRead(relay7));
  Serial.print("Relay 8: ");
  Serial.println(digitalRead(relay8));
  Serial.print("Relay 9: ");
  Serial.println(digitalRead(relay9));
  
  delay(1000);
}
