<script>
  export let table;
  export let encabezado;
  $: console.log(table);
</script>

<h1>PROCEDIMIENTO</h1>

<table>
  <thead>
    {#each encabezado as title}
      <th> {title} </th>
    {/each}
  </thead>
  <tbody>
    {#each table as row}
      <tr>
        {#each row as col}
          <td>
            {col}
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th,
  td {
    text-align: center;
    border: 1px solid rgba(0, 0, 0, 0.151);
  }
</style>
