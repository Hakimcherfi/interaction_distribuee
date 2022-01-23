const int sensorPin = A0;
const float baselineTemp = 20.0;
void setup() {
  // put your setup code here, to run once:
pinMode(LED_BUILTIN, OUTPUT);

  

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorVal = analogRead(sensorPin);
  float temperature = (sensorVal/1024.0*5.0-0.5)*100;
  Serial.begin(9600);
  Serial.println(temperature);
  Serial.end();
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
