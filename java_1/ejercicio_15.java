package proyecto_java;
import java.util.Scanner;
public class ejercicio_15 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int numero = 0;
		int suma = 0;
		for(int i=0;i<10;i++) {
			System.out.println("Introduce numeros : ");
			numero = comienzo.nextInt();
			if (numero>0) {
				suma = suma+numero;
			}
		
		}
		System.out.println(suma + " Es la suma ");
		System.out.println("Fin");
	}
}
