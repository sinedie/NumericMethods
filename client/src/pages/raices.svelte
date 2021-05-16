<script>
  import {
    Select,
    SelectItem,
    Toggle,
    DataTable,
    NumberInput,
    TextInput,
    Accordion,
    AccordionItem,
  } from "carbon-components-svelte";

  let func = "x + 100";
  let func_g = "100";
  let method = "biseccion";
  let xi = -200;
  let xf = 100;
  let tol = 1e-6;
  let err = "abs";
  let regla_falsa = false;
  let n_max_iter = 1000;
  let multiplicidad_raiz = 1;

  let message;
  let raiz;
  let procedimiento = [];

  $: func ||
  func_g ||
  xi ||
  xf ||
  tol ||
  err ||
  regla_falsa ||
  n_max_iter ||
  multiplicidad_raiz ||
  method
    ? calculate()
    : null;

  let xi_grafico = -200;
  let xf_grafico = 0;
  let src;

  $: func || xi_grafico || xf_grafico ? graficar_function() : null;

  async function calculate() {
    try {
      const httpResponse = await fetch(
        `/api/raices/${method}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            xi,
            xf,
            tol,
            err,
            n_max_iter,
            func,
            func_g,
            regla_falsa,
            multiplicidad_raiz,
          }),
        }
      );
      const response = await httpResponse.json();

      raiz = response.raiz[0];
      message = response.raiz[1];
      procedimiento = response.raiz[2].map((row, index) => {
        return {
          id: index,
          x: row[0].toFixed(10),
          fx: row[1].toFixed(10),
          err: row[2].toFixed(10),
        };
      });
    } catch {}
  }

  async function graficar_function() {
    try {
      const httpResponseImage = await fetch(
        "/api/raices/grafico",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ func, xi: xi_grafico, xf: xf_grafico }),
        }
      );
      const response = await httpResponseImage.json();
      src = `data:image/jpeg;base64, ${response.image}`;
    } catch (e) {
      console.log(e);
    }
  }
</script>

<Accordion>
  <AccordionItem title="Opciones" open>
    <TextInput labelText="Funcion" bind:value={func} />
    {#if method == "punto_fijo"}
      <TextInput labelText="G(x)" bind:value={func_g} />
    {/if}

    <Select labelText="Metodo" bind:selected={method}>
      <SelectItem value="biseccion" text="Biseccion" />
      <SelectItem value="punto_fijo" text="Punto Fijo" />
      <SelectItem value="newton" text="Newthon Raphson" />
      <SelectItem
        value="newton_multiple"
        text="Newthon Raphson Raices Multiples"
      />
      <SelectItem value="secante" text="Secante" />
    </Select>

    <Select labelText="Tipo de error" bind:selected={err}>
      <SelectItem value="abs" text="Absoluto" />
      <SelectItem value="rel" text="Relativo" />
    </Select>

    <NumberInput label="Coordenada inicial del intervalo" bind:value={xi} />
    <NumberInput label="Coordenada final del intervalo" bind:value={xf} />
    <NumberInput label="Tolerancia" positive bind:value={tol} />

    <NumberInput
      label="Numero maximo de iteraciones"
      integer
      positive
      bind:value={n_max_iter}
    />

    {#if method == "biseccion"}
      <Toggle labelText="Usar regla falsa" bind:toggled={regla_falsa} />
    {/if}
  </AccordionItem>

  <AccordionItem title="Raiz" open>
    <h2>Raiz: {raiz}</h2>
    Notas: {message}
  </AccordionItem>

  <AccordionItem title="Grafica" open>
    <img {src} alt="Representacion grafica de la funcion" />
    <NumberInput label="Coordenada inicial" bind:value={xi_grafico} />
    <NumberInput label="Coordenada final" bind:value={xf_grafico} />
  </AccordionItem>

  <AccordionItem title="Procedimiento">
    <DataTable
      headers={[
        { key: "id", value: "i" },
        { key: "x", value: "X(i)" },
        { key: "fx", value: "F( X(i) )" },
        { key: "err", value: `Error ${err}` },
      ]}
      rows={procedimiento}
    />
  </AccordionItem>
</Accordion>
