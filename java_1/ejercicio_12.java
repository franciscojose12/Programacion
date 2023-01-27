package proyecto_java;
import java.util.Scanner;
public class ejercicio_12 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int contador = 0;
		int numeros = 0;
		System.out.println("Introduce numeros : ");
		numeros = comienzo.nextInt();
		while(numeros>0) {
			System.out.println("Introduce numeros : ");
			numeros = comienzo.nextInt();
			contador = contador+1;
		}
		System.out.println("Ha introducido : " + contador + " numeros positivo");
	}
}
