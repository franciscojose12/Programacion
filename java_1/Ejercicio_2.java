package proyecto_java;

import java.util.Scanner;

public class Ejercicio_2 {
	public static void main(String[] args) {
		String dia_semana;
		System.out.println("Intrduzca un dia de la semana :");
		Scanner comienzo = new Scanner (System.in);
		dia_semana = comienzo.nextLine();
		dia_semana = dia_semana.toLowerCase();
		while(!dia_semana.equals("lunes") && !dia_semana.equals("martes") && !dia_semana.equals("miercoles") && !dia_semana.equals("jueves") && !dia_semana.equals("viernes")) {
			System.out.println("Dia incorrecto.Intrduzca un dia de la semana :");
			dia_semana = comienzo.nextLine();
			dia_semana = dia_semana.toLowerCase();
		};
		switch (dia_semana) {
		
		case "lunes": {
			System.out.println(dia_semana +"  Toca a primera hora Base de Datos.");
		} 
		break;
		
		case "martes": {
			System.out.println(dia_semana +"  Toca a primera hora Programacion.");
		}
		break;

		case "miercoles": {
			System.out.println(dia_semana +"  Toca a primera hora Programacion.");
		
		}
		break;

		case "jueves": {
			System.out.println(dia_semana +"  Toca a primera hora FOL.");
		}
		break;

		case "viernes": {
			System.out.println(dia_semana +"  Toca a primera hora Programacion.");
		}
		}
		}
	
	}

