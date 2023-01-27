package proyecto_java;
import java.util.Scanner;
public class ejercicio_8 {
	public static void main(String[] args) {
		int  suma_total = 0;
		for (int i=1; i<=15 ; i++) {
			System.out.println("Introduzca un numero : ");
			int numero = new Scanner (System.in).nextInt ();
			suma_total = suma_total+numero;

		}
		System.out.println("La suma total es  :  "+suma_total);

	}
}
