// Define the pin connected to the LED
const int luzQuarto = 13;
const int luzCozinha = 12;
const int luzSala = 11;

void setup() {
  // Initialize serial communication at a baud rate of 9600
  Serial.begin(9600);
  
  // Set the LED pin as an output
  pinMode(luzQuarto, OUTPUT);
  pinMode(luzCozinha, OUTPUT);
  pinMode(luzSala, OUTPUT);
}

void loop() {
  // Check if data is available to read from serial port
  if (Serial.available() > 0) {
    // Read the incoming byte
    char command = Serial.read();

    // Perform action based on the received command
    if (command == '1') {
      digitalWrite(luzQuarto, HIGH); // Turn on the Quarto
      Serial.println("LED Quarto On");
    } else if (command == '2') {
      digitalWrite(luzQuarto, LOW); // Turn off the Quarto
      Serial.println("LED Quarto Off");
    } else if (command == '3') {
      digitalWrite(luzCozinha, HIGH);
      Serial.println("Led Cozinha On");
    } else if (command == '4'){
      digitalWrite(luzCozinha, LOW);
      Serial.println("Led Cozinha Off");
    }
      else if (command == '5'){
      digitalWrite(luzSala, HIGH);
      Serial.println("Led Sala On");
    } else if (command == '6'){
      digitalWrite(luzSala, LOW);
      Serial.println("Led Sala Off");
    }
  }
}
