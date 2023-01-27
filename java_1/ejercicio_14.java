package proyecto_java;
import java.util.Scanner;
public class ejercicio_14 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int numero = 0;
		int contador = 0;
		int suma_impares = 0;
		int mayor = 0 ;
		System.out.println("Introduzca numeros : ");
		numero = comienzo.nextInt();
		while(numero>0) {
			System.out.println("Introduzca numeros : ");
			numero = comienzo.nextInt();
			contador = contador +1;
			if(numero%2==0 && numero>0) {
				if(numero>mayor) {
					mayor=numero;
				}
			}
			if(numero%3==0 && numero>0) {
				suma_impares = suma_impares+numero;
			}
			
	}
		if(numero<0) {
			System.out.println("Numero introducido negativo.Cerrando programa");
		}
		int media_impares = suma_impares/2;
		System.out.println(contador + " Numeros han sido introducidos");
		System.out.println(mayor + " Es el numero mayor de los  pares");
		System.out.println(media_impares + " Es la media de los impares");
}
}
