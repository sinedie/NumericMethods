<script>
  import {
    Grid,
    Row,
    Column,
    Slider,
    Button,
    Select,
    SelectItem,
    NumberInput,
    Accordion,
    AccordionItem,
    StructuredList,
    StructuredListCell,
    StructuredListRow,
    DataTable,
  } from "carbon-components-svelte";

  let method = "gauss";
  let pivoteo = false;
  let tol = 1e-6;
  let n_iter_max = 1000;
  let size = 3;
  let A = arrayCero(size).map((row) => arrayCero(size));
  let b = arrayCero(size);
  let x0 = arrayCero(size);
  let result = [];

  $: if (size < b.length) {
    b = b.slice(0, size);
    A = A.slice(0, size).map((row) => row.slice(0, size));
  } else if (size > b.length) {
    const nColsToAdd = size - b.length;

    b = [...b, ...arrayCero(nColsToAdd)];
    A = [
      ...A.map((row) => [...row, ...arrayCero(nColsToAdd)]),
      ...arrayCero(nColsToAdd).map((row) => arrayCero(b.length)),
    ];
  }

  $: A || b || method || pivoteo || tol || n_iter_max ? calculate() : null;

  async function calculate() {
    const httpResponse = await fetch(
      `/api/ecuaciones/${method}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ A, b, pivoteo, tol, n_iter_max, x0 }),
      }
    );

    const response = await httpResponse.json();
    result = response.results[0].map((x, id) => {
      return {
        id: id + 1,
        x,
      };
    });

    console.log(response);
  }

  function arrayCero(size) {
    return [...Array(size)].map((a) => 0);
  }

  function clear() {
    A = A.map((row) => row.map((col) => 0));
    b = b.map((row) => 0);
  }

  function eye() {
    A = A.map((row, i) => row.map((col, j) => Number(i == j)));
  }

  function U() {
    A = A.map((row, i) => row.map((col, j) => (i < j ? 0 : col)));
  }

  function L() {
    A = A.map((row, i) => row.map((col, j) => (i > j ? 0 : col)));
  }

  function diag() {
    A = A.map((row, i) => row.map((col, j) => (i == j ? col : 0)));
  }

  function random() {
    const max = 1000;
    const min = -1000;
    A = A.map((row) =>
      row.map((col) => Math.floor(Math.random() * (max - min)) + min)
    );
  }
</script>

<Accordion>
  <AccordionItem title="Opciones" open>
    <Slider
      min={2}
      max={8}
      step={1}
      labelText="Tamano de la matriz"
      bind:value={size}
    />

    <Select labelText="Metodo" bind:selected={method}>
      <SelectItem value="gauss" text="Gauss" />
      <SelectItem value="seidel" text="Gauss Seidel" />
      <SelectItem value="jacobi" text="Jacobi" />
      <SelectItem value="sor" text="SOR" />
    </Select>

    {#if ["jacobi", "seidel"].includes(method)}
      <NumberInput label="Tolerancia" positive bind:value={tol} />
      <NumberInput
        label="Numero maximo de iteraciones"
        positive
        integer
        bind:value={n_iter_max}
      />
    {/if}

    {#if ["gauss"].includes(method)}
      <Select labelText="Pivoteo" bind:selected={pivoteo}>
        <SelectItem value={false} text="Ninguno" />
        <SelectItem value="parcial" text="Parcial" />
        <SelectItem value="total" text="Total" />
      </Select>
    {/if}
  </AccordionItem>

  <AccordionItem title="Ecuaciones" open>
    {#if ["jacobi", "seidel"].includes(method)}
      <h2>X inicial</h2>

      <Grid>
        {#each x0 as row}
          <Row>
            <Column>
              <NumberInput bind:value={row} />
            </Column>
          </Row>
        {/each}
      </Grid>
    {/if}

    <h2>Sistema de ecuaciones A*b = x</h2>

    <Button kind="ghost" on:click={clear}>Limpiar</Button>
    <Button kind="ghost" on:click={U}>Limpiar U</Button>
    <Button kind="ghost" on:click={L}>Limpiar L</Button>
    <Button kind="ghost" on:click={diag}>Solo la diagonal</Button>
    <Button kind="ghost" on:click={eye}>Generar identidad</Button>
    <Button kind="ghost" on:click={random}>Matriz aleatoria</Button>

    <StructuredList>
      {#each A as row, row_i}
        <StructuredListRow style="border: none;">
          {#each row as col}
            <StructuredListCell style="padding: 5px;">
              <NumberInput bind:value={col} />
            </StructuredListCell>
          {/each}

          <StructuredListCell style="padding: 5px;">*</StructuredListCell>
          <StructuredListCell style="padding: 5px;">
            X<sub>{row_i + 1}</sub>
          </StructuredListCell>
          <StructuredListCell style="padding: 5px;">=</StructuredListCell>

          <StructuredListCell style="padding: 5px;">
            <NumberInput bind:value={b[row_i]} />
          </StructuredListCell>
        </StructuredListRow>
      {/each}
    </StructuredList>
  </AccordionItem>

  <AccordionItem title="Resultados">
    <DataTable
      headers={[
        { key: "id", value: "i" },
        { key: "x", value: "x(i)" },
      ]}
      rows={result}
    />
  </AccordionItem>

  <AccordionItem title="Procedimiento">TODO</AccordionItem>
</Accordion>
