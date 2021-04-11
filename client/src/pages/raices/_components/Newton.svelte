<script>
  import Table from "./Table.svelte";
  import { solve_function } from "./script";

  export let func;

  let xi = -1;
  let tol = 1e-6;
  let err = "abs";
  let multiplicidad_raiz = 1;
  let n_max_iter = 1000;

  let message;
  let raiz;
  let procedimiento = [];

  $: func || xi || tol || err || multiplicidad_raiz || n_max_iter
    ? calculate()
    : null;

  async function calculate() {
    try {
      const response = await solve_function("newton", {
        xi,
        tol,
        err,
        n_max_iter,
        func,
        multiplicidad_raiz,
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
    <div>
      {raiz}
    </div>
    <div>
      {message}
    </div>
    <Table
      table={procedimiento}
      encabezado={["x", "f(x)", "f'(x)", `Error ${err}`]}
    />
  </div>
  <div class="info">
    <label>
      Coordenada inicial del intervalo
      <input type="text" bind:value={xi} />
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
      Multiplicidad de raiz
      <input type="text" bind:value={multiplicidad_raiz} />
    </label>
  </div>
</div>

<style>
  .container {
    margin-top: 10%;
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  label {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
</style>
