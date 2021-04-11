import { Server, Response } from "miragejs";

export function makeServer({ environment = "development" } = {}) {
  let server = new Server({
    environment,
    routes() {
      this.namespace = "api";
      this.timing = 750;

      this.post("/raices/grafico", (request) => {
        return [];
      });

      this.post("/raices/biseccion", (request) => {
        return [];
      });

      this.post("/raices/newton", (request) => {
        return [];
      });

      this.post("/raices/secante", (request) => {
        return [];
      });
    },
  });

  window.server = server;

  return server;
}
