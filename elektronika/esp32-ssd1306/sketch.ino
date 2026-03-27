#include <SPI.h>
#include <Wire.h>
#include "Adafruit_SHT4x.h"

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define OLED_MOSI   23 // D1
#define OLED_CLK    18 // D0
#define OLED_DC     16
#define OLED_CS     5
#define OLED_RESET  17

Adafruit_SHT4x sht4 = Adafruit_SHT4x();
Adafruit_SSD1306 display= Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT,
  OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);


void setup() 
{
  Serial.begin(115200);

  if(!display.begin(SSD1306_SWITCHCAPVCC))
  {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  
  display.clearDisplay();
  display.display();
  delay(1000);

//////////////////
  while (!Serial)
    delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit SHT4x test");
    Wire.begin(21, 22);
  if (! sht4.begin(&Wire)) 
  {
    Serial.println("Couldn't find SHT4x");
    while (1) delay(1);
  }
  Serial.println("Found SHT4x sensor");
  Serial.print("Serial number 0x");
  Serial.println(sht4.readSerial(), HEX);

  // You can have 3 different precisions, higher precision takes longer
  sht4.setPrecision(SHT4X_HIGH_PRECISION);

  // You can have 6 different heater settings
  sht4.setHeater(SHT4X_NO_HEATER);
  
}


/*
void loop() 
{
  sensors_event_t humidity, temp;
  
  uint32_t timestamp = millis();
  sht4.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
  timestamp = millis() - timestamp;

  Serial.print("Temperature: "); 
  Serial.print(temp.temperature); 
  Serial.println(" degrees C");
  Serial.print("Humidity: "); 
  Serial.print(humidity.relative_humidity); 
  Serial.println("% rH");

  Serial.print("Read duration (ms): ");
  Serial.println(timestamp);

  delay(1000);
}*/

void loop()
{
  StaticTextDisplay();
}

void StaticTextDisplay()
{
sensors_event_t humidity, temp;
  
  uint32_t timestamp = millis();
  sht4.getEvent(&humidity, &temp);// populate temp and humidity objects with fresh data
  timestamp = millis() - timestamp;
  
  Serial.print("Temperature: "); 
  Serial.print(temp.temperature); 
  Serial.print("\n");
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(5,18);
  char buf[1024];
  snprintf(buf,sizeof(buf),"temp:%0.1f\nhum:%0.1f",temp.temperature,humidity.relative_humidity);
  display.println(buf);
  display.display();
  delay(1000);
}
