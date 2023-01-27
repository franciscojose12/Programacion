package proyecto_java;
import java.util.Scanner;
public class ejercicio_11 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		
		int numeros = 0;
		System.out.println("Introduzca numeros para revelar su cuadrado : ");
		numeros = comienzo.nextInt();
		
		if(numeros>0){
			int numerosCuadrado = numeros*numeros;
			System.out.println("el cuadrado de " + numeros +" es " +numerosCuadrado);

		}
		else  {
			System.out.println("Numero introducido negativo.Cerrando programa");
		}
		
		while(numeros>0) {
			System.out.println("Introduzca numeros para revelar su cuadrado : ");
			numeros = comienzo.nextInt();
			if(numeros<0) {
				System.out.println("Numero introducido negativo.Cerrando programa");
				break;
			}
			
			int cuadrado = numeros*numeros;
			System.out.println("el cuadrado de " + numeros +" es " +cuadrado);
			
			
		}
	}
}
