int add0 = P6_0;
int add1 = P6_1;
int add2 = P6_2;
int add3 = P6_3;
int add4 = P6_4;
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

}

void loop() {
  char serial_pack[5];
  
  while(Serial1.available() > 0){
    for(int i = 0; i < 5; i++){
      serial_pack[i] = Serial1.read();
      delay(5);
    }
  }

  Serial1.print("MSP43");
  delay(5);
  for(int i = 0; i < 5; i++){
    Serial.print(serial_pack[i]); 
  }
  Serial.println("\n");

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
  Serial.println(address);
  
  delay(1000);
}
