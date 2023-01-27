package proyecto_java;
import java.util.Scanner;
public class ejercicio_13 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int mayor = 0;
		int menor = 9999999;
		for(int i=0;i<10;i++) {
			System.out.println("Introduce numeros : ");
			int numero = comienzo.nextInt();
			
			
			if (numero>mayor){
				mayor=numero;
			}
			if (numero<menor){
				menor=numero;
			}

		}
		System.out.println("El numero mayor de los numeros introducidos es  : " + mayor);
		System.out.println("El numero menor de los numeros introducidos es  : " + menor);
		
	}
}
