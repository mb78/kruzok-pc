#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <Adafruit_ST7789.h>
#include <SPI.h>

// Pin definitions
#define TFT_CS    5
#define TFT_RST   8
#define TFT_DC    9
#define TFT_MOSI  6
#define TFT_SCLK  4

// Init with hardware SPI
//Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);
Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

void setup() {
  Serial.begin(115200);

  // GREEN TAB = initR(INITR_144GREENTAB) for 128x128
  // If your 1.54" is 240x240 use ST7789 lib instead
  // For 128x128 ST7735 green tab:
  //tft.initR(INITR_GREENTAB);  // <-- green tab flag
  tft.init(240,240,0);
  tft.setRotation(0);
  tft.fillScreen(ST77XX_BLACK);

  //tft.setTextColor(ST77XX_GREEN);
  //tft.setTextSize(2);
  //tft.setCursor(10, 30);
  tft.println("ESP32-C3");
  tft.setCursor(10, 55);
  tft.println("Zero OK!");

  // Draw some shapes
  //tft.drawRect(5, 5, 118, 118, ST77XX_WHITE);
  //tft.fillCircle(64, 100, 10, ST77XX_CYAN);
}

void loop() {
  // Animate a bouncing dot
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