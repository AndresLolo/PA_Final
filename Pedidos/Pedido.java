import javax.swing.plaf.basic.ComboPopup;

public class Pedido implements Comparable<Pedido> {
    private final int id;
    private final boolean urgente;
    private int precio;
    private boolean pagado = false;
    private boolean empaquetado = false;
    private boolean enviado = false;

    public Pedido(int id, boolean urgente, int precio) {
        this.id = id;
        this.urgente = urgente;
        this.precio = precio;
    }

    public int getId() { return id; }
    public boolean isUrgente() { return urgente; }
    public int getPrecio() { return precio; }

    public boolean isPagado() { return pagado; }
    public void setPagado(boolean pagado) { this.pagado = pagado; }
    public boolean isEmpaquetado() { return empaquetado; }
    public void setEmpaquetado(boolean empaquetado) { this.empaquetado = empaquetado; }

    public boolean isEnviado() { return enviado; }
    public void setEnviado(boolean enviado) { this.enviado = enviado; }


    @Override
    public int compareTo(Pedido otroPedido) {
        if (this.urgente && !otroPedido.isUrgente()) {
            return -1; // El pedido actual tiene prioridad
        } else if (!this.urgente && otroPedido.isUrgente()) {
            return 1; // El otro pedido tiene prioridad
        }

        // Si ambos son urgentes o ambos no son urgentes, comparar por precio
        return Integer.compare(otroPedido.getPrecio(),this.precio);
    }

}

