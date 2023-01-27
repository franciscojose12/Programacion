package proyecto_java;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Ejercicio 1
		System.out.println("Intoduzca el primer numero :");
		int primerNumero = new Scanner (System.in).nextInt ();
		
		System.out.println("Introduzca el segundo numero :");
		int segundoNumero = new Scanner (System.in).nextInt ();
		
		if(primerNumero%segundoNumero==0) {
			System.out.println("Son multiplos");
			
		}else {
			System.out.println("No son multiplos");
		}
		
	}

}
