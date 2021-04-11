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
  let xi = 0;
  let xf = 100;
</script>

<div class="label">
  F(X) =
  <FuncInput bind:func />
</div>
<div class="label">
  {#if method == "punto_fijo"}
    G(X) =
    <FuncInput bind:func={func_g} />
  {/if}
</div>

<select bind:value={method}>
  <option value="biseccion">Biseccion</option>
  <option value="punto_fijo">Punto Fijo</option>
  <option value="newton">Newthon raphson</option>
  <option value="secante">Secante</option>
</select>

<input type="text" bind:value={xi} />
<input type="text" bind:value={xf} />
<Grafico {func} {xi} {xf} />

{#if method == "biseccion"}
  <Biseccion bind:func />
{:else if method == "punto_fijo"}
  <PuntoFijo bind:func bind:func_g />
{:else if method == "newton"}
  <Newton bind:func />
{:else if method == "secante"}
  <Secante bind:func />
{/if}
