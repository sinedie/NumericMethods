<script>
  import { graficar } from "./script";

  export let func;
  export let xi = 0;
  export let xf = 100;

  let src;

  $: func || xi || xf ? graficar_function() : null;

  async function graficar_function() {
    try {
      const response = await graficar(func, xi, xf);
      src = `data:image/jpeg;base64, ${response.image}`;
      console.log(response);
    } catch (e) {
      console.log(e);
    }
  }
</script>

<div class="container">
  <img {src} alt="Representacion grafica de la funcion" />

  <div class="inputs">
    <div>
      <h4>Ordenada inicial</h4>
      <input type="text" bind:value={xi} />
    </div>
    <div>
      <h4>Ordenada final</h4>
      <input type="text" bind:value={xf} />
    </div>
  </div>
</div>

<style>
  .container {
    display: flex;
    flex-direction: column;
  }
  .inputs {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 5%;
  }
</style>
