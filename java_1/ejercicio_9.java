package proyecto_java;
import java.util.Scanner;
public class ejercicio_9 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int numero=0;
		boolean multiplo_tres = false;
		for(int i=0 ; i<5 ; i++) {
			System.out.println("Introduzca un numero : ");
			numero=comienzo.nextInt();
			if (numero%3==0) {
				multiplo_tres = true;
			}
		}
		if(multiplo_tres == true) {
			System.out.println("Existen numeros multiplos de 3");
		}
		else {
			System.out.println("No existen numeros multiplos de 3");
		}


	
	}
}
