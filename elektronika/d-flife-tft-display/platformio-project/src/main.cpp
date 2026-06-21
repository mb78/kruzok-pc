#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

#define TFT_CS    5
#define TFT_RST   8
#define TFT_DC    9
#define TFT_MOSI  6
#define TFT_SCLK  4

Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

void setup() {
  Serial.begin(115200);
  tft.init(240,240,0);
  tft.setRotation(0);
  tft.fillScreen(ST77XX_BLACK);
  tft.println("ESP32-C3");
  tft.setCursor(10, 55);
  tft.println("Zero OK!");
}

void loop() {
  static int x = 120, y = 120;
  tft.fillCircle(x, y, 3, ST77XX_BLACK);
  x += (rand()%11) - 5;
  y += (rand()%11) - 5;
  if (x <= 5) x = 235;
  else if (x >=235) x = 5;
  if (y <= 10) y = 235;
  else if (y >=235) y = 5;
  tft.fillCircle(x, y, 3, ST77XX_RED);
  delay(50);
}
