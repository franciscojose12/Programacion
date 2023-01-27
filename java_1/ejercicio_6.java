package proyecto_java;
import java.util.Scanner;
public class ejercicio_6 {
	public static void main(String[] args) {
		Scanner comienzo = new Scanner (System.in);
		int dia = 0;
		int mes = 0;
		System.out.println("Introduzca el mes : ");
		mes = comienzo.nextInt();
		while(mes>12 || mes <1) {
			System.out.println("Mes incorrecto.Introduzca un mes : ");
			mes = comienzo.nextInt();
		}
		System.out.println("Introduzca el dia : ");
		dia = comienzo.nextInt();
		while(dia<1 || dia>31) {
			System.out.println("Dia incorrecto.Introduzca el dia : ");
			dia = comienzo.nextInt();
		
		}
		String estacion = " ";
		estacion = estacion.toLowerCase();
		if(mes==12  && dia>21) {
			estacion = "invierno";
		}
		 if(mes<=3 && dia<=20) {
			estacion = "invierno";
		}
		 if(mes==3 && dia>=21) {
			estacion = "Primavera";
		}
		 if(mes<6) {
			estacion = "primavera";
		}
		 if(mes==6 && dia<=21) {
			estacion = "verano";
		}
		 if(mes==9 && dia<=23) {
			estacion = "verano";
		}
		 if(mes==9 && dia<=24) {
			estacion = "otoño";
		}
		 if(mes<12 && mes>9) {
			estacion = "otoño";
		}
		switch (estacion) {
		case "verano" : {
			System.out.println("Los grados corresondiente son 24º");
		}
		break;
		case "invierno" : {
			System.out.println("Los grados correspondiente son 19º");
		}
		break;
		case "otoño" : {
			System.out.println("Los grados correspondiente son 19º");
		}
		break;
		case "primavera" : {
			System.out.println("Los grados correspondiente son 20º");
		}
		}
		
}}
