package proyecto_java;
import java.util.Scanner;
public class ejercicio_16 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int suma = 0;
		int numero = 0;
		int mayor_s = 0;
		for (int i=0;i<10;i++) {
			System.out.println("Introduce numeros");
			numero = comienzo.nextInt();
			suma = suma+numero;
			if(numero>1000) {
				mayor_s++;
			}
		}
		System.out.println("La suma de los salarios es : " + suma);
		System.out.println("Hay "+ mayor_s + " Salarios mayor a 1000");
	}
}
