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

<img {src} alt="Representacion grafica de la funcion" />
