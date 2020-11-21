int led = 13;
int sensor_izquierdo = A1;
float lectura_izquierdo;
int dist_izquierdo;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT); 
  Serial.begin(9600);      
}

// the loop routine runs over and over again forever:
void loop() {
  
  
  sharp();
  int sharp_izq = dist_izquierdo;
  Serial.println(sharp_izq);
}

void sharp(){
  

      lectura_izquierdo = analogRead(sensor_izquierdo);
      delay(10);
      dist_izquierdo=pow(3027.4/lectura_izquierdo,1.2134);
      
      
   
 }
