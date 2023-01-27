package proyecto_java;
import java.util.Scanner;
public class ejercicio_10 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int numero = 0;
		int suma = 0;
		int contador = 0;
		System.out.println("Introduce un numero : ");
		numero = comienzo.nextInt();
		if (numero>0) {
			while(contador<100){
				contador++;
				numero++;
				suma = suma +numero ;
			}
		}
		System.out.println("La suma es "+ suma);
	}
}
