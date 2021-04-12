<script>
  import FuncInput from "./_components/FuncInput.svelte";
  import Biseccion from "./_components/Biseccion.svelte";
  import PuntoFijo from "./_components/PuntoFijo.svelte";
  import Newton from "./_components/Newton.svelte";
  import Secante from "./_components/Secante.svelte";
  import Grafico from "./_components/Grafico.svelte";

  let func = "x + 100";
  let func_g = "100";
  let method;
</script>

<div class="datos">
  <div>
    <div>
      <h1>METODO</h1>
      <select bind:value={method}>
        <option value="biseccion">Biseccion</option>
        <option value="punto_fijo">Punto Fijo</option>
        <option value="newton">Newthon raphson</option>
        <option value="secante">Secante</option>
      </select>
    </div>
    <div class="label">
      <h1>F(X)</h1>
      <FuncInput bind:func />
    </div>
    <div class="label">
      {#if method == "punto_fijo"}
        <h1>G(X)</h1>
        <FuncInput bind:func={func_g} />
      {/if}
    </div>
    <h1>GRAFICA</h1>
    <Grafico {func} />
  </div>

  <div>
    {#if method == "biseccion"}
      <Biseccion bind:func />
    {:else if method == "punto_fijo"}
      <PuntoFijo bind:func bind:func_g />
    {:else if method == "newton"}
      <Newton bind:func />
    {:else if method == "secante"}
      <Secante bind:func />
    {/if}
  </div>
</div>

<style>
  .datos {
    display: flex;
    width: 100%;
    justify-content: space-around;
  }
</style>
