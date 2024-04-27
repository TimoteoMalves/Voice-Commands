#include <SPI.h>
#include <Ethernet.h>
#include <LiquidCrystal.h>

const int rs = 7, en = 6, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Enter a MAC address and IP address for your controller below.
byte mac[] = { 0x82, 0x2E, 0xA4, 0x66, 0xB0, 0xAF };
IPAddress ip(192, 168, 197, 222); // Change to your desired IP address
const int LivingRoom = 8;

// Initialize the Ethernet server library
EthernetServer server(80);

void setup() {
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.begin(9600);
  Serial.println("Server started");
  lcd.begin(16, 2);
  // Print the IP address
  Serial.print("IP Address: ");
  Serial.println(Ethernet.localIP());
  pinMode(LivingRoom, OUTPUT);
}

void loop() {
  // listen for incoming clients
  lcd.setcursor(0,1);
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        lcd.print("ligths on");
        digitalWrite(LivingRoom, HIGH);
        
        if (c == '\n' && currentLineIsBlank) {
          // Send HTTP response
          client.println((const char*)"HTTP/1.1 200 OK");
          client.println((const char*)"Content-Type: text/html");
          client.println("Connection: close");

          break;
        }
        if (c == '\n') {
          currentLineIsBlank = true;
        } else if (c != '\r') {
          currentLineIsBlank = false;
        }
      }
    }
    
    client.stop(); // Close the connection
    Serial.println("client disconnected");
  }
}
