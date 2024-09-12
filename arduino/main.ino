#include <SPI.h>
#include <SD.h>
#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

SoftwareSerial blue(6,7); // RX, TX
File theFile;
LiquidCrystal lcd(9, 8, 5, 4, 3, 2);
// change this to match your SD shield or module;
const int chipSelect = 10;



bool key_in(int asci,int count){
int i=0;
  while(i!=count){
int a = blue.read();
// Serial.print(a);
if(a==asci){
  i=i+1;
}
}
i=0;
return true;
}


void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  blue.begin(9600);
  lcd.begin(16, 2);
 
    // Clears the LCD screen
  lcd.clear();
}

void loop()
{
  
while(!blue.available()){}

while(1){
  Serial.print("Initializing SD card...");
  if (!SD.begin()) {
    Serial.println("initialization failed!");
    return;
  }
  Serial.println("initialization done.");
  theFile = SD.open("data.txt", FILE_WRITE);
  if (theFile) {
    int aval = micros();
    for(int i = 0;i<100;i++){
    theFile.println(analogRead(A0));
    theFile.println(analogRead(A1));
    theFile.println(analogRead(A2));
    }
    int akhar = micros();
    int zaman = aval-akhar;
    theFile.close();
    // lcd.print(zaman);
    blue.println(zaman);
  } 
  else {
    Serial.println("error opening data.txt");
  }


  theFile = SD.open("data.txt");
  if (theFile) {
    while (theFile.available()) {
      blue.write(theFile.read());
      
    }
    theFile.close();

  }
  else {
    Serial.println("error opening test.txt");
  }
  SD.remove("data.txt");


while(!key_in(122,4)){    //--------------------------------------------------(zzzz)
}
delay(1000);
for(int j=0;j<6;j++){
  // Serial.println(blue.read());
  lcd.write(blue.read());
}
while(!key_in(113,4)){    //--------------------------------------------------(qqqq)
}
}


}