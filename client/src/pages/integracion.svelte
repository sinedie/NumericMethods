<script>
  import {
    Select,
    SelectItem,
    TextInput,
    NumberInput,
    Accordion,
    AccordionItem,
  } from "carbon-components-svelte";

  let func = "x + 100";
  let method = "simpson";
  let xi = 0;
  let xf = 3;
  let n = 2;
  let integral;
  let error;
  $: h = Math.abs(xf - xi) / n;
  $: func || method || xi || xf || n ? calculate() : null;

  async function calculate() {
    const httpResponse = await fetch(
      `/api/integracion/${method}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ func, xi, xf, n }),
      }
    );

    if (httpResponse.ok) {
      const response = await httpResponse.json();
      integral = response.integral;
      error = null;
    } else {
      error = "Parece haber un error en los inputs o el servidor";
    }
  }
</script>

<Accordion>
  <AccordionItem title="Opciones" open>
    <TextInput labelText="Funcion" bind:value={func} />

    <Select labelText="Metodo" bind:selected={method}>
      <SelectItem value="simpson" text="Simpson" />
      <SelectItem value="trapecio" text="Trapecio" />
    </Select>

    <NumberInput label="Coordenada inicial" bind:value={xi} />
    <NumberInput label="Coordenada final" bind:value={xf} />
    <NumberInput label="Numero de divisiones" bind:value={n} />
  </AccordionItem>

  {#if error}
    {error}
  {:else}
    <AccordionItem title="Integral" open>
      Altura usada: {h}
      <h2>Resultado: {integral}</h2>
    </AccordionItem>
  {/if}
</Accordion>
