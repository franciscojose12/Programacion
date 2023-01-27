package proyecto_java;
import java.util.Scanner;
public class ejercicio_5 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int hora = 0;
		System.out.println("Introduzca la hora : ");
		hora = comienzo.nextInt();
		while(hora>24 || hora<0) {
			System.out.println("Hora incorrecta.Introduzca la hora : ");
			hora = comienzo.nextInt();
		}
		if(hora>=6 && hora<=12) {
			System.out.println("Buenos dias Jose Manuel ");
		}
		if(hora>=13 && hora<=20) {
			System.out.println("Buenas tardes Jose Manuel ");
		}
		if (hora>20 && hora<=5) {
			System.out.println("Buenas noches Jose Manuel");
		}	
		
	
	
	}
}
