
import java.util.Random;
import java.util.concurrent.*;
import java.util.Comparator;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;


//FALTA OVERRIDE DEL METODO RUN
public class SistemaProcesamientoPedidos {
    private final PriorityBlockingQueue colaPrioridadPedidos;
    private final ExecutorService pagoExecutorService;
    private final ExecutorService empaquetadoExecutorService;
    private final ExecutorService envioExecutorService;
    public int pedidosGenerados;

    private Contadores contadores;
    private final ScheduledExecutorService generadorPedidosExecutorService;
    public SistemaProcesamientoPedidos(int numHilosPago, int numHilosEmpaquetado, int numHilosEnvio) {

        this.colaPrioridadPedidos = new PriorityBlockingQueue<Pedido>();
        this.pagoExecutorService = Executors.newFixedThreadPool(numHilosPago);
        this.empaquetadoExecutorService = Executors.newFixedThreadPool(numHilosEmpaquetado);
        this.envioExecutorService = Executors.newFixedThreadPool(numHilosEnvio);
        this.generadorPedidosExecutorService = Executors.newScheduledThreadPool(1);
        this.contadores = new Contadores();
    }
    public void crearNuevoPedido() {
        // Crea un nuevo pedido con un ID aleatorio, urgencia aleatoria y precio aleatorio
        Random random = new Random();
        Pedido nuevoPedido = new Pedido(random.nextInt(1000), random.nextBoolean() , random.nextInt(200)+1);
        agregarPedido(nuevoPedido);
        System.out.println("Generando nuevo pedido: " + nuevoPedido.getId());
    }
    public void iniciarGeneracionPedidos() {
        // Generar un nuevo pedido cada 2 segundos (o el tiempo que desees).
        generadorPedidosExecutorService.scheduleAtFixedRate(() -> {
            crearNuevoPedido();
            pedidosGenerados++;
            ;
        }, 0, 100, TimeUnit.MILLISECONDS);  // Genera un pedido cada 0,1 segundos.
    }

    public void procesarPedidos() {
        while (true) {
            try {
                Pedido pedido = (Pedido) colaPrioridadPedidos.take();
                procesarPedido(pedido);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    public void agregarPedido(Pedido pedido) {
        colaPrioridadPedidos.offer(pedido);
    }



    public void procesarPedido(Pedido pedido) {
        // Procesamiento de Pago

        CompletableFuture<Void> pagoFuture = CompletableFuture.runAsync(() -> {
            try {
                procesarPago(pedido);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }, pagoExecutorService);

        // Empaquetado, después de que se procese el pago
        CompletableFuture<Void> empaquetadoFuture = pagoFuture.thenRunAsync(() -> {
            try {
                empaquetarPedido(pedido);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }, empaquetadoExecutorService);

        // Envío, después de que se empaquete el pedido
        empaquetadoFuture.thenRunAsync(() -> {
            try {
                enviarPedido(pedido);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }, envioExecutorService);

    }

    public void procesarPago(Pedido pedido) throws InterruptedException {

        Thread.sleep(250);
        pedido.setPagado(true);
        System.out.println(" Pago para pedido: " + pedido.getId() + " procesado");
        contadores.incrementarPagados(); //suma 1 al contador

    }

    public void empaquetarPedido(Pedido pedido) throws InterruptedException {

        // Usamos un stream paralelo para las dos tareas: impresión y preparación
        Stream.of(
                        (Runnable)  () -> {
                            try {
                                impresionEtiquetas(pedido);
                            } catch (InterruptedException e) {
                                throw new RuntimeException(e);
                            }
                        },   // Primera tarea: imprimir etiquetas
                        (Runnable) () -> {
                            try {
                                preparacionArticulos(pedido);
                            } catch (InterruptedException e) {
                                throw new RuntimeException(e);
                            }
                        }  // Segunda tarea: preparar artículos
                )
                .parallel()  // Ejecución en paralelo
                .forEach(Runnable::run);  // Ejecuta cada tarea

        pedido.setEmpaquetado(true);  // Marcamos el pedido como empaquetado después de ejecutar las dos tareas
        System.out.println("Pedido empaquetado: " + pedido.getId());
        contadores.incrementarEmpaquetados(); //suma 1 al contador

    }
    private void impresionEtiquetas(Pedido pedido) throws InterruptedException {

        Thread.sleep(40);
        System.out.println("Etiquetas para pedido: " + pedido.getId() + " impresas");


    }
    private void preparacionArticulos(Pedido pedido) throws InterruptedException {
        Thread.sleep(60);
        System.out.println("Artículos para pedido: " + pedido.getId()+ " preparados");

    }

    public void enviarPedido(Pedido pedido) throws InterruptedException {


        pedido.setEnviado(true);
        Thread.sleep(100);
        System.out.println("Pedido: " + pedido.getId() + " enviado");
        contadores.incrementarEnviados(); //suma 1 al contador

    }

    public void shutdown() throws InterruptedException {

        generadorPedidosExecutorService.shutdownNow();
        System.out.println("Esperando a que los hilos de generación de pedidos terminen...");

        pagoExecutorService.shutdown();
        System.out.println("Esperando a que los hilos de pago terminen...");

        empaquetadoExecutorService.shutdown();
        System.out.println("Esperando a que los hilos de empaquetado terminen...");

        envioExecutorService.shutdown();
        System.out.println("Esperando a que los hilos de envío terminen...");

        pagoExecutorService.awaitTermination(1, TimeUnit.SECONDS);
        empaquetadoExecutorService.awaitTermination(1, TimeUnit.SECONDS);
        envioExecutorService.awaitTermination(1, TimeUnit.SECONDS);

    }
    public int getPedidosGenerados(){
        return pedidosGenerados;
    }
    public int getPedidosPagados(){
        return contadores.getContadorPagados();
    }
    public int getPedidosEmpaquetados(){
        return contadores.getContadorEmpaquetados();
    }
    public int getPedidosEnviados(){
        return contadores.getContadorEnviados();
    }

}
