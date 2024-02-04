
public class E2{
    public static void main(String[] args) {
        Coche miCoche = new Coche();
        System.out.println(miCoche);
    }

    public static class Coche{
        String cor;
        String modelo;
        String motor;

        void ligar(){
            System.out.println("Embragando el coche");
        }

        void desembragar() {
            System.out.println("Desembragando el coche");
        }
        void acelerar() {
            System.out.println("Acelerando el coche");
        }
        void frenar() {
            System.out.println("Frenando el coche");
        }
        void cambiarMarcha() {
            System.out.println("Cambiando la marcha");
        }
    }
}