#include <Wire.h>
//#include "Adafruit_HTU21DF.h"
#include "SHT2x.h"
#include <WiFi.h>
#include <AsyncTCP.h>
//#include <ESPAsyncWebServer.h>

const char* ssid = "ssid";
const char* password = "ssid-pwd";

WiFiServer server(80);

//Adafruit_HTU21DF htu = Adafruit_HTU21DF();
Si7021 sht;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Serial.println("HTU21/D-F test");
  if (!sht.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
  
//sht.reset();
/*  if (!htu.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
*/
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

float g_temp=0;
long g_tm=0;

void loop() {
  if (time(0)>g_tm+2)
  {
    g_tm=time(0);
    g_temp=getHTU('C');
  }
  WiFiClient client = server.available();   // Listen for incoming clients

  if (client) {                             // If a new client connects,
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {  // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             
        if (c == '\n') {                    // if the byte is a newline character
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<link rel=\"icon\" href=\"data:,\">");
            client.println("<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}");
            client.println(".button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
            client.println(".button2 {background-color: #555555;}</style></head>");
            client.println("<body>Teplota:");
    client.println(g_temp);
    //client.println("<br/>Vlhkost:");
    //client.println(getHTU('H'));
            client.println("</body></html>");
            client.println();
            break;
          } else { // if you got a newline, then clear currentLine
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    // Clear the header variable
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }

    
}


/*
 * @brief returns temperature or relative humidity
 * @param "type" is character
 *     C = Celsius
 *     K = Keliven
 *     F = Fahrenheit
 *     H = Humidity
 * @return returns one of the values above
 * Usage: to get Fahrenheit type: getHTU('F')
 * to print it on serial monitor Serial.println(getHTU('F'));
 */
float getHTU(char type)
{
      
  float value;
/*    float temp = htu.readTemperature();
    float rel_hum = htu.readHumidity();
   if(type =='F')
   {
    value = temp *9/5 + 32;//convert to Fahrenheit 
   }else if(type =='K')
   {
    value = temp + 273.15;//convert to Kelvin
   }else if(type =='H')
   {
    value = rel_hum;//return relative humidity
   }else{*/
//    value = temp;// return Celsius
    value=sht.getTemperature();
    Serial.print("nacitanie teploty:");
    Serial.println(value);
   //}
   return value;
}//
