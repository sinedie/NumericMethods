<script>
  import {
    Slider,
    Select,
    SelectItem,
    NumberInput,
    StructuredList,
    StructuredListCell,
    StructuredListRow,
    Button,
    Accordion,
    AccordionItem,
    ButtonSet,
    DataTable,
  } from "carbon-components-svelte";

  let method = "newton";
  let procedimiento = [];
  let polinomios = [];
  let size = 3;
  let error;
  let x = [1, 2, 3];
  let y = [1, 2, 3];

  $: if (size < x.length) {
    x = x.slice(0, size);
    y = y.slice(0, size);
  } else if (size > x.length) {
    const nColsToAdd = size - x.length;
    x = [...x, ...arrayCero(nColsToAdd)];
    y = [...y, ...arrayCero(nColsToAdd)];
  }

  $: x || y || method ? calculate() : null;

  async function calculate() {
    try {
      const httpResponse = await fetch(
        `/api/interpolacion/${method}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ x, y }),
        }
      );

      if (!httpResponse.ok) {
        throw "Parece haber un error en los inputs o el servidor";
      }

      const response = await httpResponse.json();
      polinomios = response.interpolacion[0].map((pol, id) => {
        return {
          id,
          pol,
        };
      });
      procedimiento = response.interpolacion[1].map((proc, id) => {
        return {
          id,
          proc,
        };
      });
    } catch (e) {
      error = e;
    }
  }

  function arrayCero(size) {
    return [...Array(size)].map((a) => 0);
  }

  function clear() {
    x = x.map((_) => 0);
    y = y.map((_) => 0);
  }

  function random() {
    const max = 1000;
    const min = -1000;
    y = y.map((_) => Math.floor(Math.random() * (max - min)) + min);
  }
</script>

<Accordion>
  <AccordionItem title="Opciones" open>
    <Slider
      min={2}
      max={30}
      step={1}
      labelText="Cantidad de puntos"
      bind:value={size}
    />

    <Select labelText="Metodo" bind:selected={method}>
      <SelectItem value="newton" text="Newton" />
      <SelectItem value="lagrange" text="Lagrange" />
      <SelectItem value="spline_lineal" text="Spline lineal" />
      <SelectItem value="spline_cuadratico" text="Spline cuadratico" />
      <SelectItem value="spline_cubico" text="Spline cubico" />
    </Select>

    <ButtonSet stacked>
      <Button kind="ghost" on:click={clear}>Limpiar</Button>
      <Button kind="ghost" on:click={random}>Puntos aleatorios</Button>
    </ButtonSet>
  </AccordionItem>

  <AccordionItem title="Puntos" open>
    <StructuredList>
      <StructuredListRow head style="border: none">
        <StructuredListCell head>x</StructuredListCell>
        <StructuredListCell head>F(x)</StructuredListCell>
      </StructuredListRow>
      {#each x as row, i}
        <StructuredListRow style="border: none">
          <StructuredListCell style="padding: 0px;">
            <NumberInput bind:value={x[i]} />
          </StructuredListCell>
          <StructuredListCell style="padding: 0px;">
            <NumberInput bind:value={y[i]} />
          </StructuredListCell>
        </StructuredListRow>
      {/each}
    </StructuredList>
  </AccordionItem>

  {#if error}
    <AccordionItem title="ERROR" open>
      {error}
    </AccordionItem>
  {:else}
    <AccordionItem title="Polinomios" open>
      <DataTable
        headers={[
          { key: "id", value: "i" },
          { key: "pol", value: "P(i)" },
        ]}
        rows={polinomios}
      />
    </AccordionItem>
    <AccordionItem title="Procedimiento">
      <DataTable
        headers={[
          { key: "id", value: "i" },
          { key: "proc", value: "P(i)" },
        ]}
        rows={procedimiento}
      />
    </AccordionItem>
  {/if}
</Accordion>
