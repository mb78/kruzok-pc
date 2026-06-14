# Display specs

- D-FLIFE 1.8-inch SPI TFT LCD Display Module
- 128x160 RGB LCD Display Module
- 8-pin Full-color
- ST7735 Driver Module with SPI Interface for DIY Projects

Front / back side

```text
        G V S S R
        N C C D E D C B
        D C K A S C S L
    +---[][][][][][][][]---+   +---[][][][][][][][]---+
    |----------------------|   |                      |
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

# ESP32 C3 Zero Spec

Links

- https://www.waveshare.com/wiki/ESP32-C3-Zero
- https://files.waveshare.com/wiki/ESP32-C3-Zero/XL-0807RGBC-WS2812B%20(1).pdf
- https://github.com/espressif/esp-idf (Espressif IoT Development Framework)
  - https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/api-conventions.html

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
   -| 5V                21 |-
   -| GND               20 |-
   -| 3V3               19 |-
   -| 0  BOOT 10 RESET  18 |-
   -| 1  []   []    []  10 |-
   -| 2     +-----+      9 |-
   -| 3     |     |      8 |-
   -| 4     +-----+      7 |-
   -| 5                  6 |-
    |       [ C3  ]        |
    +----------------------+

```

## Sample demo - BlinkRGB

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

# ESP32 - wiring

```text
Display              ESP32
VCC ------------------- 5V
GND ------------------ GND
CS ------------------ IO-34 (CS)
RST ----------------- IO-38 (RESET)
AO ------------------ IO-37 (DC)
SDA ----------------- IO-35 (MOSI)
SCK ----------------- IO-36 (SCLK)
LED ------------------ 3.3V
```

vim: et ts=2 sw=2 et
