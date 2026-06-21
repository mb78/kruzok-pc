# Display specs

- D-FLIFE 1.8-inch SPI TFT LCD Display Module
- 128x160 RGB LCD Display Module
- 8-pin Full-color
- ST7735 Driver Module with SPI Interface for DIY Projects
  (or ST7789)

Front / back side

```text
        G V S S R
        N C C D E D C B
        D C K A S C S L
    +---[][][][][][][][]---+   +---[][][][][][][][]---+
    |---1-2-3-4-5-6-7-8----|   |                      |
    |                      |   |                      |
    |                      |   |  R2 R1        - U1   |
    |                      |   |  .  |         . J1   |
    |                      |   |               - C1   |
    |                      |   |  1.8"TFT128*RGB*160  |
    |                      |   |       VER 1.0        |
    |                      |   |                      |
    |                      |   |                      |
    |                      |   |                      |
    |----------------------|   |                      |
    | 1.8"TFT128*RGB*160   |   |                      |
    +----------------------+   +----------------------+
```

- TFT = Thin-Film Transistor
- displays consist of minuscule pixels, each governed by individual transistors
  (managing color and brightness)
- pixel is composed of three sub-pixels, one for red, green, and blue

# ESP32 C3 Zero Spec

Links

- https://www.waveshare.com/wiki/ESP32-C3-Zero
- https://files.waveshare.com/wiki/ESP32-C3-Zero/XL-0807RGBC-WS2812B%20(1).pdf
- https://github.com/espressif/esp-idf (Espressif IoT Development Framework)
  - https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/api-conventions.html
- https://www.espboards.dev/esp32/esp32-c3-zero/

Chip Espressif ESP32-C3FN4, RiscV32

- size 18x22mm
- 160 MHzCPU
- memory
  - 4MB Flash
  - 400KB of SRAM
  - 384KB ROM
- WiFi, 802.11 b/g/n, onboard ceramic antenna
- BT 5.0 LE
- BOOT button and a RESET button
- 15 GPIO pins
  - GPIO12 to GPIO17 not exposed (used for stacking the 4MB Flash)
  - GPIO10 to connect with WS2812 RGB LED
  - TX is GPIO21, and RX is GPIO20
  - does not employ a USB to UART chip
  - 6 analog IN
  - 15 PWM
  - 22 interrupts
  - interfaces:
    - 3 × SPI
              - 1 × I2C
    - 2 × UART
    - 1 × I2S
    - 2 × ADC
- When flashing firmware, press and hold the BOOT button (GPIO9) and then connect the Type-C cable

Arduino IDE

- https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
- you need to enable USB CDC when using Arduino IDE

```text
              USB-C
             +-----+
    +--------+-----+-------+
    |                      |
1  -| 5V                21 |- 18
2  -| GND               20 |- 17
3  -| 3V3               19 |- 16
4  -| 0  BOOT 10 RESET  18 |- 15
5  -| 1  []   []    []  10 |- 14
6  -| 2     +-----+      9 |- 13
7  -| 3     |     |      8 |- 12
8  -| 4     +-----+      7 |- 11
9  -| 5                  6 |- 10
    |       [ C3  ]        |
    +----------------------+

GP0-GP4: UART1/PWM/TWAI/I2S/ADC/I2C/SPI
GP5-GP9: as above, without ADC
GP10: integrated LED WS2812
GP18: USB DM
GP19: USB DP
GP20: UART0 RX
GP21: UART0 TX

```

## Projects

### Blink RGB LED on GP10

- Calling `digitalWrite(RGB_BUILTIN, HIGH)` will use hidden RGB driver.
- WARNING: After using digitalWrite to drive RGB LED it will be impossible to drive the same pin
    with normal HIGH/LOW level
- `RGBLedWrite` demonstrates controll of each channel: \
  `void neopixelWrite(uint8_t pin, uint8_t red_val, uint8_t green_val, uint8_t blue_val)`

```c
#define RGB_BRIGHTNESS 10 // Change white brightness (max 255)

// the setup function runs once when you press reset or power the board
#ifdef RGB_BUILTIN
#undef RGB_BUILTIN
#endif
#define RGB_BUILTIN 10

void setup() {
  // No need to initialize the RGB LED
}

// the loop function runs over and over again forever
void loop() {
#ifdef RGB_BUILTIN
  // digitalWrite(RGB_BUILTIN, HIGH);   // Turn the RGB LED white
  neopixelWrite(RGB_BUILTIN,RGB_BRIGHTNESS,RGB_BRIGHTNESS,RGB_BRIGHTNESS); // Red
  delay(1000);
  // digitalWrite(RGB_BUILTIN, LOW);    // Turn the RGB LED off
  neopixelWrite(RGB_BUILTIN,0,0,0); // Red
  delay(1000);

  neopixelWrite(RGB_BUILTIN,RGB_BRIGHTNESS,0,0); // Red
  delay(1000);
  neopixelWrite(RGB_BUILTIN,0,RGB_BRIGHTNESS,0); // Green
  delay(1000);
  neopixelWrite(RGB_BUILTIN,0,0,RGB_BRIGHTNESS); // Blue
  delay(1000);
  neopixelWrite(RGB_BUILTIN,0,0,0); // Off / black
  delay(1000);
#endif
}
```

### TFT display

#### Wiring

```text
Display   ESP32
GND   1    2   GND
VCC   2    3   3V3
SCK   3    8   GP4
SDA   4   10   GP6
RES   5   12   GP8
 DC   6   13   GP9
 CS   7    9   GP5
 BL   8    3   3V3
```
#### Arduino Code

```c
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
```

vim: et ts=2 sw=2 et
