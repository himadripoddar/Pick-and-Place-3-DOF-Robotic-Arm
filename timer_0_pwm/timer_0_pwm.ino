
#include<avr/io.h>

int main()
{
  TCCR0A |= (1<<COM0A1) |(1<<WGM01) | (1<< WGM00);
  TCCR0B |=   (1<< CS02) ;
  DDRD= 0xFF;
  
  
  while(1)
  {
    OCR0A=45;
  }
  

  
}

