package proyecto_java;
import java.util.Scanner;
public class ejercicio_18 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		 System.out.println("Introduzca un radio:  ");

	     int radio = comienzo.nextInt();
	     System.out.println("El radio introducido es: " + radio);
	     double area;
	     double longitud;
	     area = Math.PI * Math.pow(radio, 2);
	     System.out.println("El area del circulo es: " + area);
	     longitud = (2 * Math.PI) * radio;
	     System.out.println("La longitud de la circunferencia es: " + longitud);
	}

}
