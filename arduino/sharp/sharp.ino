int led = 2;
int sensor_izquierdo = A1;
float lectura_izquierdo;
int dist_izquierdo;

const int triger = 4;
const int echo = 3;
long tiempo;
int distancia;
    
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  pinMode(triger, OUTPUT);
  pinMode(echo, INPUT); 
  Serial.begin(9600);
   
}

// the loop routine runs over and over again forever:
void loop() {
  
  
  sharp();
  sensorultrasonido();
  int sharp_izq = dist_izquierdo;
  
  Serial.print(dist_izquierdo);
  //Serial.println(" sharp");
  //delay(100);
  Serial.print(distancia);
  //Serial.println(" ultra");
  delay(100);
  
  //delay(100);//este tiempo debe estar si o si entre envio y recibo o si no no recibe desde serial
  
  
  /*if (dist_izquierdo < 20) 
  {
    digitalWrite(led, HIGH);
  }
    
  if (dist_izquierdo > 20)
  {
    digitalWrite(led, LOW);
  }*/
  
  if (Serial.available() != 0){ // espera si recibe algo por el puerto serial desde la raspberry
    
    String dato = Serial.readStringUntil('\n');// con \n se descarta los saltos de linea que pueda llegar desde raspberry
    /*String dato = Serial.read();
    Serial.write(dato);*/
     if (dato == "1"){
        digitalWrite(led, HIGH);
     }
     
     else if (dato == "0"){
        digitalWrite(led, LOW);
     }
   
     
  }//delay(50);
}

void sharp(){
  

      lectura_izquierdo = analogRead(sensor_izquierdo);
      //delay(10);
      dist_izquierdo=pow(3027.4/lectura_izquierdo,1.2134);
      
      
   
 }
 
 void sensorultrasonido()
 {
   
   digitalWrite(triger, LOW);
   delayMicroseconds(2);
   
   digitalWrite(triger, HIGH);
   delayMicroseconds(10);
   tiempo=pulseIn(echo, HIGH);
   distancia = tiempo/58;
   
 }
