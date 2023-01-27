package proyecto_java;

public class ejercicio_4 {
	public static void main(String[] args) {
		float parte_practica = 7;
		float parte_teorica = 6;
		float parte_problemas = 9;
		float nota_practica = (parte_practica * 10)/100;
		float nota_problemas = (parte_problemas * 50)/100;
		float nota_teorica= (parte_teorica * 40)/100;
		float notaFinal = nota_practica+nota_teorica+nota_problemas;
		
		if (notaFinal<0 || notaFinal>10) {
			System.out.println("Nota invalida.");

		}
		if (notaFinal==0 && notaFinal<5) {
			System.out.println("Nota insuficiente : "+notaFinal);
		}
		if (notaFinal>=5 && notaFinal<7) {
			System.out.println("Nota Suficiente : "+notaFinal);

		}
		if (notaFinal>=7 && notaFinal<9) {
			System.out.println("Nota Notable : "+notaFinal);
		}
		if (notaFinal>=8 && notaFinal<=10) {
			System.out.println("Nota Sobresaliente : "+notaFinal);
		}
	}
}
