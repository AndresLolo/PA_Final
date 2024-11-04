
public class Main {
    public static void main(String[] args) throws InterruptedException {
        // aca se seleccionan la cant de hilos para cada operacion
        SistemaProcesamientoPedidos sistema = new SistemaProcesamientoPedidos(5, 2, 2);


        //generador de pedidos
        Thread generadorPedidos = new Thread(() -> sistema.iniciarGeneracionPedidos());
        generadorPedidos.setPriority(Thread.MAX_PRIORITY);
        generadorPedidos.start();
        // Ejecutar el procesamiento de los pedidos

        new Thread(() -> sistema.procesarPedidos()).start();



        Thread.sleep(10000);

        // Apagar el sistema después de que todos los pedidos hayan sido procesados
        sistema.shutdown();
        //terminar el programa
        System.out.println("Se generaron: " + sistema.getPedidosGenerados());
        System.out.println("Se empaquetaron: " + sistema.getPedidosEmpaquetados());
        System.out.println("Se enviaron: " + sistema.getPedidosEnviados());
        System.out.println("Se pagaron: " + sistema.getPedidosPagados());
        //siempre se logran mas pedidos pagados que los demás debido a que los demás procesos esperan que el
        //pedido sea pagado para continuar

        System.exit(0);
    }
}
