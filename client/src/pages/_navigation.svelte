<script>
  import { getContext } from "svelte";

  import {
    Header,
    HeaderNav,
    HeaderNavItem,
  } from "carbon-components-svelte";

  const ctx = getContext("Theme");

  $: if (ctx) {
    ctx.dark.subscribe((value) => {
      console.log("dark mode?", value);
    });
    ctx.light.subscribe((value) => {
      console.log("light mode?", value);
    });
    ctx.updateVar("--cds-productive-heading-06-font-size", "4rem");
  }
</script>

<Header company="EAFIT" platformName="Procesos numericos" href="/">
  <HeaderNav>
    <HeaderNavItem href="raices" text="Raices" />
    <HeaderNavItem href="ecuaciones" text="Sistemas de ecuaciones" />
    <HeaderNavItem href="interpolacion" text="Interpolacion" />
    <HeaderNavItem href="integracion" text="Integracion" />
    <HeaderNavItem href="about" text="Acerca" />
  </HeaderNav>
</Header>
