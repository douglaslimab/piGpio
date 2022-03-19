int btn = PUSH1;
String msg = "";

void setup() {
  Serial1.begin(9600);
  pinMode(btn, INPUT_PULLUP);
}

void loop() {
  int btnState = digitalRead(btn);

  msg = "";
  while(Serial1.available() > 0){
    char msgChar = Serial.read();
    msg += msgChar;
    if(msg == "uart2"){
      Serial1.print("2_MSP");
    } else if (msg == "uart4"){
      Serial1.print("4_MSP");
    }
  }
  
  delay(1000);
}
