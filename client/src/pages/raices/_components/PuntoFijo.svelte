<script>
  import Table from "./Table.svelte";
  import { solve_function } from "./script";

  export let func;
  export let func_g;

  let xi = -1;
  let tol = 1e-6;
  let err = "abs";
  let n_max_iter = 1000;

  let message;
  let raiz;
  let procedimiento = [];

  $: func || func_g || xi || tol || err || n_max_iter ? calculate() : null;

  async function calculate() {
    try {
      const response = await solve_function("punto-fijo", {
        xi,
        tol,
        err,
        n_max_iter,
        func,
        func_g,
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

<div class="prop">
  <div class="table">
    {#if message}
      <h1>RAIZ</h1>
      <div>
        {message}
      </div>
    {:else}
      <div>No se pudo solucionar. Revisa los inputs</div>
    {/if}
  </div>

  <div class="info">
    <h1>PROPIEDADES</h1>
    <label>
      Coordenada inicial
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
