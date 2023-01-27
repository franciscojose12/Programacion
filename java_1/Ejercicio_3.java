package proyecto_java;

import java.util.Scanner;

public class Ejercicio_3 {
	public static void main(String[] args) {
		String caracter;
		System.out.println("Intrduzca un caracter :");
		Scanner comienzo = new Scanner (System.in);
		caracter = comienzo.nextLine();
		switch (caracter) {
		case " ":{
			System.out.println("Es un espacion en blanco");
		}
		break;
		case "(":{
			System.out.println("Es un parentesis");
		}
		break;
		case ")":{
			System.out.println("Es un parentesis");
		}
		break;
		}
		int numero =Integer.valueOf(caracter);
		if(numero>=0 || numero<=9){
			System.out.println("Es un numero entre el 0 y el 9. Es el numero: " +numero);
		}

	}
}

