import py4j.GatewayServer;

public class backend_JVM {

  public int test(int a, int b) {
    return 1 + 2;
  }

  public static void main(String[] args) {
    backend_JVM app = new backend_JVM();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
  }
}

