<script>
  import Table from "./Table.svelte";
  import { solve_function } from "./script";

  export let func;

  let xi = -1;
  let xf = 1;
  let tol = 1e-6;
  let err = "abs";
  let regla_falsa = false;
  let n_max_iter = 1000;

  let message;
  let raiz;
  let procedimiento = [];

  $: func || xi || xf || tol || err || regla_falsa || n_max_iter
    ? calculate()
    : null;

  async function calculate() {
    try {
      const response = await solve_function("biseccion", {
        xi,
        xf,
        tol,
        err,
        n_max_iter,
        func,
        regla_falsa,
      });

      raiz = response.raiz;
      message = response.message;
      procedimiento = response.results;
      console.log(response);
    } catch (e) {
      console.log(e);
    }
  }
</script>

<div class="container">
  <div class="table">
    <h1>RAIZ</h1>
    <div>
      {message}
    </div>
  </div>

  <div class="prop">
    <h1>PROPIEDADES</h1>
    <label>
      Coordenada inicial del intervalo
      <input type="text" bind:value={xi} />
    </label>
    <label>
      Coordenada final del intervalo
      <input type="text" bind:value={xf} />
    </label>
    <label>
      Tolerancia
      <input type="text" bind:value={tol} />
    </label>
    <label>
      Tipo de error
      <select bind:value={err}>
        <option value="abs">Absoluto</option>
        <option value="rel">Relativo</option>
      </select>
    </label>
    <label>
      Numero maximo de iteraciones
      <input type="text" bind:value={n_max_iter} />
    </label>
    <label>
      Usar regla falsa
      <input type="checkbox" bind:value={regla_falsa} />
    </label>
  </div>

  {#if procedimiento.length}
    <Table table={procedimiento} encabezado={["x", "f(x)", `Error ${err}`]} />
  {/if}
</div>

<style>
  label {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
</style>
