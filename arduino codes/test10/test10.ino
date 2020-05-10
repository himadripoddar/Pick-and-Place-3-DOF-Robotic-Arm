void setup() {
 Serial.begin(9600);

}
unsigned int integervalue=0;
char incomingbyte;
void loop() {
  
  if(Serial.available()>0)
  {
    integervalue=0;
    while(1)
    {
      incomingbyte=Serial.read();
      if(incomingbyte == '\n')
      break;
      if(incomingbyte == -1)
      continue;
      integervalue *=10;
      integervalue = ((incomingbyte -48) + integervalue);
    }
    Serial.println(integervalue);
  }

}
