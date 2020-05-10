#define F_CPU 16000000
#include<avr/io.h>

int main()
{
  TCCR0A|= 1<<COM0A1 | 1<<COM0B1 | 1<<WGM00 | 1<<WGM01;
  TCCR0B|=  1<<CS00 | 1<<CS02;
  DDRD=0XFF;
 
  OCR0A=40;
  while(1);
}

