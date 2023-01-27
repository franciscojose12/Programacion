package proyecto_java;
import java.util.Scanner;
public class ejercicio_17 {
	public static void main(int n) {
		Scanner comienzo = new Scanner (System.in);
		int n1 = 0 , n2 = 1 ;
		StringBuilder sb = new StringBuilder();
		int suma = 0;
		for (int i=0 ; i<=n ; i++) {
			sb.append(n2).append(" ");
			suma = n1+n2;
			n1=n2;
			n2=suma;
		}
	}

}
