import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class SistemaProcesamientoPedidosTest {

    private SistemaProcesamientoPedidos sistemaProcesamiento;
    private ExecutorService executorService;

    @BeforeEach
    void setUp() {
        // Inicializamos el ExecutorService real
        executorService = Executors.newFixedThreadPool(3); // Usa un pool con 3 threads para el ejemplo
        sistemaProcesamiento = new SistemaProcesamientoPedidos(5,5,5);
    }

    @Test
    void testProcesarPago() throws InterruptedException {
        Pedido pedido = new Pedido(1, true, 100);

        // Ejecutamos la tarea de procesar el pago en el sistema real
        sistemaProcesamiento.procesarPago(pedido);

        // Cerramos el executor y esperamos a que las tareas terminen
        executorService.shutdown();
        executorService.awaitTermination(5, TimeUnit.SECONDS);

        // Verificamos que el pago ha sido procesado correctamente
        assertTrue(pedido.isPagado(), "El pago del pedido debería estar procesado");
    }

    @Test
    void testProcesarEmpaquetado() throws InterruptedException {
        Pedido pedido = new Pedido(2, false, 50);

        // Ejecutamos la tarea de empaquetar el pedido
        sistemaProcesamiento.empaquetarPedido(pedido);

        // Cerramos el executor y esperamos a que las tareas terminen
        executorService.shutdown();
        executorService.awaitTermination(5, TimeUnit.SECONDS);

        // Verificamos que el pedido ha sido empaquetado correctamente
        assertTrue(pedido.isEmpaquetado(), "El pedido debería estar empaquetado");
    }

    @Test
    void testProcesarEnvio() throws InterruptedException {
        Pedido pedido = new Pedido(3, true, 150);

        // Ejecutamos la tarea de enviar el pedido
        sistemaProcesamiento.enviarPedido(pedido);

        // Cerramos el executor y esperamos a que las tareas terminen
        executorService.shutdown();
        executorService.awaitTermination(5, TimeUnit.SECONDS);

        // Verificamos que el pedido ha sido enviado correctamente
        assertTrue(pedido.isEnviado(), "El pedido debería estar enviado");
    }
}