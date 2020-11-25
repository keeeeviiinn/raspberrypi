int led = 2;
int sensor_izquierdo = A1;
float lectura_izquierdo;
int dist_izquierdo;

const int triggerEmisorizq = 4;
const int echoReceptorizq = 3;
long tiempoEntradaizq;  // Almacena el tiempo de respuesta del sensor de entrada
int distanciaultra;  // Almacena la distancia en cm a la que se encuentra el objeto

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  pinMode(triggerEmisorizq,OUTPUT); // El emisor emite por lo que es configurado como salida
  pinMode(echoReceptorizq,INPUT);   // El receptor recibe por lo que es configurado como entrada
 
  Serial.begin(9600);      
}

// the loop routine runs over and over again forever:
void loop() {
  
  
  sharp();
  sensorUltrasonidos();
  int sharp_izq = dist_izquierdo;
  Serial.println(dist_izquierdo);
  Serial.println(distanciaultra);
  delay(10);//este tiempo debe estar si o si entre envio y recibo o si no no recibe desde serial
  
  
 /* if (dist_izquierdo < 20) 
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
      delay(10);
      dist_izquierdo=pow(3027.4/lectura_izquierdo,1.2134);
 }
 
 void sensorUltrasonidos()
    {
        // Se inicializa el sensor de infrasonidos izq
        digitalWrite(triggerEmisorizq,LOW);  // Para estabilizar
        delayMicroseconds(2);
     
        // Comenzamos las mediciones
        // Se envía una señal activando la salida trigger durante 10 microsegundos
        digitalWrite(triggerEmisorizq, HIGH);  // envío del pulso ultrasónico
        delayMicroseconds(10);
        tiempoEntradaizq=pulseIn(echoReceptorizq, HIGH); 
        distanciaultra= tiempoEntradaizq/58; // Fór
    }
