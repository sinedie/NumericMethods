<script>
  export let func = "x + 100";
</script>

<div class="container">
  <div class="input_container">
    <input type="text" placeholder="Funcion" bind:value={func} />
    <button
      on:click={() => {
        func = "";
      }}
    >
      Limpiar
    </button>
  </div>

  <div class="utils">
    <button
      on:click={() => {
        func += "exp()";
      }}
    >
      Exp
    </button>

    <button
      on:click={() => {
        func += "Abs()";
      }}
    >
      Abs
    </button>

    <button
      on:click={() => {
        func += "Ln()";
      }}
    >
      Ln
    </button>
  </div>
</div>

<style>
  .container {
    display: flex;
    flex-direction: column;
  }
  .utils {
    display: flex;
  }
</style>
