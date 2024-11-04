public class Contadores {
    private int contadorPagados;
    private int contadorEmpaquetados;
    private int contadorEnviados;

    public Contadores() {
        this.contadorPagados = 0;
        this.contadorEmpaquetados = 0;
        this.contadorEnviados = 0;
    }

    public synchronized void incrementarPagados() {
        contadorPagados++;
    }


    public synchronized int getContadorPagados() {
        return contadorPagados;
    }

    public synchronized int getContadorEmpaquetados() {
        return contadorEmpaquetados;
    }

    public synchronized void incrementarEmpaquetados() {
        this.contadorEmpaquetados++;
    }

    public synchronized int getContadorEnviados() {
        return contadorEnviados;
    }

    public synchronized void incrementarEnviados() {
        this.contadorEnviados ++;
    }
}

