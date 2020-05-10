#include<avr/io.h>
#include<math.h>
#include<util/delay.h>
void Wait()
{
  uint8_t i;
  for(i=0;i<120;i++)
  {
    _delay_loop_2(0);
    _delay_loop_2(0);
    _delay_loop_2(0);
  }
}
int main()
{
  float cxb=434,cyb=120;
  float cxr=233 ,cyr=249 ;
 
  float xb,yb,Xb,Yb;
  float mb,nb,ob,pb,qb,lb,zb,ab;
  xb=cxb * 0.052;
  yb=cyb * 0.061;
  Xb=xb+6;
  Yb=yb;
  

  pb=sqrt(Xb*Xb+ Yb*Yb);
  mb=atan(Yb/Xb)*57.3;
  qb=sqrt(pb*pb + 100);
  nb=acos(qb/36)*57.3;
  ab=(acos(qb/36) - atan(10/pb))*57.3;
  ob=(2*nb);
  zb=180-ob;

  float xr,yr,Xr,Yr;
  float mr,nr,orr,pr,qr,lr,zr,ar;
  xr=cxr * 0.052;
  yr=cyr * 0.061;
  Xr=xr+6;
  Yr=yr;
  

  pr=sqrt(Xr*Xr+ Yr*Yr);
  mr=atan(Yr/Xr)*57.3;
  qr=sqrt(pr*pr + 100);
  nr=acos(qr/36)*57.3;
  ar=(acos(qr/36) - atan(10/pr))*57.3;
  orr=(2*nr);
  zr=180-orr;
  TCCR0A |= (1<<COM0A1) |(1<<WGM01) | (1<< WGM00);
  TCCR0B |=   (1<< CS02) ;
  DDRD= 0xFF;
  DDRC= 0xFF;
   //Configure TIMER1
   TCCR1A|=(1<<COM1A1)|(1<<COM1B1)|(1<<WGM11);        //NON Inverted PWM
   TCCR1B|=(1<<WGM13)|(1<<WGM12)|(1<<CS11)|(1<<CS10); //PRESCALER=64 MODE 14(FAST PWM)

   ICR1=4999;  //fPWM=50Hz (Period = 20ms Standard).

   DDRB|=0xFF;   //PWM Pins as Out
   

   while(1)
   {
       
  
      OCR1B=(180+(2.28*mb))+15;//BASE
      OCR1A=(180+(2.28*ab))-10; //0 degree
      OCR0A=(50+(0.56*zb));
      
      PORTC=0b00000001;
      Wait();
      while(1)
      {
        OCR1B=150;//BASE
        OCR1A=260; //0 degree
        OCR0A=90;
        PORTC=0b00000001;
        Wait();
        PORTC=0b00000000;
        PORTC=0b00000000;
        
        while(1)
        {
           OCR1B=180;//BASE
           OCR1A=370; //0 degree
           OCR0A=150;
           Wait();
           while(1)
           {
            OCR1B=(180+(2.28*mr))+15;//BASE
            OCR1A=(180+(2.28*ar))-12; //0 degree
            OCR0A=(50+(0.56*zr));
      
            PORTC=0b00000001;
            Wait();
            while(1)
            {
              OCR1B=400;//BASE
              OCR1A=260; //0 degree
              OCR0A=90;
              PORTC=0b00000001;
              Wait();
              PORTC=0b00000000;
              PORTC=0b00000000;
              while(1)
              {
                OCR1B=210;//BASE
                OCR1A=260; //0 degree
                OCR0A=90;
                Wait();
                while(1)
                {
                  OCR1B=180;//BASE
                  OCR1A=370; //0 degree
                  OCR0A=150;
                }
              }
            }
            
          
        }
      }
     }
      
   }
}

