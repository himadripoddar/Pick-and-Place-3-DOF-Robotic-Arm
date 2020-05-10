#include<avr/io.h>
int main()
{
  DDRC=0xFF;
  while(1)
  {
    PORTC=0b00000000;
  }
}

