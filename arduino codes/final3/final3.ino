#include<avr/io.h>
#include<math.h>
#include <util/delay.h>

int main()
{
  float x=15,y=15,X,Y;
  float m,n,o,p,q,l,z,a;
  
  X=x+6;
  Y=y;
  Serial.begin(9600);

  p=sqrt(X*X+ Y*Y);
  m=atan(Y/X)*57.3;
  q=sqrt(p*p + 100);
  n=acos(q/36)*57.3;
  a=(acos(q/36) - atan(10/p))*57.3;
  o=(2*n);
  z=180-o;
  TCCR0A |= (1<<COM0A1) |(1<<WGM01) | (1<< WGM00);
  TCCR0B |=   (1<< CS02) ;
  DDRD= 0xFF;
   //Configure TIMER1
   TCCR1A|=(1<<COM1A1)|(1<<COM1B1)|(1<<WGM11);        //NON Inverted PWM
   TCCR1B|=(1<<WGM13)|(1<<WGM12)|(1<<CS11)|(1<<CS10); //PRESCALER=64 MODE 14(FAST PWM)

   ICR1=4999;  //fPWM=50Hz (Period = 20ms Standard).

   DDRB|=0xFF;   //PWM Pins as Out
   
      
   while(1)
   {   
      OCR1B=180;//BASE
      OCR1A=370; //0 degree
      
      OCR0A=150;
      
      
   }
   }
   


